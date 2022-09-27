from django.shortcuts import render

# Create your views here.

def wishlist_summary(request):
    return render(request, 'store/wishlist/wishlist.html')