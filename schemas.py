from pydantic import BaseModel, ConfigDict, Field


class CouponCreateRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(min_length=1)
    total_quantity: int = Field(strict=True, ge=1)
