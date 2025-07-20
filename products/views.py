from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from products.models import Product
from products.serializers import CreateProductSerializer, ProductSerializer, ProductUpdateSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 100


def build_response(status=False, message="", error="", data=None, include_data=False):
    response = {
        "status": status,
        "message": message,
        "error": error,
    }
    if include_data:
        response["data"] = data
    return response


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Product.objects.all().order_by('-rating_rate')
        params = self.request.query_params

        search = params.get('search', '').strip()
        if search:
            queryset = queryset.filter(title__icontains=search)

        category = params.get('category', '').strip()
        if category:
            queryset = queryset.filter(category__iexact=category)

        try:
            min_price = float(params.get('min_price', '').strip())
            queryset = queryset.filter(price__gte=min_price)
        except (ValueError, TypeError):
            pass

        try:
            max_price = float(params.get('max_price', '').strip())
            queryset = queryset.filter(price__lte=max_price)
        except (ValueError, TypeError):
            pass

        return queryset


class CreateProductView(APIView):
    def post(self, request):
        responseData = build_response()
        data = request.data
        title = data.get('title', '').strip()

        if Product.objects.filter(title__iexact=title).exists():
            responseData["error"] = "Product with this title already exists."
            return Response(responseData, status=400)

        serializer = CreateProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save(
                title=title,
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
            responseData["status"] = True
            responseData["message"] = "Product created successfully."
            return Response(responseData, status=201)

        responseData["error"] = serializer.errors
        return Response(responseData, status=400)


class RetrieveProductView(APIView):
    def get(self, request):
        responseData = build_response(include_data=True)
        product_id = request.GET.get('product_id')

        if not product_id:
            responseData["error"] = "Missing 'product_id' in query parameters."
            return Response(responseData, status=400)

        try:
            product = Product.objects.get(id=product_id)
            responseData["status"] = True
            responseData["data"] = ProductSerializer(product).data
            responseData["message"] = "Product details fetched successfully."
            return Response(responseData, status=200)
        except Product.DoesNotExist:
            responseData["error"] = "Product not found."
            return Response(responseData, status=404)


class UpdateProductView(APIView):
    def put(self, request):
        responseData = build_response()
        product_id = request.GET.get('product_id')

        if not product_id:
            responseData["error"] = "Missing 'product_id' in query parameters."
            return Response(responseData, status=400)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            responseData["error"] = "Product not found."
            return Response(responseData, status=404)

        new_title = request.data.get("title", "").strip()
        if new_title and Product.objects.exclude(id=product_id).filter(title__iexact=new_title).exists():
            responseData["error"] = "Another product with this title already exists."
            return Response(responseData, status=400)

        serializer = ProductUpdateSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(updated_at=timezone.now())
            responseData["status"] = True
            responseData["message"] = "Product updated successfully."
            return Response(responseData, status=200)

        responseData["error"] = serializer.errors
        return Response(responseData, status=400)


class DeleteProductView(APIView):
    def delete(self, request):
        responseData = build_response()
        product_id = request.GET.get('product_id')

        if not product_id:
            responseData["error"] = "Missing 'product_id' in query parameters."
            return Response(responseData, status=400)

        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            responseData["status"] = True
            responseData["message"] = "Product deleted successfully."
            return Response(responseData, status=200)
        except Product.DoesNotExist:
            responseData["error"] = "Product not found."
            return Response(responseData, status=404)


class BulkDeleteProductsView(APIView):
    def delete(self, request):
        responseData = build_response()
        product_ids = request.data.get('product_ids')

        if not product_ids or not isinstance(product_ids, list):
            responseData["error"] = "'product_ids' must be a list of IDs."
            return Response(responseData, status=400)

        products_to_delete = Product.objects.filter(id__in=product_ids)
        deleted_count = products_to_delete.count()
        products_to_delete.delete()

        responseData["status"] = True
        responseData["message"] = f"{deleted_count} product(s) deleted successfully."
        return Response(responseData, status=200)
