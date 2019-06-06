from rest_framework.response import Response
from rest_framework import viewsets
from main.models import Product
from main.scraper import make_request, parse_response, save_product
from main.serializers import ProductSerializer


class ProductList(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        '''
        Endpoint that receives Asin and returns the parsed data
        '''
        try:
            obj = Product.objects.get(asin=pk)
            serializer = ProductSerializer(obj)
            product = serializer.data
        except Product.DoesNotExist:
            response = make_request(pk)
            product = parse_response(response, pk)
            # save_product(product)

        return Response(product)
