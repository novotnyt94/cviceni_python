class capitalize:
	@property
	def name(self):
		return "Capitalize"

	def process(self, text):
	    new_text = []
	    #walk through given string and make capitalization
	    do_capitalize = True #we want to capitalize the first letter
	    for c in text:
	        #make capitalization of first letter of word
	        if do_capitalize and c.isalpha():
	            new_text.append(c.upper())
	            do_capitalize = False
	        #otherwise, copy the character
	        else:
	            new_text.append(c)
	            #reset capitalization on whitespace
	            if c.isspace():
	                do_capitalize = True
	    return "".join(new_text)
