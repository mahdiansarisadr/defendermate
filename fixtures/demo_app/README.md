Synthetic Django 3.2 app used only by `urx scan` and `tests/test_scan.py`.
It is not a real project. Each planted usage maps to a documented 4.0–4.2 removal or behaviour change;
`shop/utils.py` deliberately avoids `django.utils.http.urlquote` so that path must not fire.
