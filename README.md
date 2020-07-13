# random_ideas

A collection of anything and everything

warframe_market_api:
  * Connects to warframe market api to obtain a list of all items on the market, filters them based on user input
  * Creates a quick line chart to show the 90 day trend in average price sold per day
  * User input can be any string, the function will look to match all individual words typed. For example, an input of "Loki Set" will only retrieve a graph of "loki_prime_set", whereas an input of "Loki Prime" will retrieve "loki_prime_set" and all components as they are "loki_prime_helmet".
