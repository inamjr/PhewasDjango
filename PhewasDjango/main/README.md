## Setting Up an Admin 

To add an admin to the app ```admin.py``` .
```python
python manage.py createsuperuser
```

## Service to Get the model(entity) to a json

Add ```serializers.py``` before sending data to the client we need to serialize the data to JSON.
Documentation
[Rest_Framework](https://www.django-rest-framework.org/)

Code Snipit
```python

from .models import PheWasModel # <- add the models

# create a class of the model
class PhewasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PheWasModel
        fields = ['lab_name','analysis_type','char','pos','marker_name','rsid','ref','alt','effect', 'analysis_efect', 'var','direction', 'std_err', 'gene', 'log_p', 'p']
```

## Connecting the the urls between apps  

```python
from .views import PheWas_List # <- import the models

# add a url to display json, html .. etc

urlpatterns = [
    path("phewas/", PheWas_List), 
]
```
