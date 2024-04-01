'''
BONUS - podle asertů dopiš vlastní funkci
'''


# ÚKOL Č. 1:
# Goal: Define a function that tells a joke based on a given category.

def tell_joke(choice):
    if choice == 'dad':
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif choice == 'school':
        return "Why did the math book look sad? Because it had too many problems."
    elif choice == 'animal':
        return "What do you call a fish with no eyes? Fsh!"

choice = input('Choose a topic of a joke that you wanna hear: dad, school or animal:\n')
print(tell_joke(choice))

# Testing the function with assertions
assert tell_joke("dad") == "Why don't scientists trust atoms? Because they make up everything!", 'Invalid joke for category "dad".'
assert tell_joke("school") == "Why did the math book look sad? Because it had too many problems.", 'Invalid joke for category "school".'
assert tell_joke("animal") == "What do you call a fish with no eyes? Fsh!", 'Invalid joke for category "animal".'


# ÚKOL Č. 2:
# Goal: Define a function that suggests a movie based on the user's mood.

def choose_movie(choice):
    if choice == 'happy':
        return "You should watch a comedy like 'The Hangover'!"
    elif choice == 'sad':
        return "Why not watch a feel-good movie like 'Forrest Gump'?"
    elif choice == 'excited':
        return "You're in the mood for action! How about 'The Avengers'?"
    
choice = input('What´s your mood right now? happy, sad or excited?\n')
print(choose_movie(choice))

# Asserts:
assert choose_movie("happy") == "You should watch a comedy like 'The Hangover'!", 'Invalid response for category "happy".'
assert choose_movie("sad") == "Why not watch a feel-good movie like 'Forrest Gump'?", 'Invalid response for category "sad".'
assert choose_movie("excited") == "You're in the mood for action! How about 'The Avengers'?", 'Invalid response for category "excited".'


# ÚKOL Č. 3:
# Goal: Define a function that recommends a type of food based on the weather.

def recommend_food(choice):
    if choice == 'sunny':
        return 'BBQ'
    elif choice == 'rainy':
        return 'Soup'
    elif choice == 'snowy':
        return "Mac and Cheese"

choice = input('What´s the weather like today? sunny, rainy or snowy?\n')
print(recommend_food(choice))

# Asserts:
assert recommend_food("sunny") == "BBQ", 'Invalid response for category "sunny".'
assert recommend_food("rainy") == "Soup", 'Invalid response for category "rainy".'
assert recommend_food("snowy") == "Mac and Cheese", 'Invalid response for category "snowy".'