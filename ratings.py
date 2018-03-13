"""Restaurant rating lister."""


def get_restaurant_scores(filename):
    data = open(filename)
    restaurant_scores = {}
    user_restaurant = raw_input("What is your favorite restaurant? ")
    user_rating = raw_input("What is your rating for this restaurant? ")
    for line in data:
        words = line.strip()
        name, rating = words.split(":")
        #sorted_restaurant_name_rating = sorted(restaurant_name_rating)
        restaurant_scores[name] = rating
        restaurant_scores[user_restaurant] = user_rating
    #print restaurant_scores
    for name, rating in sorted(restaurant_scores.items()):
        print "{} is rated at {}".format(name, rating)
         
    

           #restaurant_scores[word] = restaurant_scores.get(word, 0)
    #print restaurant_scores 

    data.close()

get_restaurant_scores("scores.txt")
