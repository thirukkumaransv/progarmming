no=input("")
no=no.casefold()
rev=reversed(no)
if list(no) == list(rev):
	print("yes")
else:
	print("no")
