from user_data import load_user_data
from business_data import load_business_data
from my_yelp_business import MyYelpBusiness
from my_yelp_user import MyYelpUser
import matplotlib.pyplot as plot


def main():
    print("start")
    path_business = "yelp_academic_dataset_business.json"
    path_user = "yelp_academic_dataset_user.json"
    my_yelp = {"business": MyYelpBusiness(load_business_data(path_business)),
               "user": MyYelpUser(load_user_data(path_user))}
    while True:
        t_input = input("Input your command:")
        tokens = t_input.split(" ")
        if len(tokens) < 3:
            break
        if len(tokens) == 3:
            data_for_plot = my_yelp[tokens[0]].get_data(float(tokens[2]), tokens[1])
        else:
            data_for_plot = my_yelp[tokens[0]].get_data_range(float(tokens[2]), float(tokens[3]), tokens[1])
        plot.hist(data_for_plot)
        plot.show()
    print("end")


if __name__ == "__main__":
    main()
