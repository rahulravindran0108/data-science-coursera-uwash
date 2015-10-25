import sys
import json

def hw():
    afinnfile = open("AFINN-111.txt")
    scores = {}
    for line in afinnfile:
    	term, score = line.split("\t")
    	scores[term] =  int(score)
    print scores.items()

def lines(fp):
    print str(len(fp.readlines()))

def score_tweet(tweet):

	scores = {}

	#print tweet

	afinnfile = open("AFINN-111.txt")

	scoreIndividual = 0

	for line in afinnfile:
		term, score = line.split("\t")
		scores[term] = int(score)

	for x in tweet.split():

		if x in scores:
			scoreIndividual += scores[x]
		else:
			scoreIndividual += 0

   	return scoreIndividual
   			


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    for lines in tweet_file:
    	line = json.loads(lines)
        if(len(line) > 10):
    	   print score_tweet(line["text"])
    	#break

if __name__ == '__main__':
    main()
