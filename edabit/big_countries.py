"""
A country can be said as being big if it is:

    Big in terms of population
    Big in terms of area

Add to the Country class so that it contains the attribute is_big. Set it to True if either criteria are met:

    Population is greater than 250 million
    Area is larger than 3 million square km

Also, create a method which compares a country's population density to another country object.
Return a string in the following format: {country} has a {smaller / larger} population density than {other_country}
Examples

australia = Country('Australia', 23545500, 7692024)
andorra = Country('Andorra', 76098, 468)

australia.is_big ➞ True

andorra.is_big ➞ False

andorra.compare_pd(australia) ➞ 'Andorra has a larger population density than Australia'

Notes

    Population density is calculated by diving the population by the area.
    Area is given in square km.
"""
import unittest


class Country:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.population > 250000000 or self.area > 3000000
        self.population_density = self.population / self.area

    def compare_pd(self, other):
        if self.population_density > other.population_density:
            message = self.name + ' has a larger population density than ' + other.name
        else:
            message = self.name + ' has a smaller population density than ' + other.name
        return message


class CountryTest(unittest.TestCase):

    def setUp(self):
        self.australia = Country('Australia', 23545500, 7692024)
        self.andorra = Country('Andorra', 76098, 468)
        self.big_by_area = Country('BigByArea', 76098, 4000000)

    def test_country_is_big_by_population_return_true(self):
        self.assertEqual(self.australia.is_big, True)

    def test_country_is_big_by_area_return_true(self):
        self.assertEqual(self.big_by_area.is_big, True)

    def test_country_is_big_return_false(self):
        self.assertEqual(self.andorra.is_big, False)

    def test_compare_pd_obj_other(self):
        self.assertEqual(
            self.andorra.compare_pd(self.australia), 'Andorra has a larger population density than Australia'
        )

    def test_compare_pd_other_obj(self):
        self.assertEqual(
            self.australia.compare_pd(self.andorra), 'Australia has a smaller population density than Andorra'
        )

    def test_population_density(self):
        ret_value = self.australia.population_density
        self.assertAlmostEqual(3.06102789, ret_value)


if __name__ == '__main__':
    unittest.main()
