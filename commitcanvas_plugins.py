import commitcanvas


class subject_min_word_count:
    @commitcanvas.check
    def rule(self,message):
        min_count = 2
        count = len(message.split(" "))
        if count <= min_count:
            return("Commit message must have more than {} words, got: {}".format(min_count,count))

# class subject_capital_letter:
#     @commitcanvas.check
#     def rule(self,message:str):
#         """Subject line of commit message starts with capital letter."""
#         if message[0].isupper():
#             return("Subject must start with lower case letter") 
