with open("test.txt", "w") as my_file:
	my_file.write("TEST")
	if my_file.closed == False:
	    my_file.close()
print my_file.closed

