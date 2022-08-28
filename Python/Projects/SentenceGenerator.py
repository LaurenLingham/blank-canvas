import random

nouns = ["gorilla", "ball", "boat", "dog", "jelly", "bumblebee", "unicorn", "Queen", "magic wand", "genie"]
verbs = ["kicked", "licked", "kissed", "ate", "squashed", "rescued", "cuddled", "painted", "captured", "loved"]
adjectives = ["smelly", "gargantuan", "dopey", "silly", "slippery", "fluffy", "cute", "angry", "spikey", "colourful"]

nounNum = random.randint(0, len(nouns) - 1)
verbNum = random.randint(0, len(verbs) - 1)
adjectiveNum = random.randint(0, len(adjectives) - 1)

nounNum2 = random.randint(0, len(nouns) - 1)
verbNum2 = random.randint(0, len(verbs) - 1)
adjectiveNum2 = random.randint(0, len(adjectives) - 1)

noun = nouns[nounNum]
verb = verbs[verbNum]
adjective = adjectives[adjectiveNum]

noun2 = nouns[nounNum2]
verb2 = verbs[verbNum2]
adjective2 = adjectives[adjectiveNum2]

print("The " + adjective2 + " " + noun + " " + verb + " the " + adjective + " " + noun2 + ".")

userNoun = input("Please enter a Name: ")

print(userNoun + " " + verb2 + " the " + adjective2 + " " + noun + ".")