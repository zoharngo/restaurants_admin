# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from api.models import RestaurantModel 

class RestaurantItemSerialize(serializers.ModelSerializer):
    class Meta:
       model = RestaurantModel
       fields = "__all__"

  