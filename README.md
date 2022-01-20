# stockTracker

This project is created by Patika/Plentific Django Bootcamp participators as a follow-up project.

### Generate SECRET_KEY
There are two ways to create SECRET_KEY. The universal one is:
````shell
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
````

and if you've already installed the packages inside the ``requirements.txt``, then you have ``django-extensions`` installed. Then:

````shell
python .\manage.py generate_secret_key
````