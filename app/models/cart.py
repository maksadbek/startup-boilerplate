class CartItem:
    item: int
    count: int


class Cart:
    user_id: int
    anonymous_user_id: str
    items: [CartItem]
    checked_out: bool
    created_at: int
    updated_at: int
