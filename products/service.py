import requests
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Product

class ImportFakeStoreProductsView(APIView):
    def get(self, request):
        url = 'https://fakestoreapi.com/products'

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        data = response.json()
        now = timezone.now()

        # Fetch existing titles to avoid duplicates
        existing_titles = set(Product.objects.values_list('title', flat=True))

        product_objs = []
        for item in data:
            title = item.get('title')
            if title in existing_titles:
                continue

            product_objs.append(Product(
                title=title,
                price=item.get('price', 0),
                description=item.get('description', ''),
                category=item.get('category', ''),
                image=item.get('image', ''),
                rating_rate=item.get('rating', {}).get('rate', 0),
                rating_count=item.get('rating', {}).get('count', 0),
                created_at=now,
                updated_at=now
            ))

        # Bulk insert
        Product.objects.bulk_create(product_objs, batch_size=100)

        return Response({
            'message': 'Bulk import completed.',
            'products_created': len(product_objs),
            'products_skipped': len(data) - len(product_objs)
        }, status=status.HTTP_201_CREATED)

