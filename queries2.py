#!/usr/bin/python3

from relship2 import Country, City, session


# Create a Country

#country1 = Country(name="Kenya")
#session.add(country1)
#session.commit()

#country2 = Country(name="Nigeria")
#session.add(country2)
#session.commit()

cities1 = [
    {
        "name": "Nairobi"
    },
    {
        "name":	"Mombasa"
    },
    {
        "name":	"Nakuru"
    },
    {
        "name":	"Kisumu"
    },
]

cities2 = [
    {
        "name": "Lagos"
    },
    {
        "name": "Abuja"
    },
    {
        "name": "Port Harcourt"
    },
    
]
country1 = session.query(Country).filter(Country.id==1).first()
#print(country)
#for city in cities2:
#    new_city = City(
#            name = city['name'],
#            country=country)
#    session.add(new_city)
#    session.commit() # We havent attached our cities to any county yet

 #   print(session.query(Country).all())

cities_by_country1 = session.query(City).filter(Country.id==1).all()
for city in cities_by_country1:
    print("{}: {}".format(city.id, city.name))


#delete an entry
del_country = session.query(Country).filter(Country.id==2).first()
session.delete(del_country)
session.commit()

cities = session.query(City).all()
for city in cities:
    print("{}: {}".format(city.id, city.name))
