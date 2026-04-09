import itertools 
def is_tautology(expr):  
vars_ = sorted(c for c in expr if 'a' <= c <= 'z')  
if not vars_:  
return bool(eval(expr)) 
for vals in itertools.product([True, False], repeat=len(vars_)): 
    env = dict(zip(vars_, vals)) 
    if not eval(expr, {}, env): 
        return False 
return True 
  
if name == "main": tests = [ "(p or not p)", 
 "(p and not p)", 
 "(not (p and not q) or q)", 
 "(not p or q) or (not q or p)" 
 ] 
for t in tests: 
    print(f"Is '{t}' a tautology? {is_tautology(t)}")
