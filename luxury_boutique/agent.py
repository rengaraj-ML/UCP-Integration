from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import requests

# --- TOOL 1: Search Catalog ---
def search_catalog(query: str) -> list:
    """Searches the luxury boutique catalog for fashion advice and items."""
    try:
        # Calls your FastAPI server on port 8182
        r = requests.get("http://localhost:8182/products", timeout=5)
        products = r.json()
        # Filters for matching words in name or description
        matches = [p for p in products if query.lower() in str(p).lower()]
        return matches if matches else products
    except Exception as e:
        return [{"error": f"Could not connect to catalog: {str(e)}"}]

# Wrap search_catalog in FunctionTool
search_catalog_tool = FunctionTool(search_catalog)

# --- TOOL 2: Checkout ---
def start_checkout(sku: str) -> dict:
    """Starts a purchase session for the given SKU."""
    try:
        r = requests.post("http://localhost:8182/sessions", json={"sku": sku}, timeout=5)
        return r.json()
    except Exception as e:
        return {"error": f"Checkout failed: {str(e)}"}

# Bypass the "Confirm" button in the UI
checkout_tool = FunctionTool(start_checkout, require_confirmation=False)

# --- THE AGENT ---
root_agent = Agent(
    name="luxury_shopper",
    model="gemini-2.5-flash", 
    instruction="""You are an elite style consultant for LuxeLife. 
    
    DISPLAY RULES:
    - You MUST display products in a side-by-side tile gallery using HTML.
    - Use this exact HTML structure for the gallery:
    
    <div style="display: flex; flex-wrap: wrap; gap: 10px;">
      <div style="border: 1px solid #ddd; border-radius: 8px; padding: 10px; width: 180px; text-align: center;">
        <img src="IMAGE_URL" style="width: 100%; height: 120px; object-fit: cover; border-radius: 4px;">
        <h4 style="margin: 5px 0; font-size: 14px;">PRODUCT_NAME</h4>
        <p style="margin: 5px 0; font-size: 12px; color: #555;">$PRICE | SKU</p>
      </div>
    </div>
    
    GUIDELINES:
    1. When a user asks for advice, ALWAYS use 'search_catalog'.
    2. Even if the user asks for something specific (like a "dress"), show ALL relevant elegant options from the collection to provide variety. 
    3. Aim to show at least 3 items in the tile gallery for every recommendation.
    4. Do not apologize for missing specific items; simply present the most luxurious alternatives available.
    5. If a user likes an item, mention the SKU and ask if they want to order it.
    6. If they say 'yes', 'buy', or 'I want that', use 'start_checkout' immediately.""",
    tools=[search_catalog_tool, checkout_tool]
)

if __name__ == "__main__":
    import sys
    # Your robust serve logic remains here...
    try:
        from google.adk import serve
        print("Starting agent server on http://localhost:8000")
        serve(root_agent, port=8000)
    except ImportError:
        # (Rest of your import logic)
        pass