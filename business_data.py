import json
import pandas as pd
from collections import Counter


def load_business_data(path):
    # Load business data:
    yelp_businesses = [json.loads(line) for line in open(path)]
    bdata = pd.DataFrame(yelp_businesses)

    one_star_data = bdata[bdata.stars == 1.0]
    one_half_data = bdata[bdata.stars == 1.5]
    two_star_data = bdata[bdata.stars == 2.0]
    two_half_data = bdata[bdata.stars == 2.5]
    three_star_data = bdata[bdata.stars == 3.0]
    three_half_data = bdata[bdata.stars == 3.5]
    four_star_data = bdata[bdata.stars == 4.0]
    four_half_data = bdata[bdata.stars == 4.5]
    five_star_data = bdata[bdata.stars == 5.0]

    # 1 star data

    # First lists extracted from main data
    one_star_reviews = one_star_data.review_count.value_counts()
    one_star_states = one_star_data.state.value_counts()
    one_star_cities = one_star_data.city.value_counts()

    # These lists were all extracted from the Attributes column
    one_star_attributes = one_star_data['attributes']

    all_data = [i.get('Price Range') for i in one_star_attributes]
    one_star_prices = [i for i in all_data if i is not None]

    all_data = [i.get('Takes Reservations') for i in one_star_attributes]
    one_star_reservations = [i for i in all_data if i is not None]

    all_data = [i.get('Accepts Credit Cards') for i in one_star_attributes]
    one_star_cards = [i for i in all_data if i is not None]

    all_data = [i.get('Attire') for i in one_star_attributes]
    one_star_attire = [i for i in all_data if i is not None]

    all_data = [i.get('Delivery') for i in one_star_attributes]
    one_star_delivery = [i for i in all_data if i is not None]

    all_data = [i.get('Wi-Fi') for i in one_star_attributes]
    one_star_wifi = [i for i in all_data if i is not None]

    all_data = [i.get('Good for Kids') for i in one_star_attributes]
    one_star_kids = [i for i in all_data if i is not None]

    # This block extracts a dictionary of the 10 most common categories
    one_star_categories = [j for i in one_star_data['categories'] for j in i]
    one_star_categories_counter = Counter(one_star_categories)
    one_star_common = one_star_categories_counter.most_common(10)
    one_star_common_items = [i for y in one_star_common for i in y]
    one_star_common_keys = one_star_common_items[::2]
    one_star_common_categories = {k: v for k, v in one_star_categories_counter.items() if k in one_star_common_keys}

    # 1.5 star data

    # First lists extracted from main data
    one_half_reviews = one_half_data.review_count.value_counts()
    one_half_states = one_half_data.state.value_counts()
    one_half_cities = one_half_data.city.value_counts()

    # These lists were all extracted from the Attributes column
    one_half_attributes = one_half_data['attributes']

    all_data = [i.get('Price Range') for i in one_half_attributes]
    one_half_prices = [i for i in all_data if i is not None]

    all_data = [i.get('Takes Reservations') for i in one_half_attributes]
    one_half_reservations = [i for i in all_data if i is not None]

    all_data = [i.get('Accepts Credit Cards') for i in one_half_attributes]
    one_half_cards = [i for i in all_data if i is not None]

    all_data = [i.get('Attire') for i in one_half_attributes]
    one_half_attire = [i for i in all_data if i is not None]

    all_data = [i.get('Delivery') for i in one_half_attributes]
    one_half_delivery = [i for i in all_data if i is not None]

    all_data = [i.get('Wi-Fi') for i in one_half_attributes]
    one_half_wifi = [i for i in all_data if i is not None]

    all_data = [i.get('Good for Kids') for i in one_half_attributes]
    one_half_kids = [i for i in all_data if i is not None]

    # This block extracts a dictionary of the 10 most common categories
    one_half_categories = [j for i in one_half_data['categories'] for j in i]
    one_half_categories_counter = Counter(one_half_categories)
    one_half_common = one_half_categories_counter.most_common(10)
    one_half_common_items = [i for y in one_half_common for i in y]
    one_half_common_keys = one_half_common_items[::2]
    one_half_common_categories = {k: v for k, v in one_half_categories_counter.items() if k in one_half_common_keys}

    # 2 star data

    # First lists extracted from main data
    two_star_reviews = two_star_data.review_count.value_counts()
    two_star_states = two_star_data.state.value_counts()
    two_star_cities = two_star_data.city.value_counts()

    # These lists were all extracted from the Attributes column
    two_star_attributes = two_star_data['attributes']

    all_data = [i.get('Price Range') for i in two_star_attributes]
    two_star_prices = [i for i in all_data if i is not None]

    all_data = [i.get('Takes Reservations') for i in two_star_attributes]
    two_star_reservations = [i for i in all_data if i is not None]

    all_data = [i.get('Accepts Credit Cards') for i in two_star_attributes]
    two_star_cards = [i for i in all_data if i is not None]

    all_data = [i.get('Attire') for i in two_star_attributes]
    two_star_attire = [i for i in all_data if i is not None]

    all_data = [i.get('Delivery') for i in two_star_attributes]
    two_star_delivery = [i for i in all_data if i is not None]

    all_data = [i.get('Wi-Fi') for i in two_star_attributes]
    two_star_wifi = [i for i in all_data if i is not None]

    all_data = [i.get('Good for Kids') for i in two_star_attributes]
    two_star_kids = [i for i in all_data if i is not None]

    # This block extracts a dictionary of the 10 most common categories
    two_star_categories = [j for i in two_star_data['categories'] for j in i]
    two_star_categories_counter = Counter(two_star_categories)
    two_star_common = two_star_categories_counter.most_common(10)
    two_star_common_items = [i for y in two_star_common for i in y]
    two_star_common_keys = two_star_common_items[::2]
    two_star_common_categories = {k: v for k, v in two_star_categories_counter.items() if k in two_star_common_keys}

    # 2.5 star data

    # First lists extracted from main data
    two_half_reviews = two_half_data.review_count.value_counts()
    two_half_states = two_half_data.state.value_counts()
    two_half_cities = two_half_data.city.value_counts()

    # These lists were all extracted from the Attributes column
    two_half_attributes = two_half_data['attributes']

    all_data = [i.get('Price Range') for i in two_half_attributes]
    two_half_prices = [i for i in all_data if i is not None]

    all_data = [i.get('Takes Reservations') for i in two_half_attributes]
    two_half_reservations = [i for i in all_data if i is not None]

    all_data = [i.get('Accepts Credit Cards') for i in two_half_attributes]
    two_half_cards = [i for i in all_data if i is not None]

    all_data = [i.get('Attire') for i in two_half_attributes]
    two_half_attire = [i for i in all_data if i is not None]

    all_data = [i.get('Delivery') for i in two_half_attributes]
    two_half_delivery = [i for i in all_data if i is not None]

    all_data = [i.get('Wi-Fi') for i in two_half_attributes]
    two_half_wifi = [i for i in all_data if i is not None]

    all_data = [i.get('Good for Kids') for i in two_half_attributes]
    two_half_kids = [i for i in all_data if i is not None]

    # This block extracts a dictionary of the 10 most common categories
    two_half_categories = [j for i in two_half_data['categories'] for j in i]
    two_half_categories_counter = Counter(two_half_categories)
    two_half_common = two_half_categories_counter.most_common(10)
    two_half_common_items = [i for y in two_half_common for i in y]
    two_half_common_keys = two_half_common_items[::2]
    two_half_common_categories = {k: v for k, v in two_half_categories_counter.items() if k in two_half_common_keys}

    # 3 star data
    # First lists extracted from main data
    three_star_reviews = three_star_data.review_count.value_counts()
    three_star_states = three_star_data.state.value_counts()
    three_star_cities = three_star_data.city.value_counts()

    # These lists were all extracted from the Attributes column
    three_star_attributes = three_star_data['attributes']

    all_data = [i.get('Price Range') for i in three_star_attributes]
    three_star_prices = [i for i in all_data if i is not None]

    all_data = [i.get('Takes Reservations') for i in three_star_attributes]
    three_star_reservations = [i for i in all_data if i is not None]

    all_data = [i.get('Accepts Credit Cards') for i in three_star_attributes]
    three_star_cards = [i for i in all_data if i is not None]

    all_data = [i.get('Attire') for i in three_star_attributes]
    three_star_attire = [i for i in all_data if i is not None]

    all_data = [i.get('Delivery') for i in three_star_attributes]
    three_star_delivery = [i for i in all_data if i is not None]

    all_data = [i.get('Wi-Fi') for i in three_star_attributes]
    three_star_wifi = [i for i in all_data if i is not None]

    all_data = [i.get('Good for Kids') for i in three_star_attributes]
    three_star_kids = [i for i in all_data if i is not None]

    # This block extracts a dictionary of the 10 most common categories
    three_star_categories = [j for i in three_star_data['categories'] for j in i]
    three_star_categories_counter = Counter(three_star_categories)
    three_star_common = three_star_categories_counter.most_common(10)
    three_star_common_items = [i for y in three_star_common for i in y]
    three_star_common_keys = three_star_common_items[::2]
    three_star_common_categories = {k: v for k, v in three_star_categories_counter.items() if
                                    k in three_star_common_keys}

    # 3.5 star data
    # First lists extracted from main data
    three_half_reviews = three_half_data.review_count.value_counts()
    three_half_states = three_half_data.state.value_counts()
    three_half_cities = three_half_data.city.value_counts()

    # These lists were all extracted from the Attributes column
    three_half_attributes = three_half_data['attributes']

    all_data = [i.get('Price Range') for i in three_half_attributes]
    three_half_prices = [i for i in all_data if i is not None]

    all_data = [i.get('Takes Reservations') for i in three_half_attributes]
    three_half_reservations = [i for i in all_data if i is not None]

    all_data = [i.get('Accepts Credit Cards') for i in three_half_attributes]
    three_half_cards = [i for i in all_data if i is not None]

    all_data = [i.get('Attire') for i in three_half_attributes]
    three_half_attire = [i for i in all_data if i is not None]

    all_data = [i.get('Delivery') for i in three_half_attributes]
    three_half_delivery = [i for i in all_data if i is not None]

    all_data = [i.get('Wi-Fi') for i in three_half_attributes]
    three_half_wifi = [i for i in all_data if i is not None]

    all_data = [i.get('Good for Kids') for i in three_half_attributes]
    three_half_kids = [i for i in all_data if i is not None]

    # This block extracts a dictionary of the 10 most common categories
    three_half_categories = [j for i in three_half_data['categories'] for j in i]
    three_half_categories_counter = Counter(three_half_categories)
    three_half_common = three_half_categories_counter.most_common(10)
    three_half_common_items = [i for y in three_half_common for i in y]
    three_half_common_keys = three_half_common_items[::2]
    three_half_common_categories = {k: v for k, v in three_half_categories_counter.items() if
                                    k in three_half_common_keys}

    # 4 star data

    # First lists extracted from main data
    four_star_reviews = four_star_data.review_count.value_counts()
    four_star_states = four_star_data.state.value_counts()
    four_star_cities = four_star_data.city.value_counts()

    # These lists were all extracted from the Attributes column
    four_star_attributes = four_star_data['attributes']

    all_data = [i.get('Price Range') for i in four_star_attributes]
    four_star_prices = [i for i in all_data if i is not None]

    all_data = [i.get('Takes Reservations') for i in four_star_attributes]
    four_star_reservations = [i for i in all_data if i is not None]

    all_data = [i.get('Accepts Credit Cards') for i in four_star_attributes]
    four_star_cards = [i for i in all_data if i is not None]

    all_data = [i.get('Attire') for i in four_star_attributes]
    four_star_attire = [i for i in all_data if i is not None]

    all_data = [i.get('Delivery') for i in four_star_attributes]
    four_star_delivery = [i for i in all_data if i is not None]

    all_data = [i.get('Wi-Fi') for i in four_star_attributes]
    four_star_wifi = [i for i in all_data if i is not None]

    all_data = [i.get('Good for Kids') for i in four_star_attributes]
    four_star_kids = [i for i in all_data if i is not None]

    # This block extracts a dictionary of the 10 most common categories
    four_star_categories = [j for i in four_star_data['categories'] for j in i]
    four_star_categories_counter = Counter(four_star_categories)
    four_star_common = four_star_categories_counter.most_common(10)
    four_star_common_items = [i for y in four_star_common for i in y]
    four_star_common_keys = four_star_common_items[::2]
    four_star_common_categories = {k: v for k, v in four_star_categories_counter.items() if k in four_star_common_keys}

    # 4.5 star data

    # First lists extracted from main data
    four_half_reviews = four_half_data.review_count.value_counts()
    four_half_states = four_half_data.state.value_counts()
    four_half_cities = four_half_data.city.value_counts()

    # These lists were all extracted from the Attributes column
    four_half_attributes = four_half_data['attributes']

    all_data = [i.get('Price Range') for i in four_half_attributes]
    four_half_prices = [i for i in all_data if i is not None]

    all_data = [i.get('Takes Reservations') for i in four_half_attributes]
    four_half_reservations = [i for i in all_data if i is not None]

    all_data = [i.get('Accepts Credit Cards') for i in four_half_attributes]
    four_half_cards = [i for i in all_data if i is not None]

    all_data = [i.get('Attire') for i in four_half_attributes]
    four_half_attire = [i for i in all_data if i is not None]

    all_data = [i.get('Delivery') for i in four_half_attributes]
    four_half_delivery = [i for i in all_data if i is not None]

    all_data = [i.get('Wi-Fi') for i in four_half_attributes]
    four_half_wifi = [i for i in all_data if i is not None]

    all_data = [i.get('Good for Kids') for i in four_half_attributes]
    four_half_kids = [i for i in all_data if i is not None]

    # This block extracts a dictionary of the 10 most common categories
    four_half_categories = [j for i in four_half_data['categories'] for j in i]
    four_half_categories_counter = Counter(four_half_categories)
    four_half_common = four_half_categories_counter.most_common(10)
    four_half_common_items = [i for y in four_half_common for i in y]
    four_half_common_keys = four_half_common_items[::2]
    four_half_common_categories = {k: v for k, v in four_half_categories_counter.items() if k in four_half_common_keys}

    # 5 star

    # First lists extracted from main data
    five_star_reviews = five_star_data.review_count.value_counts()
    five_star_states = five_star_data.state.value_counts()
    five_star_cities = five_star_data.city.value_counts()

    # These lists were all extracted from the Attributes column
    five_star_attributes = five_star_data['attributes']

    all_data = [i.get('Price Range') for i in five_star_attributes]
    five_star_prices = [i for i in all_data if i is not None]

    all_data = [i.get('Takes Reservations') for i in five_star_attributes]
    five_star_reservations = [i for i in all_data if i is not None]

    all_data = [i.get('Accepts Credit Cards') for i in five_star_attributes]
    five_star_cards = [i for i in all_data if i is not None]

    all_data = [i.get('Attire') for i in five_star_attributes]
    five_star_attire = [i for i in all_data if i is not None]

    all_data = [i.get('Delivery') for i in five_star_attributes]
    five_star_delivery = [i for i in all_data if i is not None]

    all_data = [i.get('Wi-Fi') for i in five_star_attributes]
    five_star_wifi = [i for i in all_data if i is not None]

    all_data = [i.get('Good for Kids') for i in five_star_attributes]
    five_star_kids = [i for i in all_data if i is not None]

    # This block extracts a dictionary of the 10 most common categories
    five_star_categories = [j for i in five_star_data['categories'] for j in i]
    five_star_categories_counter = Counter(five_star_categories)
    five_star_common = five_star_categories_counter.most_common(10)
    five_star_common_items = [i for y in five_star_common for i in y]
    five_star_common_keys = five_star_common_items[::2]
    five_star_common_categories = {k: v for k, v in five_star_categories_counter.items() if k in five_star_common_keys}

    # Dictionaries for each level

    one_star = {'review_count': one_star_reviews,
                'states': one_star_states,
                'cities': one_star_cities,
                'prices': one_star_prices,
                'reservations': one_star_reservations,
                'credit_cards': one_star_cards,
                'attire': one_star_attire,
                'delivery': one_star_delivery,
                'wifi': one_star_wifi,
                'kids': one_star_kids,
                'common_categories': one_star_categories}

    one_half = {'review_count': one_half_reviews,
                'states': one_half_states,
                'cities': one_half_cities,
                'prices': one_half_prices,
                'reservations': one_half_reservations,
                'credit_cards': one_half_cards,
                'attire': one_half_attire,
                'delivery': one_half_delivery,
                'wifi': one_half_wifi,
                'kids': one_half_kids,
                'common_categories': one_half_categories}

    two_star = {'review_count': two_star_reviews,
                'states': two_star_states,
                'cities': two_star_cities,
                'prices': two_star_prices,
                'reservations': two_star_reservations,
                'credit_cards': two_star_cards,
                'attire': two_star_attire,
                'delivery': two_star_delivery,
                'wifi': two_star_wifi,
                'kids': two_star_kids,
                'common_categories': two_star_categories}

    two_half = {'review_count': two_half_reviews,
                'states': two_half_states,
                'cities': two_half_cities,
                'prices': two_half_prices,
                'reservations': two_half_reservations,
                'credit_cards': two_half_cards,
                'attire': two_half_attire,
                'delivery': two_half_delivery,
                'wifi': two_half_wifi,
                'kids': two_half_kids,
                'common_categories': two_half_categories}

    three_star = {'review_count': three_star_reviews,
                  'states': three_star_states,
                  'cities': three_star_cities,
                  'prices': three_star_prices,
                  'reservations': three_star_reservations,
                  'credit_cards': three_star_cards,
                  'attire': three_star_attire,
                  'delivery': three_star_delivery,
                  'wifi': three_star_wifi,
                  'kids': three_star_kids,
                  'common_categories': three_star_categories}

    three_half = {'review_count': three_half_reviews,
                  'states': three_half_states,
                  'cities': three_half_cities,
                  'prices': three_half_prices,
                  'reservations': three_half_reservations,
                  'credit_cards': three_half_cards,
                  'attire': three_half_attire,
                  'delivery': three_half_delivery,
                  'wifi': three_half_wifi,
                  'kids': three_half_kids,
                  'common_categories': three_half_categories}

    four_star = {'review_count': four_star_reviews,
                 'states': four_star_states,
                 'cities': four_star_cities,
                 'prices': four_star_prices,
                 'reservations': four_star_reservations,
                 'credit_cards': four_star_cards,
                 'attire': four_star_attire,
                 'delivery': four_star_delivery,
                 'wifi': four_star_wifi,
                 'kids': four_star_kids,
                 'common_categories': four_star_categories}

    four_half = {'review_count': four_half_reviews,
                 'states': four_half_states,
                 'cities': four_half_cities,
                 'prices': four_half_prices,
                 'reservations': four_half_reservations,
                 'credit_cards': four_half_cards,
                 'attire': four_half_attire,
                 'delivery': four_half_delivery,
                 'wifi': four_half_wifi,
                 'kids': four_half_kids,
                 'common_categories': four_half_categories}

    five_star = {'review_count': five_star_reviews,
                 'states': five_star_states,
                 'cities': five_star_cities,
                 'prices': five_star_prices,
                 'reservations': five_star_reservations,
                 'credit_cards': five_star_cards,
                 'attire': five_star_attire,
                 'delivery': five_star_delivery,
                 'wifi': five_star_wifi,
                 'kids': five_star_kids,
                 'common_categories': five_star_categories}

    # Business list of dictionaries for each star level:
    business_data = [one_star, one_half, two_star, two_half, three_star,
                     three_half, four_star, four_half, five_star]

    return business_data
