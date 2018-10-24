# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from api.models import RestaurantModel
from api.serializers import RestaurantItemSerialize
from rest_framework import status
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.decorators import list_route
from rest_framework.response import Response

class RestaurantsViewSet(viewsets.ModelViewSet):
    queryset = RestaurantModel.objects.all()
    serializer_class  = RestaurantItemSerialize

    # Save instance to get primery key and then update URL
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # Delete all restaurants 
    def delete(self, request):
        RestaurantModel.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
