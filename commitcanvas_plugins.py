import commitcanvas


class subject_min_word_count:
    @commitcanvas.check
    def rule(self,message):
        min_count = 2
        count = len(message.split(" "))
        if count <= min_count:
            return("Commit message must have more than {} words, got: {}".format(min_count,count))

