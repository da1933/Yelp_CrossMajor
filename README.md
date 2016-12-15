
# Exploratory Visualizations Using Yelp Data Based on Star Ratings

In this project, we aim to analyze a [Yelp Dataset](https://www.yelp.com/academic_dataset) by looking at business-based and user-based factors according to star-ratings. The user will be able to specify which factors to visualize for what average star rating, and the program will output appropriate graphs (pie charts or histograms) to visualize the specified data.

## Variables



Business | User 
--- | --- | 
`reservations`: Whether or not the business takes reservations| `review_count`: The number of reviews a user has posted
`delivery`: Whether or not the business delivers | `yelping_since`: The year the user started yelping
`credit_cards`: Whether or not the business accepts credit cards | `voted_useful`: The number of times the user's reviews have been voted useful by other users
`states`: The state in which this business is located | `voted_funny`: The number of times the user's reviews have been voted funny by other users
`cities`: The city in which this business is located | `voted_cool`: The number of times the user's reviews have been voted cool by other users
`common_categories`: Business category (e.g., nightlife, fast food)| 
`review_count`: The number of reviews the business received | 
`prices`: The price category of the business |


* For each of the **businesses**, the average star rating (1-5) refers to the average rating they *received*.
* For each of the **users**, the average star rating (1-5) refers to the average rating the user *gave*. 

## Getting Started

Beginning with Github (https://github.com/djasmine/Yelp_CrossMajor), clone the directory using this link: https://github.com/djasmine/Yelp_CrossMajor.git

Into your Terminal command line, enter the following: 

```
cd ./Yelp_CrossMajor
```

To run the program, enter:
```
python main.py
```

You will then be asked to: 

<img style="float: left;" src="https://dl.dropboxusercontent.com/u/105303727/Input%20Your%20Command.png">.
___

You will define 3 parameters:

1. Refer to the table above and decide whether you are interested in `business` or `user` variables
2. Find the label of the specific variable you are interested in (e.g., `delivery`, `yelping_since`)
3. Determine what average star rating you want to filter by (e.g., `3.5`). This can also be a range: The input `2` `3` would filter businesses or users with an average of anywhere between 2 - 3 stars. 

___
### Example Input #1:
```
business delivery 3
```
The above input will generate a pie chart representing the proportion of businesses with an average star rating of 3 that deliver ("True") or don't deliver ("False").

![Sample Output](https://dl.dropboxusercontent.com/u/105303727/Business%20Delivery.png "Business Delivery")

### Example Input #2:
```
user yelping_since 4 5
```
The above input will generate a pie chart representing when users who gave average ratings of 4-5 stars began Yelping, by year.

![Sample Output](https://dl.dropboxusercontent.com/u/105303727/Yelping%20Since.png "Yelping Since")


___
In order to exit the program, simply enter `finish` into the command line.


___

## Authors

* **Daniel Amaranto** - *da1933@nyu.edu*
* **Jiaming Dong** - *jd3405@nyu.edu*
* **Julie Cachia** - *jyc436@nyu.edu*




```python

```
