from rest_framework import serializers
from models import LANGUAGE_CHOICES, Snippet, STYLE_CHOICES


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """
#         create and return a new Snippet obj with given data
#         :param validated_data:
#         :return:
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, obj, validated_data):
#         """
#         update and return an existing obj with given data
#         :param obj:
#         :param validated_data:
#         :return:
#         """
#         obj.title = validated_data.get('title', obj.titel)
#         obj.code = validated_data.get('code', obj.code)
#         obj.linenos = validated_data.get('linenos', obj.linenos)
#         obj.language = validated_data.get('language', obj.language)
#         obj.style = validated_data.get('style', obj.style)
#         obj.save()
#         return obj


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')