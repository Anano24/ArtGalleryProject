from src.extentions import db
from src.models.base import BaseModel



class Product(BaseModel):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    price = db.Column(db.Integer)
    img = db.Column(db.String)

