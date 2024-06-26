import os
from flask import Flask
from flask_restx import Api
from api.place_api import api as place_api
from api.user_api import api as user_api
from api.review_api import api as review_api
from api.amenity_api import api as amenity_api
from api.country_api import api as country_api
from api.city_api import api as city_api

app = Flask(__name__)
api = Api(app)

# Adding namespaces for each APiRoute
# Example:"http://oussematurki.com/places"
# Example:"http://Goffrane.com/users"
api.add_namespace(place_api, path='/places')
api.add_namespace(user_api, path='/users')
api.add_namespace(review_api, path='/reviews')
api.add_namespace(amenity_api, path='/amenities')
api.add_namespace(country_api, path='/countries')
api.add_namespace(city_api, path='/cities')


if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Run
