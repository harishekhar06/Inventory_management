from flask import Flask, request, jsonify
from . import db
from .models import Product, Variant, SubVariant
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a new product with variants and sub-variants
@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.get_json()

    logger.info(f"Received data: {data}")

    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        product = Product(
            product_id=data['product_id'],
            product_code=data['product_code'],
            product_name=data['product_name']
        )
        db.session.add(product)
        db.session.commit()

        for variant_data in data.get('variants', []):
            variant = Variant(
                product_id=product.id,
                name=variant_data['name']
            )
            db.session.add(variant)
            db.session.commit()

            for sub_variant_data in variant_data.get('subVariants', []):
                sub_variant = SubVariant(
                    variant_id=variant.id,
                    name=sub_variant_data['name'],
                    stock=float(sub_variant_data['stock'])
                )
                db.session.add(sub_variant)
            db.session.commit()

        logger.info("Product, variants, and sub-variants added successfully!")
        return jsonify({"message": "Product added successfully!"}), 201
    
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error adding product: {str(e)}")
        return jsonify({"error": f"Error adding product: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
