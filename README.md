# Django-Explain - a helper to get EXPLAIN or EXPLAIN ANALYZE output for django queryset.

## Installation
```sh
pip install django-queryset
```

## Example

```py
from django.contrib.auth.models import User
from django_explain import explain

response = requests.get("http://google.ru")
print(curlify.to_curl(response.request))
# curl -X GET -H 'Connection: keep-alive' -H 'Accept-Encoding: gzip, deflate' -H 'Accept: */*' -H 'User-Agent: python-requests/2.7.0 CPython/2.7.11 Darwin/15.6.0' -d '' 'http://www.google.ru/'
```
