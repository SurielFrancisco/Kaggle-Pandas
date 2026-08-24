top_oceania_wines = reviews[
    reviews.country.isin(['Australia', 'New Zealand']) & (reviews.points >= 95)
]