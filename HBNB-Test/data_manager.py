from persistence.place_data import Place_Data
from persistence.user_data import User_Data
from persistence.review_data import Review_Data
from persistence.amenity_data import Amenity_Data
from persistence.country_data import Country_Data
from persistence.city_data import City_Data
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.country import Country
from models.city import City


class DataManager:
    def __init__(self):
        self.place_data = Place_Data()
        self.user_data = User_Data()
        self.review_data = Review_Data()
        self.amenity_data = Amenity_Data()
        self.country_data = Country_Data()
        self.city_data = City_Data()

    # ways for Place
    def save_place(self, place_data):
        place = Place(**place_data)
        self.place_data.save(place)
        return place.place_id

    def get_place(self, place_id):
        return self.place_data.get(place_id)

    def update_place(self, place_id, new_data):
        return self.place_data.update(place_id, new_data)

    def delete_place(self, place_id):
        return self.place_data.delete(place_id)

    def get_all_places(self):
        return self.place_data.get_all()

    # ways for User
    def save_user(self, user_data):
        user = User(**user_data)
        self.user_data.save(user)
        return user.user_id

    def get_user(self, user_id):
        return self.user_data.get(user_id)

    def update_user(self, user_id, new_data):
        return self.user_data.update(user_id, new_data)

    def delete_user(self, user_id):
        return self.user_data.delete(user_id)

    def get_all_users(self):
        return self.user_data.get_all()

    # ways for Review
    def save_review(self, review_data):
        review = Review(**review_data)
        self.review_data.save(review)
        return review.review_id

    def get_review(self, review_id):
        return self.review_data.get(review_id)

    def update_review(self, review_id, new_data):
        return self.review_data.update(review_id, new_data)

    def delete_review(self, review_id):
        return self.review_data.delete(review_id)

    def get_all_reviews(self):
        return self.review_data.get_all()

    # ways for Amenity
    def save_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_data.save(amenity)
        return amenity.amenity_id

    def get_amenity(self, amenity_id):
        return self.amenity_data.get(amenity_id)

    def update_amenity(self, amenity_id, new_data):
        return self.amenity_data.update(amenity_id, new_data)

    def delete_amenity(self, amenity_id):
        return self.amenity_data.delete(amenity_id)

    def get_all_amenities(self):
        return self.amenity_data.get_all()

    # ways for Country
    def save_country(self, country_data):
        country = Country(**country_data)
        self.country_data.save(country)
        return country.country_id

    def get_country(self, country_id):
        return self.country_data.get(country_id)

    def update_country(self, country_id, new_data):
        return self.country_data.update(country_id, new_data)

    def delete_country(self, country_id):
        return self.country_data.delete(country_id)

    def get_all_countries(self):
        return self.country_data.get_all()

    # ways for City
    def save_city(self, city_data):
        city = City(**city_data)
        self.city_data.save(city)
        return city.city_id

    def get_city(self, city_id):
        return self.city_data.get(city_id)

    def update_city(self, city_id, new_data):
        return self.city_data.update(city_id, new_data)

    def delete_city(self, city_id):
        return self.city_data.delete(city_id)

    def get_all_cities(self):
        return self.city_data.get_all()
