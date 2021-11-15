import os

from pyswip import Prolog


class Searcher:
    def __init__(self, inp_age, inp_money, inp_family, inp_location, inp_likesfastcars):
        self.inp_age = inp_age
        self.inp_money = inp_money
        self.inp_family = inp_family
        self.inp_location = inp_location
        self.inp_likesfastcars = inp_likesfastcars

    def create_query(self, age, money, family, location, likesfastcars):
        return "advisor:is_suitable_car(client(%s, %s, %s, %s, %s), Car)." % (age, money, family, location,
                                                                              likesfastcars)

    def get_result(self):
        print(self.inp_age, self.inp_money, self.inp_family, self.inp_location,
              self.inp_likesfastcars)
        d = Prolog()
        file_path = os.path.abspath(__file__)
        edited_path = file_path[:-9].replace("\\", "/")
        d.consult(edited_path + 'advisor.pl')

        res = d.query(self.create_query(self.inp_age, self.inp_money, self.inp_family, self.inp_location,
                                   self.inp_likesfastcars))
        total = {}
        for r in res:
            car_name = r["Car"]
            image = 'images/'+ r["Car"]+".jpg"
            total.update({car_name: image})
        return total


    age_choices = [
            ("young", "young"),
            ("mid", "mid"),
            ("old", "old")
    ]


    money_choices=[
        ("poor","poor"),
        ("average","average"),
        ("rich","rich")
    ]

    family_choices=[
        ("single","single"),
        ("married","married")
        ]

    location_choice = [
        ("smallcity", "smallcity"),
        ("bigcity", "bigcity"),
        ("village", "village")
    ]


    likesfastcars_choice = [
        ("dontcare", "dontcare"),
        ("yes", "yes")
    ]


