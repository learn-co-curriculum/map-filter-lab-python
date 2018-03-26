
# Map and Filter in Python Lab

### Introduction

Let's continue to work with our Yelp Api.  


```python
from restaurants import yelp_restaurants
# dict_keys(['categories', 'coordinates', 'display_phone', 'distance', 
# 'id', 'image_url', 'is_closed', 'location', 'name', 'phone', 'price', 
# 'rating', 'review_count', 'transactions', 'url'])
```


```python
restaurants = list(map(lambda restaurant: dict(name=restaurant['name'], 
                                           price=restaurant['price'], 
                                           is_closed=restaurant['is_closed'],
                                           review_count=restaurant['review_count'],
                                          ), yelp_restaurants))
```

We have a list of five restaurants from the Yelp Api.  Let's take a look at the list.


```python
restaurants
```




    [{'is_closed': False,
      'name': 'Fork & Fig',
      'price': '$$',
      'review_count': 610},
     {'is_closed': False,
      'name': 'Salt And Board',
      'price': '$$',
      'review_count': 11},
     {'is_closed': False,
      'name': 'Frontier Restaurant',
      'price': '$',
      'review_count': 1373},
     {'is_closed': False,
      'name': 'Nexus Brewery',
      'price': '$$',
      'review_count': 680},
     {'is_closed': False,
      'name': "Devon's Pop Smoke",
      'price': '$$',
      'review_count': 54},
     {'is_closed': True,
      'name': 'Cocina Azul',
      'price': '$$',
      'review_count': 647},
     {'is_closed': False,
      'name': 'Philly Steaks',
      'price': '$$',
      'review_count': 25},
     {'is_closed': True,
      'name': 'Stripes Biscuit',
      'price': '$$',
      'review_count': 20}]



### Using map

As you can see, it's a little tricky to see the names of all of the restaurants.  Assign a variable `names` to the list of names of the functions.  Use the `map` function to do so.


```python
names = list(map(lambda restaurant: restaurant['name'] ,restaurants))
names
```




    ['Fork & Fig',
     'Salt And Board',
     'Frontier Restaurant',
     'Nexus Brewery',
     "Devon's Pop Smoke",
     'Cocina Azul',
     'Philly Steaks',
     'Stripes Biscuit']



Let's get a sense of how many reviews were written for each of the restaurants.  Assign a variable `review_counts` to equal a list of the `review_count` for each restaurant.  


```python
review_counts = list(map(lambda restaurant: restaurant['review_count'] ,restaurants))
review_counts
```




    [610, 11, 1373, 680, 54, 647, 25, 20]



Now add up the elements in the list, and assign the result to a variable named `total_reviews`.


```python
total_reviews = sum(review_counts)
total_reviews
```




    3420



It's a little tricky to work with the price in the format of dollars signs.  So write a called `format_restaurants` that changes each restaurant to have the attribute `'price'` point to the number of dollar signs.  We'll get you started with the function, `format_restaurant`.


```python
def format_restaurant(restaurant):
    if type(restaurant['price']) == str:
        restaurant['price'] = len(restaurant['price'])
    return restaurant
```


```python
format_restaurant(restaurants[0])
```




    {'is_closed': False, 'name': 'Fork & Fig', 'price': 2, 'review_count': 610}



Now write a function called `format_restaurants`, that returns a list of restaurants with each of them formatted with price pointing to the respective number.


```python
def format_restaurants(restaurants):
    return list(map(format_restaurant,restaurants))
```


```python
format_restaurants(restaurants)
```

### Filter

Now let's search for restaurants based on specific criteria.  

Write a function called `open_restaurants` that takes in a list of restaurants and only returns those that are open.


```python
def open_restaurants(restaurants):
    return list(filter(lambda restaurant:not restaurant['is_closed'] ,restaurants))
```


```python
open_restaurants(restaurants)

# [{'is_closed': False, 'name': 'Fork & Fig', 'price': 2, 'review_count': 610},
#  {'is_closed': False,
#   'name': 'Salt And Board',
#   'price': 2,
#   'review_count': 11},
#  {'is_closed': False,
#   'name': 'Frontier Restaurant',
#   'price': 1,
#   'review_count': 1373},
#  {'is_closed': False,
#   'name': 'Nexus Brewery',
#   'price': 2,
#   'review_count': 680},
#  {'is_closed': False,
#   'name': "Devon's Pop Smoke",
#   'price': 2,
#   'review_count': 54},
#  {'is_closed': False, 'name': 'Philly Steaks', 'price': 2, 'review_count': 25}]
```

Now write a function called `cheapest_restaurants` that returns restaurants those restaurants that have a price of  1, or '$'.  


```python
def cheapest_restaurants(restaurants):
    return list(filter(lambda restaurant: restaurant['price'] == 1 ,restaurants))
```


```python
cheapest_restaurants(restaurants)

# [{'is_closed': False,
#   'name': 'Frontier Restaurant',
#   'price': 1,
#   'review_count': 1373}]
```




    [{'is_closed': False,
      'name': 'Frontier Restaurant',
      'price': 1,
      'review_count': 1373}]



### Summary

Great!  Through this lab we saw how to pass arguments to functions, multiple arguments to functions, and how to implement functinons with default arguments.
