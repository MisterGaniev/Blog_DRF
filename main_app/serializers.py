from main_app.models import *
from rest_framework.serializers import ModelSerializer

class MaqolaSerial(ModelSerializer):
    class Meta:
        model = Maqola
        fields = '__all__'

class ImageSerial(ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'