from . import db
import uuid

class Product(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    product_id = db.Column(db.BigInteger, unique=True, nullable=False)
    product_code = db.Column(db.String(255), unique=True, nullable=False)
    product_name = db.Column(db.String(255), nullable=False)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_date = db.Column(db.DateTime, onupdate=db.func.current_timestamp())
    total_stock = db.Column(db.Float, default=0.0)

    # Relationship to Variant
    variants = db.relationship('Variant', backref='product', lazy=True)

    def __repr__(self):
        return f'<Product {self.product_name}>'

class Variant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(36), db.ForeignKey('product.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)

    # Relationship to SubVariant
    sub_variants = db.relationship('SubVariant', backref='variant', lazy=True)

    def __repr__(self):
        return f'<Variant {self.name}>'

class SubVariant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    variant_id = db.Column(db.Integer, db.ForeignKey('variant.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    stock = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<SubVariant {self.name}>'
