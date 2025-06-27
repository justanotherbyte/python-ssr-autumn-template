from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

if TYPE_CHECKING:
    from autumn.aio.client import AsyncClient

router = APIRouter()


CUSTOMER_ID = "user_123"


@router.route("/", methods=["GET", "POST"])
async def index(request: Request):
    autumn: AsyncClient = request.app.state.autumn

    if request.method.upper() == "POST":
        form_data = await request.form()
        chat_message = form_data.get("chat_message")

        if chat_message:
            await autumn.track(CUSTOMER_ID, feature_id="chat_messages", value=1)

    table = await autumn.customers.pricing_table(CUSTOMER_ID)
    customer = await autumn.customers.get(CUSTOMER_ID)

    context = {
        "list": table.list,
        "usage": int(customer.features["chat_messages"].usage),
        "balance": int(customer.features["chat_messages"].balance),
        "included_usage": int(customer.features["chat_messages"].included_usage),
        "customer_name": customer.name,
    }

    return request.app.state.templates.TemplateResponse(
        request=request, name="index.html", context=context
    )


@router.get("/checkout/{product_id}")
async def checkout(request: Request, product_id: str):
    autumn: AsyncClient = request.app.state.autumn

    attach = await autumn.attach(CUSTOMER_ID, product_id=product_id)
    print(attach.checkout_url)
    return RedirectResponse(attach.checkout_url or "/")
