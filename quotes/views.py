import pandas as pd
from django.shortcuts import render
from django.core.paginator import Paginator

def quotes_view(request):
    df = pd.read_csv('quotes.csv')

    # Handle NaN safely
    df = df.fillna('')

    search_query = request.GET.get('q', '')

    # SEARCH
    if search_query:
        df = df[
            df['quote'].str.contains(search_query, case=False) |
            df['author'].str.contains(search_query, case=False) |
            df['tags'].str.contains(search_query, case=False)
        ]

    quotes = df.to_dict('records')

    # Split tags
    for q in quotes:
        q['tags'] = [tag.strip() for tag in q['tags'].split(',') if tag.strip()]

    # PAGINATION
    paginator = Paginator(quotes, 6)  # 6 cards per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'quotes.html', {
        'page_obj': page_obj,
        'search_query': search_query
    })
