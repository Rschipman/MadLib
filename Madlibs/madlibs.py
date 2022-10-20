# string concatenation ( aka how to put strings together)
# suppose we want to create a string that says "subscribe to ___"
# youtuber = "Kylie Ying" # some string variable

# a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

#-------------------------------
# Example

# adj = input("Adjective: ")
# emot = input("Emotion: ")
# verb1 = input("Verb: ")
# verb2 = input("Verb: ")
# famousPerson = input("famous person: ")

#madlib = f"Computer programming is so {adj}! It makes me so {emot} all the time, because I love to {verb1}. Stay hydrated and {verb2} like you are {famousPerson}!"

#print(madlib)

#-------------------------------
adverb1 = input("Adverb: ")
speed1 = input("Speed adverb ending in ly: ")
verb1 = input("Verb ending in -ed: ")
verb2 = input("Verb in past tense: ")
verb3 = input("Verb in past tense: ")
noun1 = input("Noun: ")
noun2 = input("Noun: ")
noun3 = input("Noun: ")
noun4 = input("Noun: ")
noun5 = input("Noun: ")

vampMadlib = f' "I see—" said the vampire {adverb1}, and {speed1} he {verb1} across the room towards the {noun1}. For a long time he {verb2} there against the dim light from Divisadero Street and the passing beams of traffic. The boy could see the furnishings of the room more clearly now, the round oak table, the chairs. A {noun2} hung on one wall with a {noun3}. He set his {noun4} on the {noun5} and {verb3}. '

print(vampMadlib)

