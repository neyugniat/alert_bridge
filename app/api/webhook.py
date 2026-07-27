from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()

    print(f"Received webhook payload: {payload}")

    return {"status": "received"}