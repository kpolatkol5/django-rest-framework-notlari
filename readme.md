# Serializer Kavramı 


Karmaşık veri yapılarını , model örnkelerini  json xml gibi veri yapılarını python verilerine dönüştürmek ve  diğer sistemlerle iletişim kuracak şekilde veri oluşturmak için kullanırız.Mesela elimizde ürün bilgilerinin bulunduğu bir json verileri ve bir e-ticaret uygulaması olsun. Serileştiriciler ile kolaylıkla json verilerini alıp python verilerine dönüştürerek veritabanına ekleme işlemi yapabilriz. Veya bu durumun tam tersi de olabilir. Elimizde ürünlerin bir datası varsa ve biz bu datayı ilgili kişilerle paylaşmak istersek bunu serializer ile json veri türüne dönüştürüp paylaşabiliriz.  

<br>

# Manuel Serializer Tanımlaması

<br>

Oluşturduğumuz app in içersine api dizini tanımlayalım. Projedeki dosyaların daha düzneli olması ve kullanılabilirliği arttırmak için yapıyoruz. Aslında öyle bir dizin oluşturulmak zorunda değiliz. Model dosyasında tanımladığımız sınıfı ve serializer dosyasını import edelim.

<br>

blog/models
```py
from django.db import models


class Blog(models.Model):
    yazar = models.CharField(max_length=50 , verbose_name="yazar")
    baslik = models.CharField(max_length=50 , verbose_name="baslik")
    aciklama = models.CharField(max_length=100)
    metin = models.CharField(max_length=150)
    yayimlanma_tarihi = models.DateField(auto_now=True)
    yaratilma_tahrihi = models.DateField(auto_now_add=True)


```


<br>

blog/api/serializer.py
```py
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
```

<br>

Serializer tanımlarken dikkat edilmesi gerekenler;

- Modelde tanımlanan alan isimleri ile serializer da tanımlanan alan isimleri aynı olması gerekiyor.
- Modelde tanımlanan alanların parametrelerini tekrar tanımlaya gerek yok zaten oluşturulan serileri modelde kaydetmeye çalıştığımızda o tanımlamalar modelde olacağı için tekrar tanımlamamıza gerek yok.
- Eğer değişiklik yapılmayacak alanlar tanımlamak istersek paranterler içerisinde ```read_only=True``` paramteresini tanımlamamız gerekiyor. Bu alanlar okuanbilir ancak değiştirilemez.



