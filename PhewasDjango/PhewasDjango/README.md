# Modified Files

In ```settings.py``` modify 

```javascript
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',   # <- add_this
    'main.apps.MainConfig', # <- add_this
]
```
