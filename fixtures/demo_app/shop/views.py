import pytz
from django.http import JsonResponse
from django.utils.encoding import force_text

from .models import Product


def product_list(request):
    tz = pytz.timezone("Europe/Berlin")
    rows = [{"name": force_text(p.name)} for p in Product.objects.all()]
    if request.is_ajax():
        return JsonResponse({"rows": rows, "tz": str(tz)})
    return JsonResponse({"rows": rows})
