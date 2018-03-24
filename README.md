
# Conditionals in Python Lab

### Introduction

In our earlier lab on working with functional arguments, we found ways to work with food in Yelp.  In this lesson, we'll add new methods with our new knowledge of conditionals.

### Again, our two restuarants in Albuquerque

Let's take another look at our data for a single restaurant.  Once again, we have Fork and Fig, as our sample of the data Yelp will provide on a restaurant.


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

And here is Frontier.


```python
frontier_restaurant = {'categories': [{'alias': 'mexican', 'title': 'Mexican'},
  {'alias': 'diners', 'title': 'Diners'},
  {'alias': 'tradamerican', 'title': 'American (Traditional)'}],
 'coordinates': {'latitude': 35.0808088832532, 'longitude': -106.619402244687},
 'display_phone': '(505) 266-0550',
 'distance': 4033.6583235266075,
 'id': 'frontier-restaurant-albuquerque-2',
 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/M9L2z6-G0NobuDJ6YTh6VA/o.jpg',
 'is_closed': True,
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

And once again, here are the keys of the dictionaries above.


```python
fork_fig.keys()
```




    dict_keys(['categories', 'coordinates', 'display_phone', 'distance', 'id', 'image_url', 'is_closed', 'location', 'name', 'phone', 'price', 'rating', 'review_count', 'transactions', 'url'])



### Writing functions with conditionals

Now let's write a function called `better_restaurant` that provided two restaurants, resturns the restaurant with the better rating.  The first argument is `restaurant` and the second argument is `alternative`.  


```python
def better_restaurant(restaurant, alternative):
    if restaurant['rating'] > alternative['rating']:
        return restaurant
    else:
        return alternative
```


```python
better_restaurant(frontier_restaurant, fork_fig)['name'] # 'Fork & Fig'
better_restaurant(fork_fig, frontier_restaurant)['name'] # 'Fork & Fig'
```




    'Fork & Fig'



Now let's write a function called `cheaper_restaurant` that returns the restaurant that has a higher price, that is the restaurant that has more `'$'` signs, than the alternative restaurant.  The first argument is `restaurant` and the second argument is `alternative`.


```python
def cheaper_restaurant(restaurant, alternative):
    if len(restaurant['price']) < len(alternative['price']):
        return restaurant
    else:
        return alternative
```


```python
cheaper_restaurant(fork_fig, frontier_restaurant)['name'] # 'Frontier Restaurant'
cheaper_restaurant(frontier_restaurant, fork_fig)['name'] # 'Frontier Restaurant'
```




    'Frontier Restaurant'



### Conditionals and Loops

Let's continue our work of conditionals by seeing how they can be combined with loops.  So write a function called `open_restaurants` that takes as an argument a list of restaurants and returns only a list of only the restaurants that are not closed.  


```python
fork_fig['is_closed'] # False
frontier_restaurant['is_closed'] # True
```




    True




```python
restaurants = [fork_fig, frontier_restaurant]
```


```python
def open_restaurants(restaurants):
    selected = []
    for restaurant in restaurants:
        if not restaurant['is_closed']:
            selected.append(restaurant)
    return selected
```


```python
len(open_restaurants(restaurants)) # 1
open_restaurants(restaurants)[0]['name'] # 'Fork & Fig'
```




    'Fork & Fig'



### Summary

Great!  Through this lab we saw how to pass arguments to functions, multiple arguments to functions, and how to implement functinons with default arguments.
