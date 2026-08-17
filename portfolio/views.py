from django.shortcuts import render
from .models import PortfolioItem

# Create your views here.
def portfolio_home(request):
    items = PortfolioItem.objects.filter(is_published=True)

    return render(request, "portfolio/portfolio.html", {"items": items},)
