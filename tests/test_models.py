import pytest
from pydantic import ValidationError
from src.models.item import GTLItem

def test_valid_gtl_item():
    """Testa se um item válido do GTL é criado corretamente."""
    item_data = {
        "item_name": "Rare Candy",
        "category": "Medicine",
        "price": 10500,
        "quantity": 10
    }
    item = GTLItem(**item_data)
    assert item.item_name == "Rare Candy"
    assert item.price == 10500
    assert item.quantity == 10

def test_invalid_gtl_item_price():
    """Testa se o Pydantic rejeita um preço negativo ou zero."""
    with pytest.raises(ValidationError):
        GTLItem(
            item_name="Poke Ball",
            category="Items",
            price=-50,
            quantity=1
        )