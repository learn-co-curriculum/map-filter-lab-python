
# Map and Filter in Python Lab

### Introduction

In this lab, we'll put our new knowledge about map and filter to the test. We'll also get back to working with Yelp again. Let's get started!


```python
from restaurants import yelp_restaurants # in this line we are simply importing our data we gathered from Yelp.
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




    [{'name': 'Fork & Fig',
      'price': '$$',
      'is_closed': False,
      'review_count': 610},
     {'name': 'Salt And Board',
      'price': '$$',
      'is_closed': False,
      'review_count': 11},
     {'name': 'Frontier Restaurant',
      'price': '$',
      'is_closed': False,
      'review_count': 1373},
     {'name': 'Nexus Brewery',
      'price': '$$',
      'is_closed': False,
      'review_count': 680},
     {'name': "Devon's Pop Smoke",
      'price': '$$',
      'is_closed': False,
      'review_count': 54},
     {'name': 'Cocina Azul',
      'price': '$$',
      'is_closed': True,
      'review_count': 647},
     {'name': 'Philly Steaks',
      'price': '$$',
      'is_closed': False,
      'review_count': 25},
     {'name': 'Stripes Biscuit',
      'price': '$$',
      'is_closed': True,
      'review_count': 20}]



### Using map

As you can see, it's a little tricky to see the names of all of the restaurants.  Assign a variable `names` to equal the list of names of the functions.  Use the `map` function to do so.


```python
names = None
names
# ['Fork & Fig',
#  'Salt And Board',
#  'Frontier Restaurant',
#  'Nexus Brewery',
#  "Devon's Pop Smoke",
#  'Cocina Azul',
#  'Philly Steaks',
#  'Stripes Biscuit']
```

Let's get a sense of how many reviews were written for each of the restaurants.  Assign a variable `review_counts` to equal a list of the `review_count` for each restaurant.  


```python
review_counts = None
review_counts # [610, 11, 1373, 680, 54, 647, 25, 20]
```

Now add up the elements in the list, and assign the result to a variable named `total_reviews`.


```python
total_reviews = None
total_reviews # 3420
```

It's a little tricky to work with the price in the format of dollars signs.  So write a function called `format_restaurants` that changes each restaurant to have the attribute `'price'` point to the number of dollar signs.  We'll get you started with the function, `format_restaurant`.


```python
def format_restaurant(restaurant):
    if type(restaurant['price']) == str:
        restaurant['price'] = len(restaurant['price'])
    return restaurant
```


```python
format_restaurant(restaurants[0]) # {'is_closed': False, 'name': 'Fork & Fig', 'price': 2, 'review_count': 610}
```




    {'is_closed': False, 'name': 'Fork & Fig', 'price': 2, 'review_count': 610}



Now write a function called `format_restaurants`, that returns a list of restaurants with each of them formatted with price pointing to the respective number.


```python
def format_restaurants(restaurants):
    return list(map(format_restaurant,restaurants))
```


```python
format_restaurants(restaurants)

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
#  {'is_closed': True, 'name': 'Cocina Azul', 'price': 2, 'review_count': 647},
#  {'is_closed': False, 'name': 'Philly Steaks', 'price': 2, 'review_count': 25},
#  {'is_closed': True,
#   'name': 'Stripes Biscuit',
#   'price': 2,
#   'review_count': 20}]
```

### Filter

Now let's search for restaurants based on specific criteria.  

Write a function called `open_restaurants` that takes in a list of restaurants and only returns those that are open.


```python
def open_restaurants(restaurants):
    pass
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

Now write a function called `cheapest_restaurants` that returns the restaurants that have a price of  1, or '$'.  


```python
def cheapest_restaurants(restaurants):
    pass
```


```python
cheapest_restaurants(restaurants)

# [{'is_closed': False,
#   'name': 'Frontier Restaurant',
#   'price': 1,
#   'review_count': 1373}]
```

Next, write a function that filters out only those restaurants that 100 reviews or more, since we want to make sure there is some solid data points backing the reviews -- we are burgeoning data scientists after all!


```python
def sufficiently_reviewed_restaurants(restuarants)
    pass
```


```python
sufficiently_reviewed_restaurants(restuarants)

# [{'is_closed': False, 
#   'name': 'Fork & Fig', 
#   'price': 2,
#   'review_count': 610},
#  {'is_closed': False,
#   'name': 'Frontier Restaurant',
#   'price': 1,
#   'review_count': 1373},
#  {'is_closed': False,
#   'name': 'Nexus Brewery',
#   'price': 2,
#   'review_count': 680}]
```

### Summary

Neat! In this lab, we successfully proved our prowess when it comes to iterating over each element of a list with both `map` and `filter`! We used `map` to format our data into ways that better help us answer questions and extrapolate insights. We used `filter` to return subsets of our data like our restaurants that were only one $ or our restaurants that had 100 or more reviews.
