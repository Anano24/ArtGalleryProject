from src.extentions import db
from src.models.base import BaseModel



class GalleryItem(BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    img = db.Column(db.String)

    