from django.db import models

# Create your models here.
class PortfolioItem(models.Model):
    title = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to="portfolio/")
    alt_text = models.CharField(max_length=200)
    display_order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return self.title or f"Portfolio item {self.pk}"
