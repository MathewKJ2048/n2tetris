# M*n is any number of occurences of M followed by alphanumeric string
# name is a string referring to a location which already exists
# arguments listed as comment
# all instructions start with directive
# general operation: M*n = M*n OP M*n 
# general assignment: M*n = M*n

directive = '-'
terminate = "terminate"
push = "push"    # M*n
pop = "pop"      # M*n  
call = "call"    # name
branch = "branch"    # name M*n OP M*n
inc = "inc"      # M*n
dec = "dec"      # M*n
return_ = "return"
M = "M"
stack = "stack"  # value, specifies starting point of stack
goto = "goto"    # name

less = "<"
less_eq = "<="
great = ">"
great_eq = ">="
eq = "=="
neq = "!="