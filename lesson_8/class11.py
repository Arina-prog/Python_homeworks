# haytararel studentneri class irenc atributnerov anun tariq mog
#

import functools

class Student:
    def __init__(self, name, old, mog):
        self.name = name
        self.old = old
        self.mog = mog

    def increase_old(self):
        self.old += 1
        return self.old

    def change_name(self, new_name):
        self.name = new_name
        return self.name

    def change_mog(self, new_rating):
        self.mog = new_rating
        return self.mog


class Master(Student):
    def __init__(self, name, old, mog, name_essay, subject_duration):
        Student.__init__(self, name, old, mog)
        self.name_essay = name_essay
        self.subject_duration = subject_duration

    def search_subject(self, subject):
        if subject in self.subject_duration:
            print(subject)
        else:
            print("error")


    def get_longest_sub(self):
        max = 0
        longest_sub = ' '
        for subject in self.subject_duration.keys():
            if self.subject_duration[subject] > max:
                max = self.subject_duration[subject]
                longest_sub = subject

            return (longest_sub, max)

    def search_first_sub(self, simbol):
        found = 0
        numbers1 = list(filter(lambda simbol: simbol in self.subject_duration, self.subject_duration))
        return numbers1


t = Master("ajjh", 25, 86, "OOP jhhjk", {"jhghdf": 25, "hjgd":35})
print(t.get_longest_sub())
t.search_subject("security")
t.search_first_sub("O")

