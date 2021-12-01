import os

from pyswip import Prolog

class Rule:
    def __init__(self, text):
        self.text = text

    def create_query(self, text):
        return "advisor:"+text

    def get_result(self):
        d = Prolog()
        file_path = os.path.abspath(__file__)
        edited_path = file_path[:-7].replace("\\", "/")
        d.consult(edited_path + 'advisor.pl')

        print(self.text)
        results = d.query(self.create_query(self.text))

        exp = []
        for result in results:
            exp.append(result)
        return exp

    def add_rule(self):
        f = open('main/advisor.pl', 'a')
        print("*" * 100)
        print(self.text)
        f.write(str(self.text) + "\n"*2)
        f.close()