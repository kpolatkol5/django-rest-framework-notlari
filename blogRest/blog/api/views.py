from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blog.models import Blog
from blog.api.serializers import Blog_Serializer

# class Based view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404






class GetBLogListAndCreate(APIView):


    def get(self,request):

        bloglar = Blog.objects.all()
        serializer = Blog_Serializer(bloglar , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def post(self ,request):
        serializer = Blog_Serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)




class GetBlogDetail(APIView):

    def get_instance(self , pk):

        makale = get_object_or_404(Blog,pk=pk)
        return makale

    def get(self ,request , pk):
        
        makale = self.get_instance(pk=pk)
        print(makale)
        serializer = Blog_Serializer(makale)
        print(serializer)

        return Response(serializer.data)



    def put(self , request , pk):
        makale = self.get_instance(pk=pk)
        serializer = Blog_Serializer(makale , data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors)


    def delete(self ,request , pk):
        makale = self.get_instance(pk=pk)

        makale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










""" 

@api_view(["GET" , "POST"])
def makale_list_create_api_views(request):
    if request.method == "GET":
        bloglar=Blog.objects.all()
        serializer = Blog_Serializer(bloglar,many=True)
        print(serializer)
        return Response(serializer.data , status=status.HTTP_200_OK)

    elif request.method =="POST":
        serializer = Blog_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET" , "PUT" , "DELETE"])
def blog_detail(request , pk):

    try:
        makale = Blog.objects.get(pk=pk)

    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)




    if request.method == "GET":
        serializer = Blog_Serializer(makale)
        return Response(serializer.data , status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = Blog_Serializer(makale , request.data )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)



    elif request.method == "DELETE":
        makale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) """
    



