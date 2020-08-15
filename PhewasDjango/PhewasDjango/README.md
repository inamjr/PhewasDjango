# Modified Files

In ```settings.py``` modify 

```java
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',   # <- add this
    'main.apps.MainConfig', # <- add this
]
```
Local Data Base

```java
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
In ```urls.py``` Add

```python
from django.contrib import admin
from django.urls import path,include  <-- # add include

# paths to find the various pages 
urlpatterns = [
# default 
    path('admin/', admin.site.urls),
    path('', include('main.urls')), # main is the name of your app 
]
```
