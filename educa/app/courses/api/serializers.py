from rest_framework.serializers import RelatedField, ModelSerializer
from ..models import Subject, Course, Module, Content

class ItemRelatedField(RelatedField):
    def to_representation(self, value):
        return value.render()

class ContentSerializer(ModelSerializer):
    item = ItemRelatedField(read_only=True)
    class Meta:
        model = Content
        fields = ('order', 'item')

class ModuleSerializer(ModelSerializer):
    class Meta:
        model = Module
        fields = ('order', 'title', 'description')


class CourseSerializer(ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ('id', 'subject', 'title', 'slug', 'overview', 'created', 'owner', 'modules')

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'title', 'slug')


class ModuleWithContentsSerializer(ModelSerializer):
    contents = ContentSerializer(many=True)
    class Meta:
        model = Module
        fields = ('order', 'title', 'description', 'contents')

class CourseWithContentsSerializer(CourseSerializer):
    modules = ModuleWithContentsSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'subject', 'title', 'slug',
                  'overview', 'created', 'owner', 'modules')
