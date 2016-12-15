'''
The final project of DS-GA 1007
NYU Center for Data Science
Authors: Jiaming Dong (jd3405@nyu.edu)
         Daniel Amaranto (da1933@nyu.edu)
         Julie Cachia (jyc436@nyu.edu)

These tests check the data'''

from user_data import load_user_data
from business_data import load_business_data
from my_yelp_business import MyYelpBusiness
from my_yelp_user import MyYelpUser
from my_plot import MyPloter
import unittest

path = r"C:\Users\da1933\Desktop\code"
path_business = path + "\yelp_academic_dataset_business.json"
path_user = path + "\yelp_academic_dataset_user.json"
my_yelp = MyPloter(business_data=MyYelpBusiness(load_business_data(path_business)),
                   user_data=MyYelpUser(load_user_data(path_user)))

class yelpTests(unittest.TestCase):
    
    def test_user_hist_assignments(self):
        user_hist_assignments = ["review_count"]
        self.assertEqual(my_yelp.user_hist, user_hist_assignments)

    def test_business_hist_assignments(self):
        business_hist_assignments = ["review_count", "prices"]
        self.assertEqual(my_yelp.business_hist, business_hist_assignments)

    def test_user_pie_assignments(self):
        user_pie_assignments = ["yelping_since"]
        self.assertEqual(my_yelp.user_pie, user_pie_assignments)
        
    def test_business_pie_assignments(self):
        business_pie_assignments = ["reservations", "delivery", "credit_cards", "states", "cities", "common_categories"]
        self.assertEqual(my_yelp.business_pie, business_pie_assignments)
    
    def test_boxplot_assignments(self):
        boxplot_assignments = ["votedFunny", "votedCool", "votedUseful"]
        self.assertEqual(my_yelp.user_box, boxplot_assignments)


if __name__ == "__main__":
    unittest.main()