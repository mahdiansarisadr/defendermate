from urllib.parse import quote


def product_slug(name: str) -> str:
    return quote(name.lower().replace(" ", "-"))
