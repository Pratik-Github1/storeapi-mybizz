from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255, unique=True, db_index=True)
    price = models.FloatField(default=0, db_index=True)
    description = models.TextField()
    category = models.CharField(max_length=100, db_index=True)
    image = models.CharField(max_length=512)
    rating_rate = models.FloatField(default=0, db_index=True)
    rating_count = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=False, db_index=True)

    class Meta:
        managed = False
        db_table = 'products'
        indexes = [
            models.Index(fields=['category'], name='idx_category'),
            models.Index(fields=['rating_rate'], name='idx_rating_rate'),
            models.Index(fields=['price'], name='idx_price'),
            models.Index(fields=['title'], name='idx_title'),
            models.Index(fields=['created_at'], name='idx_created_at'),
            models.Index(fields=['updated_at'], name='idx_updated_at')
        ]


    
