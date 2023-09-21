# M*n is any number of occurances of M followed by alphanumeric string
# name is a string referring to a location which already exists
# arguments listed as comment
# all instructions start with directive
# general operation: M*n = M*n OP M*n has no keyword (for brevity)
# general assignment: M*n = M*n has no keyword (for brevity)

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

less = "<"
less_eq = "<="
great = ">"
great_eq = ">="
eq = "=="
neq = "!="