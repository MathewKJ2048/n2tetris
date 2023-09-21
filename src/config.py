sp = "0" # stack pointer address
ra = "1" # return address address
names = {"s":sp,"r":ra,"a":"2","b":"3","c":"4","d":"5","x":"6","y":"7","z":"8"} # reserved for symbolic use
mem = "M"
END = "END" # standard label for terminating program
UID_calls = 0
def get_return_point(func):
    global UID_calls
    UID_calls+=1
    return "return_from_"+func+"_"+str(UID_calls)