# The final project of DS-GA 1007
# NYU Center for Data Science
# Authors: Jiaming Dong (jd3405@nyu.edu)
#          Daniel Amaranto (da1933@nyu.edu)
#          Julie Cachia (jyc436@nyu.edu)
#
# The main program
# To run the project, simply type "python main.py".
# Note that the project is written in Python 3.5.


from user_data import load_user_data
from business_data import load_business_data
from my_yelp_business import MyYelpBusiness
from my_yelp_user import MyYelpUser
from my_plot import MyPloter
from errors import *


def main():
    print("Loading data...")
    path = "/Users/JiamingDong/Downloads/yelp/"
    path_business = path + "yelp_academic_dataset_business.json"
    path_user = path + "yelp_academic_dataset_user.json"
    my_yelp = MyPloter(business_data=MyYelpBusiness(load_business_data(path_business)),
                       user_data=MyYelpUser(load_user_data(path_user)))

    inputErrorMessage = "\nThis program takes three inputs.\n 1) Choose 'user' or 'business'\n" + \
                        "2) Choose a feature from the instructions.\n" + \
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
                    my_yelp.plot(tokens[0], tokens[1], float(tokens[2]))
                else:
                    if len(tokens) == 4:
                        my_yelp.plot(tokens[0], tokens[1], float(tokens[2]), float(tokens[3]))
                    else:
                        raise TokenNumberInvalidException
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
        except AttributeNotFoundException:
            print(inputErrorMessage)
        except TokenNumberInvalidException:
            print(inputErrorMessage)
    print("Thank you!")


if __name__ == "__main__":
    main()
