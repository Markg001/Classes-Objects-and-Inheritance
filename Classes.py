#!/usr/bin/env python3

class person:
    def __init__(self, first="John", last="kimotho", age="95", city="Juja", country="Kenya"):
        self.first = first
        self.last= last
        self.age = age
        self.city = city
        self.country=country
        self.skills= []
        self.organization=[]
    def personal_info(self):
        return f' {self.first} {self.last} is {self.age} years. He lives in {self.city} {self.country}'
    def add_skill(self, skill):
        self.skills.append(skill)
    def add_organization(self,organization):
        self.organization.append(organization)


class student(person):
    pass

class children(person):
    def __init__(self, first="John", last="kimotho", age="95", city="Juja", country="Kenya"):
        self.gender=gender
        super().__init__(first, last, age, city, country)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1= student("Martin", "Irungu", "45", "Kiambu", "Kenya")
s1.add_organization("Marketing")
print(s1.organization)
print(s1.personal_info())
print("\n------------------------------------------------------------")
s2= student("Gladys", "Wamuyu", "67", "Nakuru", "Kenya")
s2.add_organization("Doctor")
print(s2.organization)
print(s2.personal_info())
print("\n------------------------------------------------------------")
p1= person()
p1.add_organization("Developer")
print(p1.organization)
p1.add_skill("HTML")
print(p1.personal_info())
print(p1.skills)
print("\n------------------------------------------------------------")
p2 = person("Mark", "Gitonga", "84", "Nairobi", "Kenya")
p2.add_organization("Security analyist")
print(p2.organization)
p2.add_skill("Python")
print(p2.personal_info())
print(p2.skills)
print("\n------------------------------------------------------------")
p3=person("Allan", "Mbugua", "55", "Kitale", "Kneya")
p3.add_organization("Cybersecurity Engineer")
print(p3.organization)
p3.add_skill("C++")
print(p3.personal_info())
print(p3.skills)
print("\n------------------------------------------------------------")
print("\n------------------------------------------------------------")