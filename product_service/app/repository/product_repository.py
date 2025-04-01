# Repositório de produtos 

from app import db
from app.domain.models.product import Product
from app.repository.base_repository import BaseRepository
from typing import List, Optional

class ProductRepository(BaseRepository):
    def get(self, id: int) -> Optional[Product]:
        return Product.query.get(id)

    def get_all(self) -> List[Product]:
        return Product.query.all()

    def create(self, product: Product) -> Product:
        db.session.add(product)
        db.session.commit()
        return product

    def update(self, id: int, product: Product) -> Optional[Product]:
        existing_product = self.get(id)
        if existing_product:
            for key, value in product.__dict__.items():
                if not key.startswith('_'):
                    setattr(existing_product, key, value)
            db.session.commit()
        return existing_product

    def delete(self, id: int) -> bool:
        product = self.get(id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return True
        return False 
