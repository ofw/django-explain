# Django-Explain - a helper to get EXPLAIN or EXPLAIN ANALYZE output for django queryset.

## Installation
```sh
pip install django-queryset
```

## Example

```py
from django.contrib.auth.models import User
from django_explain import explain

explain_result = explain(User.objects.filter(pk=123))
explain_result.pretty_print()

# SELECT "auth_user"."id",
#        "auth_user"."password",
#        "auth_user"."last_login",
#        "auth_user"."is_superuser",
#        "auth_user"."username",
#        "auth_user"."first_name",
#        "auth_user"."last_name",
#        "auth_user"."email",
#        "auth_user"."is_staff",
#        "auth_user"."is_active",
#        "auth_user"."date_joined",
#        "auth_user"."has_orders"
# FROM "auth_user"
# WHERE "auth_user"."id" = 1
#
# Index Scan using auth_user_pkey on auth_user  (cost=0.43..8.45 rows=1 width=1070) (actual time=0.039..0.039 rows=0 loops=1)
#   Index Cond: (id = 1)
# Planning time: 1.203 ms
# Execution time: 0.106 ms

result.get_depesz_url()
# https://explain.depesz.com/s/Tym
```
