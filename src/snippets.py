import config
import syntax

def __parse(M): # returns [depth,location]
    id = M.rfind(syntax.M)
    location = M[id+1:len(M)]
    print("parse"+M+":"+str(id+1)+","+location)
    if not location[0].isdigit():
        location = config.names[location]
    return id+1, location

def __load(M): # puts M into A, without using D
    depth, location = __parse(M)
    code = "\n@"+location
    for i in range(depth):
        code = code+"\nA = M"
    return code

def __save(): # saves value of A into D
    return "\nD = A"

def __store(M): # puts D into M, without using anything else
    depth, location = __parse(M)
    if depth == 0:
        return "ERROR with "+M
    code = "\n@"+location
    for i in range(depth-1):
        code = "\nA = M"
    code = code+"\nM = D"
    return code

def goto(name):
    return "\n@"+name+"\n0 ; JMP"

def general_operation(MD, MS1, OP, MS2):
    return "\n// "+MD+" = "+MS1+" "+OP+" "+MS2+__load(MS1)+__save()+__load(MS2)+"\nD = D "+OP+" A"+__store(MD)

def general_assignment(MD, MS):
    return "\n// "+MD+" = "+MS+__load(MS)+__save()+__store(MD)

def push(M): # loads M into the stack
    SP = syntax.M+config.sp
    MSP = syntax.M+config.sp
    return "//push "+M+" into stack"+__load(M)+__save()+__store(MSP)+inc(SP)

def branch(name,ML,OP,MR):
    operations = {syntax.less:"JLT",syntax.less_eq:"JLE",syntax.great:"JGT",syntax.great_eq:"JGE",syntax.eq:"JEQ",syntax.neq:"JNE"}
    return "// branch to "+name+" if "+ML+OP+MR+"\n"+__load(ML)+__save()+__load(MR)+"\nD = D - A\n@"+name+"\n0 ; "+operations[OP]

def pop(M): # pops and puts value into M
    SP = syntax.M+config.sp
    MSP = syntax.M+config.sp
    return "//pop stack into "+M+__load(MSP)+save()+__store(M)+dec(SP)

def terminate():
    return  "\n// terminate the program"+goto(config.END)

def return_snippet():
    return "\n// return to calling function\n@"+config.ra+"\nA = M\n0 ; JMP"

def inc(M):
    return "\nincrement "+M+load(M)+"\n@"+"\nD = D + A"+store(M)
    pass

def dec(M):
    return "\ndecrement "+M+load(M)+"\n@"+"\nD = D - A"+store(M)
    pass

def call(func):
    RA = config.get_return_point(func)
    return "\n// function call to "+func+"\n@"+RA+__save()+"\n@"+config.ra+"\nM = D\n@"+func+"\n0 ; JMP\n("+RA+")"


def stack(start):
    return "\n// set start of stack as address "+start+"\n@"+start+__save()+"\n@"+config.sp+"\nM = D"