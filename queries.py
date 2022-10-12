#!/usr/bin/python3

from relship import Country, City, session


# Create a Country

#country1 = Country(name="Kenya")
#session.add(country1)
#session.commit()

cities = [
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
country = session.query(Country).filter(Country.id==1).first()

#for city in cities:
#    new_city = City(
#            name = city['name'],
#            country=country)
#    session.add(new_city)
#    session.commit() # We havent attached our cities to any county yet

#    print(session.query(Country).all())

cities_by_country = session.query(City).filter(Country.id==1).all()
for city in cities_by_country:
    print("{}: {}   {}".format(city.id, city.name, country.name))
