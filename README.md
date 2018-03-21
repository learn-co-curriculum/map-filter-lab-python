
# Functions with arguments lab

### Introduction

In this lesson, we will be scoping out some of the things that we can do while in Albuquerque.  To do so, we'll be working with information pulled from the Yelp.  Yelp is great for learning about what to do in Albuquerque, but it gives us back a lot of information.  We'll use what we know about functions to format out data. 

### Exploring two restuarants in Albuquerque

This is what the Yelp provides us for a information about a single restaurant.  Below is information about Fork and Fig, but all restaurants are provided with this information.


```python
fork_fig = {'categories': [{'alias': 'burgers', 'title': 'Burgers'},
  {'alias': 'sandwiches', 'title': 'Sandwiches'},
  {'alias': 'salad', 'title': 'Salad'}],
 'coordinates': {'latitude': 35.10871, 'longitude': -106.56739},
 'display_phone': '(505) 881-5293',
 'distance': 3571.724649307866,
 'id': 'fork-and-fig-albuquerque',
 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/_-DpXKfS3jv6DyA47g6Fxg/o.jpg',
 'is_closed': False,
 'location': {'address1': '6904 Menaul Blvd NE',
  'address2': 'Ste C',
  'address3': '',
  'city': 'Albuquerque',
  'country': 'US',
  'display_address': ['6904 Menaul Blvd NE', 'Ste C', 'Albuquerque, NM 87110'],
  'state': 'NM',
  'zip_code': '87110'},
 'name': 'Fork & Fig',
 'phone': '+15058815293',
 'price': '$$',
 'rating': 4.5,
 'review_count': 604,
 'transactions': [],
 'url': 'https://www.yelp.com/biz/fork-and-fig-albuquerque?adjust_creative=SYc8R4Gowqru5h4SBKZXsQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=SYc8R4Gowqru5h4SBKZXsQ'}
```

For example, here is another one.


```python
frontier_restaurant = {'categories': [{'alias': 'mexican', 'title': 'Mexican'},
  {'alias': 'diners', 'title': 'Diners'},
  {'alias': 'tradamerican', 'title': 'American (Traditional)'}],
 'coordinates': {'latitude': 35.0808088832532, 'longitude': -106.619402244687},
 'display_phone': '(505) 266-0550',
 'distance': 4033.6583235266075,
 'id': 'frontier-restaurant-albuquerque-2',
 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/M9L2z6-G0NobuDJ6YTh6VA/o.jpg',
 'is_closed': False,
 'location': {'address1': '2400 Central Ave SE',
  'address2': '',
  'address3': '',
  'city': 'Albuquerque',
  'country': 'US',
  'display_address': ['2400 Central Ave SE', 'Albuquerque, NM 87106'],
  'state': 'NM',
  'zip_code': '87106'},
 'name': 'Frontier Restaurant',
 'phone': '+15052660550',
 'price': '$',
 'rating': 4.0,
 'review_count': 1369,
 'transactions': [],
 'url': 'https://www.yelp.com/biz/frontier-restaurant-albuquerque-2?adjust_creative=SYc8R4Gowqru5h4SBKZXsQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=SYc8R4Gowqru5h4SBKZXsQ'}
```

One way to quickly view a dictionary is to look at the keys of the dictionary.


```python
fork_fig.keys()
```




    dict_keys(['categories', 'coordinates', 'display_phone', 'distance', 'id', 'image_url', 'is_closed', 'location', 'name', 'phone', 'price', 'rating', 'review_count', 'transactions', 'url'])




```python
frontier_restaurant.keys()
```




    dict_keys(['categories', 'coordinates', 'display_phone', 'distance', 'id', 'image_url', 'is_closed', 'location', 'name', 'phone', 'price', 'rating', 'review_count', 'transactions', 'url'])



As you can see, Yelp provides us with the same information on both restaurants.  

### Writing our functions

Ok, now let's write our functions.  Write a function called `restaurant_name` that provided a dictionary representing a restaurant like you saw above, resturns that restaurant's name.


```python
def restaurant_name(restaurant):
    return restaurant['name']
```


```python
restaurant_name(frontier_restaurant) # 'Frontier Restaurant'
```




    'Frontier Restaurant'




```python
restaurant_name(fork_fig) # 'Frontier Restaurant'
```




    'Fork & Fig'



Now write a function called `restaurant_rating` that returns the rating of the restaurant provided a function.


```python
def restaurant_rating(restaurant):
    return restaurant['rating']
```


```python
restaurant_rating(frontier_restaurant) # 4.0
```




    4.0




```python
restaurant_rating(fork_fig) # 4.5
```




    4.5



### Comparing restaurants

Now let's write a function called `is_better` that returns `True` if a restaurant has a higher rating than an alternative restaurant.  The first argument should be called `restaurant` and the second argument should be called `alternative`.  The function returns `False` if the two ratings are equal.


```python
def is_better(restaurant, alternative):
    return restaurant['rating'] > alternative['rating']
```


```python
is_better(frontier_restaurant, fork_fig) # False
is_better(fork_fig, frontier_restaurant) # True
is_better(fork_fig, fork_fig) # False
```




    False



Now let's write a function called `is_cheaper` that returns `True` if a restaurant has a higher price, that is has more `'$'` signs, than an alternative restaurant.  The first argument should be called `restaurant` and the second argument should be called `alternative`.  The function returns `False` if the two prices are equal.


```python
def is_cheaper(restaurant, alternative):
    return len(restaurant['price']) < len(alternative['price'])
```


```python
is_cheaper(fork_fig, frontier_restaurant) # False
is_cheaper(frontier_restaurant, fork_fig) # True
is_cheaper(fork_fig, fork_fig) # False
```




    False



Now write a function called `high_rating` than that takes a `restaurant` as a first argument and a number that represents a rating as the second argument.  If the second argument is not provided, then the function returns `True` so long as the retaurant's rating is greater than 4.


```python
def high_rating(restaurant, rating = 4):
    return restaurant['rating'] > rating
```


```python
high_rating(fork_fig, 4) # True
high_rating(fork_fig, 5) # False
high_rating(fork_fig) # True
high_rating(frontier_restaurant) # False
```




    False



### Summary

Great!  Through this lab we saw how to pass arguments to functions, multiple arguments to functions, and how to implement functinons with default arguments.
