#https://speakpython.codes/problem-solving/2023/04/29/symbol-balancing.html
print("Input: ")
arrangement = input("")
arrangement = arrangement.replace(' ', '')

symb = {
    "{" : "}",
    "[" : "]",
    "(" : ")",
}
stack = []
inc = 0
miss = None

for i in arrangement:
	if i in symb:
	    stack.append(i)
	    print("Push",i," >> ",stack)
	
	inc +=  1
	
	if i in symb.values():
	    key = [x for x in symb if symb[x] == i]
	    if stack and key[0] in stack:
	        peak = stack.pop()
	        if peak == key[len(key) - 1]:
	            key.pop()
	            print("Pop ",i," >> ",stack)
	            continue
	    miss = key[0]
	    break
	    
if not stack and not miss and inc == len(arrangement):
	print("\nValid Pattern")
else:
	print("\nInvalid Pattern")