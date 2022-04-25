import commitcanvas


class min_length:
    @commitcanvas.hookimpl
    def rule(self,message):
        min_count = 2
        count = len(message.split(" "))
        if count <= min_count:
            return("Commit must have more than 2 words, got: {}".format(count)) 

class max_length:
    @commitcanvas.hookimpl
    def rule(self,message):
        max_count = 100
        count = len(message)
        if count >= 100:
            return("Commit must have less than 100 characters, got: {}".format(count)) 