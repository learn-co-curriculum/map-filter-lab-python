
# Map, Filter and Lambda in Python Lab

## Objectives
* Apply and combine the skills covered for map, filter and lambda functions.
* Modify given data using map and lambda functions as an alternative to writing for loops.
* Filter given data using filter function to only include the data that meets a given crietria. 

### Introduction

In this lab, we'll put our new knowledge about `map`, `filter` and `lambda` functions to the test. We'll also get back to working with Yelp again. Let's get started!


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

As you can see, it's a little tricky to see the names of all of the restaurants due to amount of data. Let's create a new list `names` to contain only the names of all the restaurants from the list above. Use the `map` and `lambda` functions, along with your understanding of a dictionary's structure to do so.


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

This worked well. Now let's get a sense of how many reviews were written for each of these restaurants. Just like above, create a new list `review_counts` to only contain the values of `review_count` for each restaurant.    


```python
review_counts = None
review_counts # [610, 11, 1373, 680, 54, 647, 25, 20]
```

Let's say we want to get a sense of total number of reviews in the whole dataset. We can add up the elements in `review_counts` list, and assign the result to a variable named `total_reviews`.


```python
total_reviews = None
total_reviews # 3420
```

It's a little tricky to work with the price in the format of dollars signs i.e. \$ and \$$ based on how expensive the restaurant is.  

So write a function called `format_restaurants` that changes each restaurant to have the attribute `'price'` point to the number of dollar signs (i.e. 1 for \$ and 2 for \$$).  We'll get you started with the function, `format_restaurant`.


```python
def format_restaurant(restaurant):
    if type(restaurant['price']) == str:
        restaurant['price'] = len(restaurant['price'])
    return restaurant
```


```python
format_restaurant(restaurants[0]) # {'is_closed': False, 'name': 'Fork & Fig', 'price': 2, 'review_count': 610}
```

Now write another function called `map_format_restaurants` using `map`, that uses above function and returns a list of restaurants with each of them formatted with price pointing to the respective number.


```python
def map_format_restaurants(restaurants):
    pass
```


```python
map_format_restaurants(restaurants)

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

Now let's use `filter` to search for restaurants based on specific criteria.  

Write a function called `open_restaurants` using `filter` and `lambda` that takes in a list of restaurants and only returns those that are open. You can use the distionary key `is_closed` to make a decision in your code. 


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

Let's say we now want to look at restaurants that are comparatively cheaper i.e. \$ or 1 as price. 

Write a function called `cheap_restaurants` using filter, that returns the restaurants that have a price of  1, or '$'.  


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

So we have only one restaurant in the data that meets the given criteria. Next, we shall write a function that filters out only those restaurants that 100 reviews or more, since we want to make sure there is some solid data points backing the reviews -- we are burgeoning data scientists after all!


```python
def sufficiently_reviewed_restaurants(restaurants):
    pass
```


```python
sufficiently_reviewed_restaurants(restaurants)

# [{'name': 'Fork & Fig', 'price': 2, 'is_closed': False, 'review_count': 610},
#  {'name': 'Frontier Restaurant', 'price': 1, 'is_closed': False,  'review_count': 1373},
#  {'name': 'Nexus Brewery', 'price': 2, 'is_closed': False, 'review_count': 680},
#  {'name': 'Cocina Azul', 'price': 2, 'is_closed': True, 'review_count': 647}]
```

### Summary

Neat! In this lab, we successfully proved our prowess when it comes to iterating over each element of a list with both `map` and `filter`! We used `map` to format our data into ways that better help us answer questions and extrapolate insights. We used `filter` to return subsets of our data like our restaurants that were only one $ or our restaurants that had 100 or more reviews.
