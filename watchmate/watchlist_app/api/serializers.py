from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'
        
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields ='__all__'
        
    # def get_len_name(self, obj):
    #     return len(obj.name)
        
    # def validate_name(self, value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value

    # def validate(self, data):
    #     if data['name'] == data['discreption']:
    #         raise serializers.ValidationError("Title and Description should be different!")
    #     else:
    #         return data
        

# def name_length(value):
#     if len(value)<2:
#         raise serializers.ValidationError("Name is too short!")
#     else:
#         return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators = [name_length])
#     discreption = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.discreption = validated_data.get('discreption', instance.discreption)
#         instance.active = validated_data.get('active', instance.active)
        
#         instance.save()
#         return instance
    
#     # def validate_name(self, value):
#     #     if len(value)<2:
#     #         raise serializers.ValidationError("Name is too short!")
#     #     else:
#     #         return value
        
#     def validate(self, data):
#         if data['name'] == data['discreption']:
#             raise serializers.ValidationError("Title and Description should be different!")
#         else:
#             return data