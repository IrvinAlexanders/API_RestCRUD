from rest_framework import serializers

from .models import Bill, BillProducts
from products.models import Product

from products.serializers import ProductModelSerializer


class BillModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = ('company_name', 'nit', 'code', 'client_id')

class BillProductsSerializer(serializers.ModelSerializer):

    bill = serializers.CharField()
    products = serializers.CharField()

    class Meta:
        model = BillProducts
        fields = ['bill', 'products']

    def create(self, data):

        new_bill = Bill.objects.filter(pk=data['bill']).first()
        new_product = Product.objects.filter(pk=data['products']).first()

        new_bill_product = BillProducts.objects.create(
            products=new_product,
            bill=new_bill
        )
        return new_bill_product