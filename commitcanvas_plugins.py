import commitcanvas


class min_length:
    @commitcanvas.hookimpl
    def rule(self,message):
        min_count = 2
        count = len(message.split(" "))
        if count <= min_count:
            return("Commit must have more than 2 words, got: {}".format(count)) 

class plug1:
    @commitcanvas.hookimpl
    def rule(self,message:str):
        pass