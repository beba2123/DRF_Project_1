from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .permissions import IsStaffEditorPermision
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication,
                                    authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermision]

    def perform_create(self, serializer):
        print(serializer)
        serializer.save()

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance


class ProductDestroyApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_Delete(self, instance):
        super().perform_Delete(instance)


class ProductMixinsView(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get(self.lookup_field)
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

            # return self.list(request, *args, **kwargs)
    def post(self,  request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        print(serializer)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content =  f"This product was created by {title}"
        serializer.save(content= content)



@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'POST':
        #CREATE AN ITEM
        serializer  = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
                print(serializer.data)
                data = serializer.data
                return Response(data)

    if method == 'GET':
        #DETAIL VIEW
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)

        #LIST VIEW
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)