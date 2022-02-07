from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

class BaseSerializer(FlexFieldsModelSerializer):
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        validated_data['updated_by'] = self.context['request'].user
        validated_data['published'] = True
        return super(BaseSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        validated_data['updated_by'] = self.context['request'].user
        return super(BaseSerializer, self).update(instance, validated_data)