import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from women.models import Women


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        # fields = ('title', 'content', 'cat')
        fields = '__all__'

# class WomenSerializer(serializers.ModelSerializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()

# python manage.py shell
# from women.serializers import encode
# encode()


# Кодирование даннных в json
# def encode():
#     model = WomenModel('Pamela Anderson', 'Content: Walking')
#     model_sr = WomenSerializer(model)
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# python manage.py shell
# from women.serializers import encode
# decode()


# Декодирование данных из json в словарь
# def decode():
#     stream = io.BytesIO(b'{"title": "Pamela Anderson", "content": "Content Walking"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)


# class WomenSerializer(serializers.Serializer):
#     class Meta:
#         model = Women
#         fields = ('title', 'cat_id')
