from rest_framework import generics
from .models import Template, Website, Page
from .serializers import TemplateSerializer, WebsiteSerializer, PageSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class TemplateListCreateView(generics.ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

class WebsiteListCreateView(APIView):
    def get(self, request, format=None):
        user_id = request.query_params.get('user_id')
        if user_id is not None:
            websites = Website.objects.filter(user_id=user_id)
            serializer = WebsiteSerializer(websites, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, format=None):
        serializer = WebsiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WebsiteDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Website.objects.get(pk=pk)
        except Website.DoesNotExist:
            return None
        
    def get(self, request, pk, format=None):
        website = self.get_object(pk)
        if website is not None:
            serializer = WebsiteSerializer(website)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        website = self.get_object(pk)
        if website is not None:
            website.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PageListCreateView(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
