from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication,BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Category, Product, Order,User
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer,UserRegisterSerializer
from .permissions import IsAuthenticatedOrSafeMethods
from rest_framework.decorators import api_view,authentication_classes



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods]



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods]


@api_view(http_method_names=['GET', ])
@authentication_classes([BasicAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_user_info(request):
    user = request.user
    data = {
        'username': user.username,
        'password': user.password
    }
    return Response(data)



@api_view(http_method_names=['POST'])
def user_register(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)



