from django.db import models

# Create your models here.
class Testimonial(models.Model) :
    client_name = models.CharField(max_length=150)
    quote = models.TextField()

    wedding_date = models.DateField(
        blank=True,
        null=True
    )

    display_order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return self.client_name