import random


nouns = ["dispute", "drama", "debate", "nominee", "nomination", "Senator", "unnamed Source", "dictator", "Hitler", "fascist", "tyrant", "Nazi", "President Trump", "Vladimir Putin", "Trump", "Putin", "Drumph","pee-pee", "urine", "golden shower", "leaker", "leak", "cheeto", "President", "Russian", "Kremlin", "Russia", "prostitute", "grifter", "bed", "Obama", "racism"]
verbs = ["explained", "tinkled", "flirted", "touched", "signed", "voted", "betrayed", "lied", "nutted, ""dog whistled", "peed", "urinated", "unload", "leaked", "said", "tweeted", "reported", "soaked", "grifted", "undid", "pinched", "kissed", "sucked", "laughed", "stroked", "dumped", "impeached"]
prepPhrases = ["on top of", "behind", "below", "underneath", "around", "between", "next to", "beneath", "betwixt"]
adverbs = ["when", "while", "slyly", "trecherously", "secretly", "subsequently"]
adjectives = ["racist", "golden", "fluid", "orange", "cheeto-colored", "stupid", "xenophobic", "divisive", "misogynistic", "hateful", "dishonest", "greedy"]

conjunctions = [ "and", "or", "but", "for" , "yet" ]


# adverb noun verb prepphrase adjective noun

def chooseRandomWord(wordSet): 
    return wordSet[random.randint(0,len(wordSet)-1)]


def composeAdverbPrep():
    return chooseRandomWord(adverbs).capitalize() + " " + chooseRandomWord(nouns).capitalize() + " " + chooseRandomWord(verbs).capitalize() + " " + chooseRandomWord(prepPhrases) + " " + chooseRandomWord(adjectives).capitalize() + " " + chooseRandomWord(nouns).capitalize()

def composeSimple():
    return chooseRandomWord(nouns).capitalize() + " " + chooseRandomWord(verbs).capitalize()

def compoundSimple():
    return chooseRandomWord(nouns).capitalize() + " " + chooseRandomWord(verbs).capitalize() + ", " + chooseRandomWord(conjunctions).capitalize() + " "+ chooseRandomWord(nouns).capitalize() + " " + chooseRandomWord(verbs).capitalize()


adjList = []


for i in range(random.randint(0,3)):
    adjList.append(chooseRandomWord(adjectives).capitalize())


def composeHeadline():
    return "Why " + chooseRandomWord(nouns).capitalize() + " " + chooseRandomWord(verbs).capitalize() + " " + chooseRandomWord(prepPhrases) + " " + " ".join(adjList) + " " + chooseRandomWord(nouns).capitalize()

def composeQuestion():
    return "Is " + chooseRandomWord(nouns).capitalize() + " " + chooseRandomWord(prepPhrases) + " a " + chooseRandomWord(adjectives).capitalize() + " " + chooseRandomWord(nouns).capitalize() + "?"


functionArray = [composeSimple, composeAdverbPrep, compoundSimple, composeHeadline, composeAdverbPrep, composeHeadline, compoundSimple]
outfile = open("headlines.txt", "w+")
for i in range(10):
    outfile.write(functionArray[random.randint(0,len(functionArray)-1)]() + "\n") 

print composeQuestion()



