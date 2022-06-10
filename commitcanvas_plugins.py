import commitcanvas
import textblob
# import pandas as pd

# s = pd.Series([1, 3, 5, 6, 8])
# print(s)

def helper(input):
    return(input)
    
class subject_min_word_count:
    @commitcanvas.check
    def rule(self,message):
        min_count = 2
        count = len(message.split(" "))
        if count <= min_count:
            return("Commit message must have more than {} words, got: {}".format(min_count,count))


class subject_start_verb:
    @commitcanvas.check
    def rule(self,message):
        blob = textblob.TextBlob(message)
        if blob.tags[0][1] not in "VB, NNP":
            return("Commit message must start with word in imperative")

