
def get_num_words(text):
	w_list = text.split()
	return(len(w_list))

def get_char_count(text):
	char_dict = {}
	for i in text:
		if i.lower() in char_dict:
			char_dict[i.lower()] += 1
		else:
			char_dict[i.lower()] = 1
	return char_dict

def sort_on(items):
    return items["num"]

def sorted_dict(char_dict):
	output_list = []
	for i in char_dict:
		tmp = {"char": i, "num": char_dict[i]}
		output_list.append(tmp)
	output_list.sort(reverse=True, key=sort_on)
	return output_list
