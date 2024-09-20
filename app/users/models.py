from sqlmodel import Relationship, SQLModel
from typing import List, Optional
from app.core.models import TimestampModel, UUIDModel
# from app.proposals.models import Proposal
from app.users.base import UserBase
from app.models.common import UserDaoLink

class User(UserBase, TimestampModel,UUIDModel,  table=True):
    __tablename__ = "users"
    daos: List["Dao"] = Relationship(back_populates="members", link_model=UserDaoLink)
    created_daos: List["Dao"] = Relationship(back_populates="creator", cascade_delete=True)
    created_proposals :List["Proposal"] = Relationship(back_populates="created_by", cascade_delete=True)

class UserRead(UserBase, UUIDModel):
    daos: List["DaoRead"] = []
    created_daos: List["DaoRead"] = []

class UserCreate(UserBase):
    pass

# class UserUpdate(SQLModel):
#     username: Optional[str] = None
#     decentralized_id: Optional[str] = Field(default=None)
#     stx_address_testnet: Optional[str] = Field(default=None)
#     stx_address_mainnet: Optional[str] = Field(default=None)
#     btc_address_mainnet: Optional[str] = Field(default=None)
#     btc_address_testnet: Optional[str] = Field(default=None)
#     wallet_provider: Optional[str] = Field(default=None)
#     public_key: Optional[str] = Field(default=None)
#     gaia_hub_url: Optional[str] = Field(default=None)
#