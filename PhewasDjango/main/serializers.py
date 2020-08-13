from rest_framework import serializers
from .models import PheWasModel


# class PhewasSerializer(serializers.Serializer):
#     lab_name = serializers.CharField(max_length=100)
#     analysis_type = serializers.CharField(max_length=100)
#     char = serializers.CharField(max_length=20)
#     pos = serializers.CharField(max_length=200)
#     marker_name = serializers.CharField(max_length=200)
#     rsid = serializers.CharField(max_length=200)
#     ref = serializers.CharField(max_length=50)
#     alt = serializers.CharField(max_length=50)
#     effect = serializers.CharField(max_length=200)
#     analysis_efect = serializers.CharField(max_length=200)
#     var = serializers.CharField(max_length=200)
#     direction = serializers.CharField(max_length=2)
#     std_err = serializers.CharField(max_length=200)
#     gene = serializers.CharField(max_length=200)
#     log_p = serializers.CharField(max_length=200)
#     p = serializers.CharField(max_length=200)



class PhewasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PheWasModel
        fields = ['lab_name','analysis_type','char','pos','marker_name','rsid','ref','alt','effect', 'analysis_efect', 'var','direction', 'std_err', 'gene', 'log_p', 'p']