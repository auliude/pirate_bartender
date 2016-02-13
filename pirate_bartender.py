import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def enter_preference():
    preferences = {}
    for flavor,question in questions.items():
        print (question)
        preferences [flavor] = input() in ["y", "yes", "aye", "ye"]
        print ("Got ye!")
        print ("")
    return preferences
   
def recommended_ingredients(preferences):    
    drink = []
    for added_ingredient, preference in preferences.items():
        if preference == True:
            drink.append(random.choice(ingredients[added_ingredient]))
        else:
            pass
    return drink
    
def main():
    preferences = enter_preference()
    drink = recommended_ingredients(preferences)
    print ("Aye, hearing that ye likers something:")
    for taste, preference in preferences.items():
        if preference == True:
            print (taste)
        else:
            pass
    print ("")
    print ("Here ye swishin' concoction-")
    for ingredient in drink:
        print ("Thar be a {}".format(ingredient))
    

if __name__ == "__main__":
    main()