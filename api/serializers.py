from rest_framework import serializers
from django.utils import timezone
from datetime import timedelta
from .models import Box
from . import helpers
from . import params

class BoxSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField()

    def get_creator(self, instance):
        return instance.creator.username

    class Meta:
        model = Box
        fields = ('id', 'length', 'breadth', 'height', 'area', 'volume', 'creator', 'updated_date')

    def __init__(self, *args, **kwargs):
        super(BoxSerializer, self).__init__(*args, **kwargs)
        if not kwargs['context']['request'].user.is_staff:
            self.fields.pop('creator')
            self.fields.pop('updated_date')

    def validate(self, data):
        length = data['length']
        breadth = data['breadth']
        height = data['height']

        boxes = Box.objects.all()

        area = helpers.get_area(length, breadth, height)
        total_area = 0.0
        for box in boxes:
            total_area += box.area
        if (total_area + area) / (boxes.count() + 1) > params.AVERAGE_AREA_ALLOWED:
            raise serializers.ValidationError("Average area of all added boxes cannot exceed {}!".format(params.AVERAGE_AREA_ALLOWED))

        current_user = self.context['request'].user
        current_boxes = boxes.filter(creator=current_user)
        volume = helpers.get_volume(length, breadth, height)
        total_volume = 0.0
        for box in current_boxes:
            total_volume += box.area
        if (total_volume + volume) / (current_boxes.count() + 1) > params.AVERAGE_VOLUME_ALLOWED_CURRENT:
            raise serializers.ValidationError("Average volume of all boxes added by the current user cannot exceed {}!".format(params.AVERAGE_VOLUME_ALLOWED_CURRENT))

        week_old = timezone.now() - timedelta(days=7)
        week_boxes = boxes.filter(created_date__gt=week_old)
        if week_boxes.count() > params.WEEKLY_BOX_ALLOWED:
        	raise serializers.ValidationError("Total Boxes added in a week cannot be more than {}!".format(params.WEEKLY_BOX_ALLOWED))

        if week_boxes.filter(creator=current_user).count() > params.WEEKLY_BOX_ALLOWED_CURRENT:
        	raise serializers.ValidationError("Total Boxes added in a week by a user cannot be more than {}!".format(params.WEEKLY_BOX_ALLOWED_CURRENT))
        return data

    def create(self, validated_data):
        length = validated_data['length']
        breadth = validated_data['breadth']
        height = validated_data['height']
        print(self.context['request'])
        validated_data['area'] = helpers.get_area(length, breadth, height)
        validated_data['volume'] = helpers.get_volume(length, breadth, height)
        return Box.objects.create(creator=self.context['request'].user, **validated_data)

    def update(self, instance, validated_data):
        instance.length = validated_data.get('length', instance.length)
        instance.breadth = validated_data.get('breadth', instance.breadth)
        instance.height = validated_data.get('height', instance.height)

        instance.area = helpers.get_area(instance.length, instance.breadth, instance.height)
        instance.volume = helpers.get_volume(instance.length, instance.breadth, instance.height)
        instance.save()
        return instance