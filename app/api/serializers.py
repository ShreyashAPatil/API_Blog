from app.models import blog
from rest_framework import serializers


class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = ['id', 'title', 'content', 'date', 'image']


