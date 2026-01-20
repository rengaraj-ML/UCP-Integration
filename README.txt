================================================================================
                    LUXELIFE LUXURY BOUTIQUE AGENT PROJECT
                           Comprehensive Documentation
================================================================================

TABLE OF CONTENTS
-----------------
1. Project Overview
2. Project Architecture
3. File Structure
4. Prerequisites & Installation
5. Setup Instructions
6. Running the Application
7. API Documentation
8. Agent Configuration
9. Agent Tools Documentation
10. Product Catalog
11. Usage Examples
12. Troubleshooting
13. Development Notes

================================================================================
1. PROJECT OVERVIEW
================================================================================

Project Name: LuxeLife Luxury Boutique Agent
Purpose: An AI-powered luxury fashion shopping assistant built with Google ADK
         that provides personalized style advice and facilitates purchases.

Technology Stack:
- Google ADK (Agent Development Kit) - For building the conversational agent
- FastAPI - RESTful API backend for product catalog and session management
- Python 3.9-3.12 - Programming language
- Uvicorn - ASGI server for FastAPI
- Requests - HTTP library for API calls

High-Level Description:
This project implements an intelligent shopping assistant named "luxury_shopper"
that helps customers discover and purchase luxury fashion items. The agent uses
Google's Gemini 2.5 Flash model to provide personalized fashion advice and can
search through a product catalog, display items in an elegant tile gallery format,
and initiate checkout sessions.

Key Features:
- Natural language fashion advice and recommendations
- Product catalog search and filtering
- Visual product display with images, prices, and descriptions
- Seamless checkout initiation
- Integration with FastAPI backend for product management

================================================================================
2. PROJECT ARCHITECTURE
================================================================================

The project follows a two-server architecture:

┌─────────────────────────────────────────────────────────────────┐
│                    CLIENT (Web Browser)                         │
│              http://localhost:8000 (ADK Web UI)                  │
└────────────────────────────┬──────────────────────────────────┘
                             │
                             │ HTTP Requests
                             │
┌────────────────────────────▼──────────────────────────────────┐
│              GOOGLE ADK AGENT (luxury_shopper)                │
│  - Model: gemini-2.5-flash                                    │
│  - Port: 8000 (via adk web command)                           │
│  - Tools: search_catalog_tool, checkout_tool                  │
└────────────────────────────┬──────────────────────────────────┘
                             │
                             │ HTTP API Calls
                             │
┌────────────────────────────▼──────────────────────────────────┐
│              FASTAPI BACKEND SERVER                           │
│  - Port: 8182                                                │
│  - Endpoints: /products, /sessions, /                         │
│  - Product Catalog Storage                                   │
└───────────────────────────────────────────────────────────────┘

Component Breakdown:

1. Google ADK Agent (luxury_shopper)
   - Location: luxury_boutique/agent.py
   - Purpose: Main conversational AI agent
   - Responsibilities:
     * Process user queries about fashion and style
     * Search product catalog using search_catalog tool
     * Display products in HTML tile gallery format
     * Initiate checkout using start_checkout tool

2. FastAPI Backend Server
   - Location: luxury_boutique/main.py
   - Purpose: Product catalog and session management API
   - Responsibilities:
     * Serve product catalog data
     * Handle product search requests
     * Create shopping sessions for checkout

3. Agent Tools
   - search_catalog_tool: Searches and filters products based on query
   - checkout_tool: Initiates purchase session for a specific SKU

4. Product Catalog
   - In-memory database stored in main.py
   - Contains product information: name, SKU, price, description, image_url

Data Flow:
1. User asks question in ADK Web UI
2. Agent processes query and determines if catalog search is needed
3. Agent calls search_catalog tool
4. Tool makes HTTP GET request to FastAPI /products endpoint
5. FastAPI returns product list
6. Tool filters products based on query
7. Agent formats products in HTML tile gallery
8. User selects item to purchase
9. Agent calls start_checkout tool with SKU
10. Tool makes HTTP POST request to FastAPI /sessions endpoint
11. FastAPI creates session and returns session details

================================================================================
3. FILE STRUCTURE
================================================================================

UCP-Integration/
│
└── luxury_boutique/
    ├── __init__.py          # Package initialization, exports root_agent
    ├── agent.py             # Agent definition, tools, and configuration
    ├── main.py              # FastAPI server with product catalog
    └── index.html           # Product showcase page (static HTML)

File Descriptions:

__init__.py
- Purpose: Makes luxury_boutique a Python package
- Content: Imports and exports root_agent from agent.py
- Critical for: ADK web agent discovery

agent.py
- Purpose: Defines the luxury_shopper agent and its tools
- Key Components:
  * search_catalog() function - Searches product catalog
  * start_checkout() function - Initiates purchase session
  * search_catalog_tool - FunctionTool wrapper for search_catalog
  * checkout_tool - FunctionTool wrapper for start_checkout
  * root_agent - Main Agent instance with instructions and tools
- Size: ~70 lines

main.py
- Purpose: FastAPI backend server for product catalog
- Key Components:
  * PRODUCTS list - In-memory product database
  * /products endpoint - Returns all products
  * /sessions endpoint - Creates shopping sessions
  * / endpoint - Health check
- Size: ~34 lines

index.html
- Purpose: Static HTML page showcasing products
- Contains: Schema.org structured data for products
- Note: Currently not integrated with the agent system

================================================================================
4. PREREQUISITES & INSTALLATION
================================================================================

Prerequisites:
- Python 3.9, 3.10, 3.11, or 3.12 (Python 3.13+ may not be fully supported)
- pip package manager
- Virtual environment (recommended)

Required Python Packages:
- google-adk - Google Agent Development Kit
- fastapi - Modern web framework for building APIs
- uvicorn - ASGI server implementation
- requests - HTTP library for making API calls
- pydantic - Data validation using Python type annotations

Installation Steps:

1. Create a virtual environment (recommended):
   python -m venv .venv

2. Activate the virtual environment:
   Windows: .venv\Scripts\activate
   Linux/Mac: source .venv/bin/activate

3. Install required packages:
   pip install google-adk fastapi uvicorn requests pydantic

4. Verify installation:
   python -c "import google.adk; import fastapi; print('All packages installed successfully')"

================================================================================
5. SETUP INSTRUCTIONS
================================================================================

Step-by-Step Setup:

1. Clone or navigate to the project directory:
   cd C:\Users\renga\OneDrive\Documents\Projects\UCP-Integration

2. Create and activate virtual environment (if not already done):
   python -m venv .venv
   .venv\Scripts\activate

3. Install dependencies:
   pip install google-adk fastapi uvicorn requests pydantic

4. Verify the project structure:
   - Ensure luxury_boutique/ directory exists
   - Check that __init__.py, agent.py, and main.py are present

5. Test agent import (optional):
   python -c "from luxury_boutique import root_agent; print(root_agent.name)"
   Expected output: luxury_shopper

6. Verify FastAPI server can start (optional):
   cd luxury_boutique
   python main.py
   (Press Ctrl+C to stop after verifying it starts)

Environment Configuration:
- No environment variables required for basic operation
- Ports used: 8000 (ADK web), 8182 (FastAPI)
- Ensure these ports are not in use by other applications

================================================================================
6. RUNNING THE APPLICATION
================================================================================

The application requires TWO servers running simultaneously:

TERMINAL 1: FastAPI Backend Server
---------------------------------
1. Navigate to the luxury_boutique directory:
   cd luxury_boutique

2. Start the FastAPI server:
   python main.py

3. Expected output:
   INFO:     Started server process
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
   INFO:     Uvicorn running on http://0.0.0.0:8182

4. Keep this terminal open and running

TERMINAL 2: ADK Web Interface
------------------------------
1. Navigate to the project root directory:
   cd C:\Users\renga\OneDrive\Documents\Projects\UCP-Integration

2. Start the ADK web server:
   adk web luxury_boutique

   IMPORTANT: Use "luxury_boutique" not "." as the argument

3. Expected output:
   INFO:     Application startup complete.
   INFO:     Uvicorn running on http://127.0.0.1:8000

4. Keep this terminal open and running

BROWSER ACCESS
--------------
1. Open your web browser
2. Navigate to: http://localhost:8000
   (or http://127.0.0.1:8000)
3. You should see the ADK web interface
4. Select "luxury_shopper" from the agent dropdown
5. Start chatting with the agent!

VERIFICATION CHECKLIST
-----------------------
✓ FastAPI server running on port 8182
✓ ADK web server running on port 8000
✓ Browser can access http://localhost:8000
✓ Agent "luxury_shopper" appears in dropdown
✓ Can send messages to the agent

STOPPING THE SERVERS
--------------------
- Press Ctrl+C in each terminal to stop the respective servers
- Always stop ADK web server first, then FastAPI server

================================================================================
7. API DOCUMENTATION
================================================================================

FastAPI Backend API Endpoints
------------------------------

Base URL: http://localhost:8182

1. GET /products
   Description: Returns the complete product catalog
   
   Request:
   - Method: GET
   - URL: http://localhost:8182/products
   - Headers: None required
   - Body: None
   
   Response:
   - Status Code: 200 OK
   - Content-Type: application/json
   - Body: Array of product objects
   
   Example Response:
   [
     {
       "name": "Signature Piqué Polo",
       "sku": "LUXE-POLO-001",
       "price": 95,
       "description": "Breathable cotton piqué.",
       "image_url": "https://dtcralphlauren.scene7.com/is/image/..."
     },
     ...
   ]
   
   Example using curl:
   curl http://localhost:8182/products

2. POST /sessions
   Description: Creates a new shopping session for a product purchase
   
   Request:
   - Method: POST
   - URL: http://localhost:8182/sessions
   - Headers: Content-Type: application/json
   - Body: JSON object with "sku" field
   
   Request Body Schema:
   {
     "sku": "string"  // Product SKU (e.g., "LUXE-POLO-001")
   }
   
   Response:
   - Status Code: 200 OK
   - Content-Type: application/json
   - Body: Session object
   
   Example Request:
   {
     "sku": "LUXE-POLO-001"
   }
   
   Example Response:
   {
     "session_id": "sess_12345",
     "status": "active",
     "sku": "LUXE-POLO-001"
   }
   
   Example using curl:
   curl -X POST http://localhost:8182/sessions \
        -H "Content-Type: application/json" \
        -d '{"sku": "LUXE-POLO-001"}'

3. GET /
   Description: Health check endpoint
   
   Request:
   - Method: GET
   - URL: http://localhost:8182/
   - Headers: None required
   - Body: None
   
   Response:
   - Status Code: 200 OK
   - Content-Type: application/json
   - Body: Status message
   
   Example Response:
   {
     "message": "LuxeLife Server Online"
   }
   
   Example using curl:
   curl http://localhost:8182/

Error Handling:
- If FastAPI server is not running, agent tools will return error messages
- Connection timeout is set to 5 seconds
- Errors are caught and returned in tool response format

================================================================================
8. AGENT CONFIGURATION
================================================================================

Agent Name: luxury_shopper
Model: gemini-2.5-flash
Location: luxury_boutique/agent.py

Agent Instructions:
The agent is configured as an "elite style consultant for LuxeLife" with the
following behavior:

DISPLAY RULES:
- Products MUST be displayed in a side-by-side tile gallery using HTML
- Uses specific HTML structure with flexbox layout
- Each product tile shows:
  * Product image (120px height, object-fit: cover)
  * Product name (h4, 14px font)
  * Price and SKU (12px font, gray color)
- Tiles are 180px wide with 10px gap between them
- Border radius: 8px for container, 4px for images

GUIDELINES:
1. When user asks for advice, ALWAYS use 'search_catalog' tool
2. Show ALL relevant elegant options from collection (aim for variety)
3. Display at least 3 items in tile gallery for every recommendation
4. Don't apologize for missing specific items; present luxurious alternatives
5. If user likes an item, mention the SKU and ask if they want to order
6. If user says 'yes', 'buy', or 'I want that', use 'start_checkout' immediately

Agent Tools:
- search_catalog_tool: FunctionTool wrapping search_catalog() function
- checkout_tool: FunctionTool wrapping start_checkout() function
  * require_confirmation=False (bypasses manual approval button)

Agent Behavior:
- Proactive: Always searches catalog when fashion advice is requested
- Visual: Displays products in elegant HTML tile gallery
- Helpful: Shows multiple options even for specific requests
- Efficient: Automatically initiates checkout without confirmation prompt

================================================================================
9. AGENT TOOLS DOCUMENTATION
================================================================================

Tool 1: search_catalog
-----------------------
Function: search_catalog(query: str) -> list
Tool Wrapper: search_catalog_tool = FunctionTool(search_catalog)

Purpose:
Searches the luxury boutique catalog for fashion advice and items based on
a query string.

Parameters:
- query (str): Search query string (e.g., "dress", "suit", "party outfit")

Functionality:
1. Makes HTTP GET request to http://localhost:8182/products
2. Retrieves all products from FastAPI backend
3. Filters products where query appears in name or description (case-insensitive)
4. Returns matching products, or all products if no matches found
5. Returns error message if connection fails

Return Value:
- Success: List of product dictionaries matching the query
- No matches: List of all products (fallback)
- Error: List containing single dict with "error" key and message

Example Usage by Agent:
User: "What should I wear to a party?"
Agent calls: search_catalog("party")
Returns: [{"name": "Silk Midi Dress", "sku": "LUXE-DRESS-05", ...}, ...]

Product Dictionary Structure:
{
  "name": "Product Name",
  "sku": "LUXE-XXXX-XXX",
  "price": 123,
  "description": "Product description",
  "image_url": "https://..."
}

Tool 2: start_checkout
-----------------------
Function: start_checkout(sku: str) -> dict
Tool Wrapper: checkout_tool = FunctionTool(start_checkout, require_confirmation=False)

Purpose:
Initiates a purchase session for a specific product by SKU.

Parameters:
- sku (str): Product SKU identifier (e.g., "LUXE-POLO-001")

Functionality:
1. Makes HTTP POST request to http://localhost:8182/sessions
2. Sends JSON body with "sku" field
3. FastAPI creates shopping session
4. Returns session details including session_id and status

Return Value:
- Success: Dictionary with session information
  {
    "session_id": "sess_12345",
    "status": "active",
    "sku": "LUXE-POLO-001"
  }
- Error: Dictionary with "error" key and message

Example Usage by Agent:
User: "I want to buy the polo shirt"
Agent calls: start_checkout("LUXE-POLO-001")
Returns: {"session_id": "sess_12345", "status": "active", "sku": "LUXE-POLO-001"}

Special Configuration:
- require_confirmation=False: Tool executes immediately without user approval
- This allows seamless checkout flow without manual confirmation clicks

Error Handling:
Both tools implement try-except blocks with 5-second timeouts:
- Connection errors are caught and returned as error dictionaries
- Prevents agent from crashing if backend is unavailable
- Error messages are user-friendly and informative

================================================================================
10. PRODUCT CATALOG
================================================================================

Current Products:
-----------------
The product catalog is stored in luxury_boutique/main.py as the PRODUCTS list.

1. Signature Piqué Polo
   SKU: LUXE-POLO-001
   Price: $95
   Description: Breathable cotton piqué.
   Image: https://dtcralphlauren.scene7.com/is/image/PoloGSI/s7-1266705_alternate10?$rl_4x5_pdp$

2. Italian Wool Suit
   SKU: LUXE-SUIT-99
   Price: $1,200
   Description: Sharp charcoal wool.
   Image: https://dtcralphlauren.scene7.com/is/image/PoloGSI/s7-1339429_alternate10?$rl_4x5_pdp$

3. Silk Midi Dress
   SKU: LUXE-DRESS-05
   Price: $450
   Description: Elegant emerald silk.
   Image: https://dtcralphlauren.scene7.com/is/image/PoloGSI/s7-AI253979849001_alternate10?$rl_4x5_pdp$

4. Cashmere V-Neck
   SKU: LUXE-CASH-10
   Price: $300
   Description: Ultra-soft Mongolian cashmere.
   Image: https://dtcralphlauren.scene7.com/is/image/PoloGSI/s7-1470465_alternate10?$rl_4x5_pdp$

Product Schema:
--------------
Each product is a dictionary with the following structure:

{
  "name": str,           # Product display name
  "sku": str,            # Stock Keeping Unit (unique identifier)
  "price": int,          # Price in USD (integer, no cents)
  "description": str,    # Brief product description
  "image_url": str       # URL to product image
}

Adding New Products:
--------------------
To add a new product to the catalog:

1. Open luxury_boutique/main.py
2. Locate the PRODUCTS list (around line 7)
3. Add a new dictionary entry following the schema:

   PRODUCTS = [
       # ... existing products ...
       {
           "name": "New Product Name",
           "sku": "LUXE-XXXX-XXX",  # Use consistent SKU format
           "price": 999,
           "description": "Product description here.",
           "image_url": "https://example.com/image.jpg"
       }
   ]

4. Save the file
5. Restart the FastAPI server (Ctrl+C and run python main.py again)
6. The new product will be immediately available to the agent

Modifying Products:
------------------
To modify an existing product:

1. Open luxury_boutique/main.py
2. Find the product in the PRODUCTS list by SKU or name
3. Update the desired fields (name, price, description, image_url)
4. Save and restart FastAPI server

Note: Changes take effect immediately after server restart. No agent restart needed.

================================================================================
11. USAGE EXAMPLES
================================================================================

Example Conversation 1: General Fashion Advice
------------------------------------------------
User: "What should I wear to a formal dinner party?"

Agent Response:
[Agent uses search_catalog tool with query "dinner party"]
[Displays products in HTML tile gallery]

"I have some elegant options perfect for a formal dinner party. Here are our
luxurious selections:

[HTML tile gallery showing: Italian Wool Suit, Silk Midi Dress, etc.]

The Italian Wool Suit (SKU: LUXE-SUIT-99) is perfect for formal occasions,
or the Silk Midi Dress (SKU: LUXE-DRESS-05) offers a sophisticated alternative.
Would you like to purchase one of these?"

Example Conversation 2: Specific Product Request
--------------------------------------------------
User: "Do you have any polo shirts?"

Agent Response:
[Agent uses search_catalog tool with query "polo"]
[Displays matching products]

"Yes! We have the Signature Piqué Polo (SKU: LUXE-POLO-001) available for $95.
It's made from breathable cotton piqué, perfect for casual outings.

[HTML tile gallery showing the polo shirt]

Would you like to order it?"

User: "Yes, I'll take it."

Agent Response:
[Agent uses start_checkout tool with SKU "LUXE-POLO-001"]
[FastAPI creates session]

"Perfect! I've started your purchase session for the Signature Piqué Polo.
Session ID: sess_12345. Your order is being processed!"

Example Conversation 3: Multiple Options
-----------------------------------------
User: "I need something elegant for a wedding."

Agent Response:
[Agent uses search_catalog tool]
[Shows at least 3 elegant options]

"For a wedding, I recommend these elegant pieces from our collection:

[HTML tile gallery showing: Italian Wool Suit, Silk Midi Dress, Cashmere V-Neck]

Each offers sophisticated style perfect for such an occasion. The Italian Wool
Suit (SKU: LUXE-SUIT-99) is particularly striking for formal events. Which
would you prefer?"

Best Practices for Users:
-------------------------
- Ask open-ended questions for best recommendations
- Be specific about occasion (party, wedding, casual, etc.)
- Mention style preferences if you have them
- Use natural language - the agent understands context
- Say "yes", "buy", or "I want that" to initiate checkout

================================================================================
12. TROUBLESHOOTING
================================================================================

Issue 1: Agent Not Appearing in Dropdown
-----------------------------------------
Symptoms:
- ADK web interface loads but dropdown is empty
- No agents listed in /list-apps endpoint

Solutions:
1. Verify you're running: adk web luxury_boutique (not "adk web .")
2. Check that __init__.py exists and contains: from .agent import root_agent
3. Verify agent.py defines root_agent variable
4. Test import: python -c "from luxury_boutique import root_agent; print(root_agent.name)"
5. Ensure you're in the project root directory when running adk web
6. Check for Python syntax errors in agent.py or __init__.py

Issue 2: Port Already in Use
-----------------------------
Symptoms:
- Error: "Address already in use"
- Server fails to start

Solutions:
1. Find process using port 8000: netstat -ano | findstr :8000 (Windows)
2. Find process using port 8182: netstat -ano | findstr :8182 (Windows)
3. Kill process: taskkill /PID <process_id> /F (Windows)
4. Or change ports in code:
   - ADK web: Use different port in adk web command (if supported)
   - FastAPI: Change port in main.py uvicorn.run() call

Issue 3: ModuleNotFoundError: No module named 'google.adk'
----------------------------------------------------------
Symptoms:
- Import error when running agent.py
- Error when starting adk web

Solutions:
1. Verify virtual environment is activated
2. Install google-adk: pip install google-adk
3. Check Python version (must be 3.9-3.12)
4. Reinstall: pip install --upgrade google-adk
5. Verify installation: python -c "import google.adk; print('OK')"

Issue 4: Agent Can't Connect to FastAPI Server
-----------------------------------------------
Symptoms:
- Agent says "Could not connect to catalog"
- Tool returns error messages
- Products not loading

Solutions:
1. Verify FastAPI server is running (check Terminal 1)
2. Test API directly: curl http://localhost:8182/products
3. Check port number matches (should be 8182)
4. Verify no firewall blocking localhost connections
5. Check FastAPI server logs for errors
6. Ensure both servers are running simultaneously

Issue 5: Tools Not Working
---------------------------
Symptoms:
- Agent doesn't search catalog when asked
- Checkout doesn't initiate
- Agent makes excuses about not having access

Solutions:
1. Verify tools are wrapped in FunctionTool:
   - search_catalog_tool = FunctionTool(search_catalog)
   - checkout_tool = FunctionTool(start_checkout, require_confirmation=False)
2. Check tools are included in Agent definition:
   - tools=[search_catalog_tool, checkout_tool]
3. Verify tool function signatures match expected format
4. Check for syntax errors in agent.py

Issue 6: Products Not Displaying Correctly
-------------------------------------------
Symptoms:
- Products show but formatting is wrong
- Images not loading
- HTML not rendering

Solutions:
1. Verify image_urls in PRODUCTS list are valid URLs
2. Check agent instructions include HTML display rules
3. Ensure products have all required fields (name, sku, price, description, image_url)
4. Test image URLs in browser to verify they're accessible

Issue 7: Checkout Not Working
------------------------------
Symptoms:
- Agent says checkout failed
- No session created
- Error messages in tool response

Solutions:
1. Verify FastAPI /sessions endpoint is working:
   curl -X POST http://localhost:8182/sessions -H "Content-Type: application/json" -d '{"sku":"LUXE-POLO-001"}'
2. Check SKU format matches exactly (case-sensitive)
3. Verify FastAPI server is running
4. Check FastAPI logs for POST request errors
5. Ensure SessionRequest model matches request format

General Debugging Tips:
-----------------------
1. Check both terminal outputs for error messages
2. Use browser developer tools (F12) to inspect network requests
3. Test API endpoints directly with curl or Postman
4. Verify Python version: python --version
5. Check all imports work: python -c "from luxury_boutique import root_agent"
6. Review agent.py for syntax errors
7. Ensure proper indentation in Python files
8. Check that all required packages are installed

Common Error Messages:
---------------------
- "Could not connect to catalog": FastAPI server not running
- "Checkout failed": /sessions endpoint error or invalid SKU
- "No module named 'google.adk'": Package not installed
- "Address already in use": Port conflict
- Empty dropdown: Agent not properly exported or wrong command used

================================================================================
13. DEVELOPMENT NOTES
================================================================================

Code Structure:
---------------
The project follows a clean separation of concerns:

1. Agent Logic (agent.py):
   - Contains all agent-specific code
   - Tool definitions and wrappers
   - Agent configuration and instructions
   - No business logic, only orchestration

2. Backend API (main.py):
   - Product data storage
   - RESTful API endpoints
   - Session management
   - No agent-specific code

3. Package Structure (__init__.py):
   - Minimal, only exports root_agent
   - Enables package import
   - Required for ADK web discovery

Key Design Decisions:
---------------------
1. Two-Server Architecture:
   - Separates agent UI from product API
   - Allows independent scaling
   - Enables API reuse by other clients

2. In-Memory Product Storage:
   - Simple for development/demo
   - Easy to modify
   - Can be replaced with database later

3. FunctionTool Wrapping:
   - Consistent tool interface
   - Enables tool configuration (require_confirmation)
   - Standard ADK pattern

4. HTML Display in Agent:
   - Rich visual presentation
   - Better user experience
   - Leverages agent's HTML rendering capability

5. Automatic Checkout:
   - require_confirmation=False for seamless flow
   - Better UX, fewer clicks
   - Can be changed if approval needed

Extension Points:
-----------------
1. Database Integration:
   - Replace PRODUCTS list with database queries
   - Add product persistence
   - Implement product management API

2. User Authentication:
   - Add user accounts
   - Track purchase history
   - Personalize recommendations

3. Payment Integration:
   - Connect /sessions endpoint to payment gateway
   - Process actual transactions
   - Handle payment confirmations

4. Inventory Management:
   - Add stock levels to products
   - Check availability before checkout
   - Handle out-of-stock scenarios

5. Enhanced Search:
   - Add filtering by price range
   - Category-based search
   - Sort options (price, name, etc.)

6. Product Recommendations:
   - ML-based recommendations
   - "Customers also bought" features
   - Style matching algorithms

7. Multi-Agent Support:
   - Add more agents for different purposes
   - Specialized agents (men's, women's, accessories)
   - Agent routing based on query type

8. Analytics:
   - Track popular products
   - Monitor agent performance
   - User behavior analytics

9. Error Recovery:
   - Retry logic for API calls
   - Fallback product suggestions
   - Graceful degradation

10. Testing:
    - Unit tests for tools
    - Integration tests for API
    - Agent conversation tests

Code Quality Notes:
-------------------
- All functions have docstrings
- Error handling in all tool functions
- Type hints used where appropriate
- Consistent code formatting
- Clear variable naming

Performance Considerations:
---------------------------
- Product list is small, in-memory is fine
- API calls have 5-second timeout
- No caching currently implemented
- Consider caching for production use

Security Considerations:
------------------------
- Currently no authentication
- API endpoints are open
- No input validation beyond Pydantic
- Add authentication for production
- Validate and sanitize all inputs
- Implement rate limiting

Future Improvements:
--------------------
- Add logging framework
- Implement proper error handling
- Add configuration file support
- Environment-based settings
- Docker containerization
- CI/CD pipeline
- Comprehensive test suite
- API documentation (OpenAPI/Swagger)
- Monitoring and observability

================================================================================
                              END OF DOCUMENTATION
================================================================================

For questions or issues, refer to the Troubleshooting section or consult the
Google ADK documentation: https://google.github.io/adk-docs/

Last Updated: January 2026
Project Version: 1.0
