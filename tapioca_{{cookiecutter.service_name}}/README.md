# Tapioca {{ cookiecutter.service_name }}

## Installation
```
pip install tapioca-{{ cookiecutter.service_name}}
```

## Documentation
``` python
from tapioca_{{ cookiecutter.service_name}} import {{ cookiecutter.service_name}}

{% if cookiecutter.use_oauth_2 == 'y' %}
api = {{ cookiecutter.service_name}}(
	client_id='{your-client-id}', access_token='{any-valid-access-token}')
{% elif cookiecutter.use_oauth_1 == 'y' %}
api = {{ cookiecutter.service_name}}(
	api_key='{your-api-id}',
    api_secret='{your-api-secret}',
    access_token='{your-access-token}',
    access_token_secret='{your-access-token-secret}')
{% elif cookiecutter.use_basic_auth == 'y' %}
api = {{ cookiecutter.service_name}}(
	user='{your-user}', password='{your-password}')
{% else %}
api = {{ cookiecutter.service_name}}()
{% endif %}
```

No more documentation needed.

- Learn how Tapioca works [here](http://tapioca-wrapper.readthedocs.org/en/stable/quickstart.html)
- Explore this package using iPython
- Have fun!
