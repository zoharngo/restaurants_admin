# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from api.models import RestaurantModel, Location
from api.serializers import RestaurantItemSerialize
from rest_framework import status
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.decorators import list_route
from rest_framework.response import Response
import json
import requests


class RestaurantsViewSet(viewsets.ModelViewSet):
    queryset = RestaurantModel.objects.all()
    serializer_class  = RestaurantItemSerialize

    # Save instance to get primery key and then update URL
    def create(self, request, *args, **kwargs):   
        self.convert_coords_to_address(restaurants=request.data)
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            headers = self.get_success_headers(serializer.data)            
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)
                        
    def convert_coords_to_address(self,restaurants):
        try:
            for restaurant in restaurants:
                coords = restaurant['location']['coordinates'].split('/')
                if len(coords) is 2 and float(coords[0]) and float(coords[1]):
                    url = 'https://{GeocodeMapUrlAPI}{lat},{lng}&key={MapApiKey}'.format(
                       GeocodeMapUrlAPI='maps.googleapis.com/maps/api/geocode/json?latlng=',
                       lat=coords[0],
                       lng=coords[1],
                       MapApiKey='AIzaSyA2Z4OUcvc5HSKEachHAy8uYyEwnsz7Z6Y')
                    try:
                        response = requests.get(url)                    
                        restaurant['location']['address'] = response.json()['results'][0]['formatted_address'] 
                    finally:
                        response.close()
        except ValueError as e:
            raise e
    
    def perform_destroy(self, instance):
        instance.location.delete()
        super(RestaurantsViewSet,self).perform_destroy
        

    # Delete all restaurants 
    def delete(self, request):
        RestaurantModel.objects.all().delete()
        Location.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
