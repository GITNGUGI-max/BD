from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields= ('url', 'id', 'username', 'password')
	

class CountySerializer(serializers.ModelSerializer):
	class Meta:
		model=County
		fields=('url', 'id', 'countyName')

class SubCountySerializer(serializers.ModelSerializer):

	class Meta:
		model=SubCounty
		fields=['url', 'id', 'county', 'subCountyName']	

class DonorSerializer(serializers.ModelSerializer):


	county = serializers.SlugRelatedField(
		 queryset = County.objects.all(),
		 slug_field='countyName'
	 )
	subCounty = serializers.SlugRelatedField(
		 queryset = SubCounty.objects.all(),
		 slug_field = 'subCountyName'
		
	 )
	 
	class Meta:
	 	model=Donor
	 	fields=['url', 'id', 'donorName', 'gender', 'dateOfBirth', 'bloodGroup', 'weight', 'email', 
	 			'location', 'county', 'subCounty', 'contactOne', 'contactTwo', 'voluntary', 'newDonor', 
	 			'lastDonated', 'image','status'
	 	 ]
	 	
class PatientSerializer(serializers.ModelSerializer):
	 county = serializers.SlugRelatedField(
		 queryset = County.objects.all(),
		 slug_field='countyName'
	 )
	 
	 subCounty = serializers.SlugRelatedField(
		 queryset = SubCounty.objects.all(),
		 slug_field = 'subCountyName'
	 )
	
	 class Meta:
			model=Patient
			fields=['url', 'id', 'patientName', 'hospital', 'county', 'subCounty', 
			'doctor', 'contactName', 'email', 'contactDate', 'requiredDate', 
			'bloodUnits', 'bloodGroup', 'contactOne', 'contactTwo', 'reason', 'status']
			
class MessageSerializer(serializers.ModelSerializer):

	class Meta:
		model=Message
		fields=['url', 'id', 'sender', 'senderName', 'senderEmail', 'sentDate', 'contact', 'message', 'status']




