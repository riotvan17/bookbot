from stats import get_num_words, get_char_count, sorted_dict
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	filepath = sys.argv[1]
	text = get_book_text(filepath)
	outp = sorted_dict(get_char_count(text))
	print(f'''
	   ============ BOOKBOT ============
		Analyzing book found at {filepath}...
		----------- Word Count ----------
		Found {get_num_words(text)} total words
		--------- Character Count -------
		'''
	)
	for i in outp:
		if i['char'].isalpha():
			print(f"{i['char']}: {i['num']}")
	print('============= END ===============')




main()