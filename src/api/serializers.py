# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from api.models import RestaurantModel,Location 



class LocationSerialize(serializers.ModelSerializer):
    coordinates = serializers.ReadOnlyField()
    class Meta:
       model = Location
       fields = "__all__"

class RestaurantItemSerialize(serializers.ModelSerializer):
    location = LocationSerialize(required=False)
    uuid = serializers.ReadOnlyField()
    class Meta:
       model = RestaurantModel
       fields = "__all__"

    def create(self, validated_data):
            """
            Overriding the default create method of the Model serializer.
            :param validated_data: data containing all the details of Restaurant
            :return: returns a successfully created Restaurant record
            """
            location_data = validated_data.pop('location')
            location = LocationSerialize.create(LocationSerialize(), validated_data=location_data)
            restaurants, created = RestaurantModel.objects.update_or_create(
                                location=location,
                                restaurant_name=validated_data.pop('restaurant_name'),
                                restaurant_type=validated_data.pop('restaurant_type'),
                                phone=validated_data.pop('phone'))
            return restaurants
  