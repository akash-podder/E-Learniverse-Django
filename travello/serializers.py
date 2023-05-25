from rest_framework import serializers
from .models import FootballClub, Player

class DestinationSerializer(serializers.Serializer):

    # Id Required False karon API_response theke Data Create er somoy amra jokon is_validate call dibo jano tokon id Auto_generate hobe  .save() call dile
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=100)
    # img = serializers.ImageField(upload_to='pics')
    desc = serializers.CharField()
    price = serializers.IntegerField(default=0)
    is_club_in_city = serializers.BooleanField(default=False)


    # This Function is used for "De-Serialization"
    def create(self, validated_data):
        return FootballClub.objects.create(**validated_data)



class PlayerSerializer(serializers.Serializer):

    # Id Required False karon API_response theke Data Create er somoy amra jokon is_validate call dibo jano tokon id Auto_generate hobe  .save() call dile
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=100)
    desc = serializers.CharField()
    country = serializers.CharField()
    price = serializers.IntegerField(default=0)
    # img = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True, allow_null=True)


    # This Function is used for "De-Serialization"
    def create(self, validated_data):
        return Player.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # here instance = OLD Data Saved in Database
        # here validated_data = New Data from User for Updation

        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.country = validated_data.get('country', instance.country)
        instance.price = validated_data.get('price', instance.price)
        # instance.image = validated_data.get('image', instance.image)

        instance.save()
        return instance
