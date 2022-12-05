def describe_city(city, country='Philippines'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Boracay')
describe_city('Love Lake', 'United Arab Emirates')
describe_city('Tagaytay')