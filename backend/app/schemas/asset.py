from pydantic import BaseModel, ConfigDict


class AssetBase(BaseModel):
    name: str
    asset_type: str
    ip_address: str | None = None
    criticality: int
    internet_exposed: bool
    owner: str | None = None


class AssetResponse(AssetBase):
    id: int

    model_config = ConfigDict(from_attributes=True)