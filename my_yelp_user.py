# class for retriving data
class MyYelpUser:
    def __init__(self, user):
        self.user = user

    def get_data(self, star, data_attr):
        """get data for the given star number and attribute"""
        index_star = int(star * 2 - 2)
        return self.user[index_star][data_attr]

    def get_data_range(self, star_st, star_ed, data_attr):
        """get data for the given star range and attribute"""
        ret = []
        index_st = int(star_st * 2 - 2)
        index_ed = int(star_ed * 2 - 2)
        for i in range(index_st, index_ed + 1):
            ret.extend(self.user[i][data_attr])
        return ret
