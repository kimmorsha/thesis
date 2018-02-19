import indicoio
indicoio.config.api_key = 'YOUR_API_KEY'

# single example
indicoio.sentiment("I love writing code!")

# batch example
indicoio.sentiment([
    "I love writing code!",
    "Alexander and the Terrible, Horrible, No Good, Very Bad Day"
])