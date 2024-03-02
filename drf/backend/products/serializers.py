from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Product model serializer."""
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field='pk')
    class Meta:
        model = Product
        fields = ('url','edit_url', 'pk', 'id', 'title', 'price', 'sales_price', 'my_discount', )


    def validate_title(self, value):
        qs = Product.objects.filter(title__iexact=value) # filter title that is similar to product title the reason iexact is to make sure it is more case sensetive.
        if qs.exists():
            raise serializers.ValidationError(f"A product with this {value} title already exists.")
        return value
    def get_edit_url(self, obj):
        request = self.context.get('request')
        print(request)
        if request is None:
            return None
        return reverse("product-update", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None