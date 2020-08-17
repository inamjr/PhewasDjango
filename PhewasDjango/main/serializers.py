from rest_framework import serializers
from .models import PheWasModel,PheWasModel_2


class PhewasSerializer(serializers.ModelSerializer):
# This is for mysqlite
    class Meta:
        model = PheWasModel
        fields = ['lab_name','analysis_type','char','pos','marker_name','rsid','ref','alt','effect', 'analysis_efect', 'var','direction', 'std_err', 'gene', 'log_p', 'p']


# This is for MYSQL database on amazone
class PhewasSerializer2(serializers.ModelSerializer):
     
    class Meta:
        model = PheWasModel_2
        fields = ['lab_name','analysis_type','charr','pos','marker_name','rsid','reff','altt','effect', 'analysis_effect', 'varr','direction', 'std_err', 'gene', 'log_p', 'p']
