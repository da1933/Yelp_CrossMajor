from user_data import load_user_data
from business_data import load_business_data
from my_yelp_business import MyYelpBusiness
from my_yelp_user import MyYelpUser
import matplotlib.pyplot as plot



def main():
    print("Loading data...")
    path_business = "yelp_academic_dataset_business.json"
    path_user = "yelp_academic_dataset_user.json"
    my_yelp = {"business": MyYelpBusiness(load_business_data(path_business)),
               "user": MyYelpUser(load_user_data(path_user))}
    
    inputErrorMessage = "\nThis program takes three inputs.\n 1) Choose 'user' or 'business'\n" + \
                    " 2) Choose a feature from the instructions.\n" + \
                    " 3) Choose one of these star level to analyze:\n" + \
                    "    1   1.5   2   2.5   3   3.5   4   4.5   5\n" + \
                    " E.g. 'business prices 2.5'\nType 'features' for more information."
                  
    while True:
        try:
            t_input = input("Input your command:")
        except KeyboardInterrupt:
            print(inputErrorMessage)
        
        try:
            if t_input == 'finish':
                break
            else:
                tokens = t_input.split(' ')
                if len(tokens) == 3:
                    data_for_plot = my_yelp[tokens[0]].get_data(float(tokens[2]), tokens[1])
                else:
                    data_for_plot = my_yelp[tokens[0]].get_data_range(float(tokens[2]), float(tokens[3]), tokens[1])
                plot.hist(data_for_plot)
                plot.show()        
        
        except IndexError:
            print(inputErrorMessage)
        except UnboundLocalError:
            print(inputErrorMessage)
        except TypeError:
            print(inputErrorMessage)
        except ValueError:
            print(inputErrorMessage)
        except KeyError:
            print(inputErrorMessage)
    print("Thank you!")


if __name__ == "__main__":
    main()
