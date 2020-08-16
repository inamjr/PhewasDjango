## Setting Up an Admin 

To add an admin to the app ```admin.py``` .
```python
python manage.py createsuperuser
```

## Service to Get the model(entity) to a json

Add ```serializers.py``` before sending data to the client we need to serialize the data to JSON.
Documentation
[Rest_Framework](https://www.django-rest-framework.org/)

There are different types of serializers implementation
here we use a model serializer.

```python

from .models import PheWasModel # <- add the models

# create a class of the model
class PhewasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PheWasModel
        fields = ['lab_name','analysis_type','char','pos','marker_name','rsid','ref','alt','effect', 'analysis_efect', 'var','direction', 'std_err', 'gene', 'log_p', 'p']
```

## Connecting the the urls between apps  

In the ```urls.py``` add the following 

```python
from .views import PheWas_List # <- import the models

# add a url to display json, html .. etc

urlpatterns = [
    path("phewas/", PheWas_List), 
]
```

## Display 
In the  ```views.py```  file you get the link to what gets shown by the url

In this app we only display information so we only need a GET 

```python
from django.http import HttpResponse , JsonResponse   # <- added
from rest_framework.parsers import JSONParser  # <- added
from .models import PheWasModel    # <- added
from .serializers import PhewasSerializer # <- added

# Create your views here.

def PheWas_List(request):
    if request.method =='GET':
        phewas = PheWasModel.objects.all()
        serializer = PhewasSerializer(phewas,many=True)
        return JsonResponse(serializer.data, safe=False)
```

