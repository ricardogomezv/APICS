from rest_framework import routers, serializers, viewsets

from Login.models import Example2

class Example2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Example2
        fieldsn = ('__all__')