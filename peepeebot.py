import random


nouns = ["dictator", "Hitler", "fascist", "tyrant", "Nazi", "President Trump", "Vladimir Putin", "Trump", "Putin", "Drumph","pee-pee", "urine", "golden shower", "leaker", "leak", "cheeto", "President", "Russian", "Kremlin", "Russia", "prostitute", "grifter", "bed", "Obama", "racism"]
verbs = ["tinkled", "flirted", "touched", "signed", "voted", "betrayed", "lied", "nutted, ""dog whistled", "peed", "urinated", "unload", "leaked", "said", "tweeted", "reported", "soaked", "grifted", "undid", "pinched", "kissed", "sucked", "laughed", "stroked", "dumped", "impeached"]
prepPhrases = ["on top of", "behind", "below", "underneath", "around", "between", "next to", "beneath", "betwixt"]
adverbs = ["when", "while", "slyly", "trecherously", "secretly", "subsequently"]
adjectives = ["racist", "golden", "fluid", "orange", "cheeto-colored", "stupid", "xenophobic", "divisive", "misogynistic", "hateful", "dishonest", "greedy"]

conjunctions = [ "and", "or", "but", "for" , "yet" ]


# adverb noun verb prepphrase adjective noun

def chooseRandomWord(wordSet): 
    return wordSet[random.randint(0,len(wordSet)-1)]


def composeAdverbPrep():
    return chooseRandomWord(adverbs).capitalize() + " " + chooseRandomWord(nouns) + " " + chooseRandomWord(verbs) + " " + chooseRandomWord(prepPhrases) + " " + chooseRandomWord(adjectives) + " " + chooseRandomWord(nouns)

def composeSimple():
    return chooseRandomWord(nouns).capitalize() + " " + chooseRandomWord(verbs)

def compoundSimple():
    return chooseRandomWord(nouns).capitalize() + " " + chooseRandomWord(verbs) + " " + chooseRandomWord(conjunctions) + " "+ chooseRandomWord(nouns) + " " + chooseRandomWord(verbs)


adjList = []

for i in range(random.randint(0,3)):
    adjList.append(chooseRandomWord(adjectives))


def composeHeadline():
    return "Why " + chooseRandomWord(nouns) + " " + chooseRandomWord(verbs) + " " + chooseRandomWord(prepPhrases) + " " + " ".join(adjList) + " " + chooseRandomWord(nouns)




functionArray = [composeSimple, composeAdverbPrep, compoundSimple, composeHeadline]
outfile = open("headlines.txt", "w+")
for i in range(10):
    outfile.write(functionArray[random.randint(0,len(functionArray)-1)]() + "\n") 



