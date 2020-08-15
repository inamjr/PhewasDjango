
To add an admin to the app ```admin.py``` .
```python
python manage.py createsuperuser
```

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
