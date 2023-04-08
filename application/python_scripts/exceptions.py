# Creating self defined Exception classes

# To be used for functions were an exact number of parameters shall be passed on but at least one is missing
# To be used when parameters are passed as "None" but are actually needed for your code, such as in the
# method get_url() within class DataProviderService, file data_provider_service.py
class MissingKeyData(Exception):
    pass


# To be used when the given parameters for MySQL queries are not values found within the DDBB
class ValueNotInDDBB(Exception):
    pass
