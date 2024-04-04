from rest_framework import serializers
from .models import Travel, Country
from users.serializers import CitySerializer



class CountrySerializer(serializers.ModelSerializer):
    travel_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Country
        fields = '__all__'

class TravelSerializer(serializers.ModelSerializer):
    travel_count = serializers.IntegerField(read_only=True)
    from_city = CitySerializer()  # Вложенный сериализатор для города
    country = CountrySerializer()  # Вложенный сериализатор для страны

    class Meta:
        model = Travel
        fields = '__all__'

 'name', 'image', 'travel_count']