from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

# Simple product database
PRODUCTS = [
    {"name": "Signature Piqué Polo", "sku": "LUXE-POLO-001", "price": 95, "description": "Breathable cotton piqué.", "image_url": "https://dtcralphlauren.scene7.com/is/image/PoloGSI/s7-1266705_alternate10?$rl_4x5_pdp$"},
    {"name": "Italian Wool Suit", "sku": "LUXE-SUIT-99", "price": 1200, "description": "Sharp charcoal wool.", "image_url": "https://dtcralphlauren.scene7.com/is/image/PoloGSI/s7-1339429_alternate10?$rl_4x5_pdp$"},
    {"name": "Silk Midi Dress", "sku": "LUXE-DRESS-05", "price": 450, "description": "Elegant emerald silk.", "image_url": "https://dtcralphlauren.scene7.com/is/image/PoloGSI/s7-AI253979849001_alternate10?$rl_4x5_pdp$"},
    {"name": "Cashmere V-Neck", "sku": "LUXE-CASH-10", "price": 300, "description": "Ultra-soft Mongolian cashmere.", "image_url": "https://dtcralphlauren.scene7.com/is/image/PoloGSI/s7-1470465_alternate10?$rl_4x5_pdp$"}
]

class SessionRequest(BaseModel):
    sku: str

@app.get("/products")
def get_products():
    return PRODUCTS

@app.post("/sessions")
def create_session(request: SessionRequest):
    # This is what triggers when the agent 'starts a purchase'
    print(f"[INFO] Creating shopping session for SKU: {request.sku}")
    return {"session_id": "sess_12345", "status": "active", "sku": request.sku}

@app.get("/")
def root():
    return {"message": "LuxeLife Server Online"}

if __name__ == "__main__":
    import uvicorn
    # This starts the server on port 8182
    uvicorn.run(app, host="0.0.0.0", port=8182)