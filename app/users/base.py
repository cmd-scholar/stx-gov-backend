from sqlmodel import SQLModel, Field
from typing import Optional

from app.core.models import UUIDModel


class UserProfile(UUIDModel, SQLModel):
    username: str = Field(min_length=3, max_length=30)

class UserBase(UserProfile):
    decentralized_id: Optional[str] = Field(default=None)
    stx_address_testnet: Optional[str] = Field(default=None)
    stx_address_mainnet: Optional[str] = Field(default=None)
    btc_address_mainnet: Optional[str] = Field(default=None)
    btc_address_testnet: Optional[str] = Field(default=None)
    wallet_provider: Optional[str] = Field(default=None)
    public_key: Optional[str] = Field(default=None)
    gaia_hub_url: Optional[str] = Field(default=None)
