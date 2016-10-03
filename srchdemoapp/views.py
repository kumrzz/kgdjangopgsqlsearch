from django.shortcuts import render, redirect, render_to_response, get_object_or_404, reverse
from .models import Category, Listing
from django.contrib.postgres.search import SearchVector

def all_listings(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    listings = Listing.objects.all()
    cat_results = lst_results = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        listings = listings.filter(category__in=[category.id])
        categories = categories.filter(pk__in=[category.id])
    if category == None:
        categories = Category.objects.all()
    #search results/view:
    if ('q' in request.GET) and request.GET['q'].strip():
        lst_results = Listing.objects.annotate(search=SearchVector('name', 'category__name'),
                                 ).filter(search=request.GET['q'])
        print [f.name for f in lst_results]
        cat_results = Category.objects.filter(name__search=request.GET['q'])
        i = 0
        catinclusion3 = []
        catinclusion2 = []
        for cat in cat_results:
            i += 1
            catinclusion2.append([f.id for f in cat_results])
        for j in range(0,i):
            catinclusion3 = catinclusion3 + catinclusion2[j]
        lstinclusion = [f.id for f in listings.filter(category__in=catinclusion3)]
        lstinclusion = lstinclusion + [f.id for f in lst_results]
        listings = listings.filter( id__in = lstinclusion )

        return render(request, 'srchdemoapp/listings/list.html', {'categories': categories,
                                                    'category': category,
                                                    'listings': listings,
                                                    'cat_results': cat_results,
                                                    'lst_results': lst_results})
    #initial rendering:
    return render(request, 'srchdemoapp/listings/list.html', {'categories': categories,
                                                    'category': category,
                                                    'listings': listings,
                                                    'cat_results': cat_results,
                                                    'lst_results': lst_results})
