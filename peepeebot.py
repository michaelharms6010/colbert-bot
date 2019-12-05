import random

## Todos:
# Add hearsay format
# Add a/an/the and article handling
# Expand adjectives
# Expand Adverbs

nouns = ["bombshell", "tweet", "twitter", "calls for impeachment", "witness", "China", "trade war", "House speaker", "diplomat", "whistleblower", "dispute", "drama", "debate", "nominee", "nomination", "Senator", "unnamed Source", "dictator", "Hitler", "fascist", "tyrant", "Nazi", "President Trump", "Vladimir Putin", "Trump", "Putin", "Drumph","pee-pee", "urine", "golden shower", "leaker", "leak", "cheeto", "President", "Russian", "Kremlin", "Russia", "prostitute", "grifter", "bed", "Obama", "racism"]
verbs = ["lied", "incited", "lashed out", "will testify", "pushed out", "raged", "explained", "tinkled", "flirted", "touched", "signed", "voted", "betrayed", "lied", "dog whistled", "blew", "nutted", "peed", "urinated", "unload", "leaked", "said", "tweeted", "reported", "soaked", "grifted", "undid", "pinched", "kissed", "sucked", "laughed", "stroked", "dumped", "impeached"]
prepPhrases = ["without the knowledge of", "by", "within", "among", "on top of", "behind", "below", "underneath", "around", "between", "next to", "beneath", "betwixt"]
adverbs = ["impulsively", "racistly", "when", "while", "slyly", "trecherously", "secretly", "subsequently"]
adjectives = ["clandestine" , "unnamed", "shocking", "problematic", "offensive", "impulsive", "unhinged", "racist", "golden", "orange", "cheeto-colored", "stupid", "xenophobic", "divisive", "misogynistic", "hateful", "dishonest", "greedy"]

conjunctions = [ "and", "or", "but", "for" , "yet" ]
questionWords= ["what", "why", "when", "how"]
sources = ["Veteran CIA Agent", "Intelligence Community", "whistleblower", "Unnamed Source", "Anonymous Source", "Senator", "Congressman", "Congresswoman", "Veteran Journalist", "Veteran", "Intelligence Official"]

# adverb noun verb prepphrase adjective noun

def chooseRandomWord(wordSet): 
    return wordSet[random.randint(0,len(wordSet)-1)]


def composeAdverbPrep():
    return chooseRandomWord(adverbs).title() + " " + chooseRandomWord(nouns).title() + " " + chooseRandomWord(verbs).title() + " " + chooseRandomWord(prepPhrases) + " " + chooseRandomWord(adjectives).title() + " " + chooseRandomWord(nouns).title()

def composeSimple():
    return chooseRandomWord(nouns).title() + " " + chooseRandomWord(verbs).title()

def compoundSimple():
    return chooseRandomWord(nouns).title() + " " + chooseRandomWord(verbs).title() + ", " + chooseRandomWord(conjunctions).title() + " "+ chooseRandomWord(nouns).title() + " " + chooseRandomWord(verbs).title()
def sourcedSimple():
    return chooseRandomWord(nouns).title() + " " + chooseRandomWord(verbs).title() + ", says " + chooseRandomWord(sources).title()


adjList = []


for i in range(random.randint(0,3)):
    adjList.append(chooseRandomWord(adjectives).title())


def composeHeadline():
    return "Why " + chooseRandomWord(nouns).title() + " " + chooseRandomWord(verbs).title() + " " + chooseRandomWord(prepPhrases) +" " + " ".join(adjList) + " " + chooseRandomWord(nouns).title()

def composeQuestion():
    return "Is " + chooseRandomWord(nouns).title() + " " + chooseRandomWord(prepPhrases) + " a " + chooseRandomWord(adjectives).title() + " " + chooseRandomWord(nouns).title() + "?"


functionArray = [sourcedSimple, composeQuestion, composeSimple, composeAdverbPrep, compoundSimple, composeHeadline, composeAdverbPrep, composeHeadline, compoundSimple]
outfile = open("headlines.txt", "w+")
for i in range(1000):
    outfile.write(functionArray[random.randint(0,len(functionArray)-1)]() + "\n") 


