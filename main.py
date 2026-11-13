from fastapi import FastAPI

from schemas import CouponCreateRequest

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/coupons")
def create_coupon(request: CouponCreateRequest):
    return request
