from src.extentions import db
from src.models.base import BaseModel



class Product(BaseModel):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    price = db.Column(db.Integer)
    description = db.Column(db.Text)

    # Define the relationship with the Image model
    images = db.relationship('Image', backref='product', lazy=True)


    def serialize(self):
        # Get image objects associated with the product
        images_data = [{'filename': image.filename} for image in self.images]

        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'description': self.description,
            'images': images_data
            
            # Add other attributes as needed
        }


class Image(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)

