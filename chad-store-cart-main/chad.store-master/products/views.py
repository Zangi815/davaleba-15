from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, mixins,generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from products.models import (
    Product,
    Review,
    FavoriteProduct,
    Cart,
    ProductTag
)
from products.serializers import (
    ProductSerializer,
    ReviewSerializer,
    FavoriteProductSerializer,
    CartSerializer,
    ProductTagSerializer
    
    )


class ProductViewSet(RetrieveModelMixin, 
                    CreateModelMixin,
                    ListModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
    
class ReviewViewSet(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk=None, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)   
    

class FavoriteProductViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = FavoriteProduct.objects.all()
    serializer_class = FavoriteProductSerializer
    permission_classes = [IsAuthenticated]  
    
    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset
    
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class CartViewSet(ListModelMixin,CreateModelMixin, GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset
    
    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProductTagView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = ProductTag.objects.all()
    serializer_class = ProductTagSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class FavoriteProductView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = FavoriteProductSerializer

    def get_queryset(self):
        return FavoriteProduct.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  

class CartView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = request.user

        cart, created = Cart.objects.get_or_create(user=user)

        return self.create(request, *args, **kwargs)  

