# Task 01 - SSO (Oauth-client)

#### lib use for SSO:
- django-allauth: https://django-allauth.readthedocs.io/en/latest/index.html

#### command need to run:
```shell
python manage.py runserver
```

#### super user login django admin
url: http://127.0.0.1:8000/admin
acc: truongnv
pass: abc1234.

#### Google Oauth setting:
client_id: 891600359969-aa6vghjgqplbu9u5ssj70l7o1h61e64a.apps.googleusercontent.com
client_secret: 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

#### TEST:
Access to 127.0.0.1:8000 to test login/log out Google

# TASK 2 : build grpc API

#### Concept
- Build API for todo app
- Build GRPC connect inside HTTP call
- Need 2 service run in 2 process
```
python manage.py grpcrunserver --dev
```

and other process
```
python manage.py runserver
```


**NOTE**: if you getting error like below

`TypeError: requires_system_checks must be a list or tuple.`

comment following lines in /lib/python3.x/site-packages/django/core/management/base.py

```python
    if (
        not isinstance(self.requires_system_checks, (list, tuple))
        and self.requires_system_checks != ALL_CHECKS
    ):
        raise TypeError("requires_system_checks must be a list or tuple.")
```


#### REFERENCES: 
- git project: https://github.com/Pradeeparul2/Django-gRPC-React-Todo-app
- lib doc: https://djangogrpcframework.readthedocs.io/en/latest/index.html

# Task 3: build docker 
