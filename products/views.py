from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser

from .models import Product, Category
from .serializers import CategorySerializer, ProductSerializer

# get user model
from django.contrib.auth import get_user_model

User = get_user_model()

class ProductsList(ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        user_id = self.request.query_params.get('user_id')
        superuser = self.request.query_params.get('superuser')
        
        if superuser == 'true':
            user = User.objects.filter(is_admin=True).first()
            queryset = Product.objects.filter(user=user)
        else:
            queryset = Product.objects.filter(user_id=user_id)

        return queryset


class ProductDetails(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        user = self.request.query_params.get('user_id')
        serializer.save(user_id=user)
        