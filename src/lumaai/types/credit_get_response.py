# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["CreditGetResponse"]


class CreditGetResponse(BaseModel):
    credit_balance: float
    """Available credits balance in USD cents"""
