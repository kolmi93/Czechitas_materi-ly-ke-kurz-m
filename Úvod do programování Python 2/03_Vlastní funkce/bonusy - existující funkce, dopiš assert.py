'''
BONUS - k existujícím funkcícm dopiš asserty
'''


# assert ÚKOL Č. 1:

def find_pet(housing_type, activity_level):
    if housing_type == "apartment":
        if activity_level == "busy":
            return "Cat"
        elif activity_level == "calm":
            return "Fish"
    elif housing_type == "house with yard":
        return "Dog"
    elif housing_type == "small apartment":
        return "Hamster"
    
housing_type = input('In which type of housing do you live?\n')
if housing_type == 'apartment':
    activity_level = input('In what kind of enviroment do you live in?\n')

assert housing_type in ("apartment", "house with yard", "small apartment"), "Invalid housing type"
assert activity_level in ("busy", "calm"), "Invalid activity level"

print(find_pet(housing_type, activity_level))


# assert ÚKOL Č. 2:

def plan_vacation(destination_type, preference):
    if destination_type == "beach":
        return "Maldives" if preference == "relaxation" else "Phuket"
    elif destination_type == "mountains":
        return "Swiss Alps" if preference == "adventure" else "Aspen"
    elif destination_type == "city":
        return "Tokyo" if preference == "culture" else "New York City"

destination_type = input('What type of destination do you want? Beach, mountain or city?\n')
preference = input('What do you prefer? Relaxation, adventure or culture?\n')

assert destination_type in ('beach', 'mountains', 'city'), 'Invalid destination type.'
assert preference in ('relaxation', 'culture', 'adventure'), 'Invalid preference.'

print(plan_vacation(destination_type, preference))


# assert ÚKOL Č. 3:

def guess_celebrity(field, descriptor):
    if field == "actor":
        return "Johnny Depp" if "Oscar winner" in descriptor else "Leonardo DiCaprio"
    elif field == "musician":
        return "Michael Jackson" if "pop star" in descriptor else "Elvis Presley"
    elif field == "scientist":
        return "Albert Einstein" if "theory of relativity" in descriptor else "Isaac Newton"

field = input('In which field does the celebrity work in? Actor, musician or scientist?\n')
descriptor = input('Do you want the celebrity be and Oscar winner, pop star or theory of relativity?')

print(guess_celebrity(field, descriptor))

assert field in ('actor', 'musician', 'scientist'), 'Invalid field.'
assert descriptor in ('Oscar winner', 'pop star', 'theory of relativity'), 'Invalid desriptor.'