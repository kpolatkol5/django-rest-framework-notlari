from rest_framework import serializers

from blog.models import Blog

class Blog_Serializer(serializers.Serializer):

    id=serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama=serializers.CharField()
    metin = serializers.CharField()
    yayimlanma_tarihi = serializers.DateField(read_only=True)
    yaratilma_tarihi = serializers.DateField(read_only=True)

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.yazar = validated_data.get("yazar" , instance.yazar)
        instance.baslik = validated_data.get("baslik" , instance.baslik)
        instance.aciklama = validated_data.get("aciklama" , instance.aciklama)
        instance.metin = validated_data.get("metin" , instance.metin)
        instance.save()
        return instance



