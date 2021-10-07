import os

class Dictionary:

	def __init__(self):
		self.new_word_en = None
		self.new_word_uz = None

	def add_new_word(self):
		new_word = input("Input new english word: ").strip().lower()
		while not new_word.isalpha():
			self.clear_everything()
			print("Invalid input. Input only should be letters[a-z] and not be an empty")
			new_word = input("Input new english word: ").strip().lower()

		new_word_translate = input('Input translation of word: ').strip().lower()
		while not new_word_translate.isalpha():
			self.clear_everything()
			print("Invalid input. Input only should be letters[a-z] and not be an empty")
			new_word_translate = input('Input translation of word: ').strip().lower()

		self.new_word_en = new_word
		self.new_word_uz = new_word_translate

	def show_words(self):
		pass


	def search_word(self):
		pass


	def quit(self):
		pass


	def show_text(self):
		print("""

		Welcome to dicrionary!
		_________________________________________

		English - Uzbek dictionary

		Choose:

			1. Add new word to dictionary;
			2. See words inside the dictionary;
			3. Search;
			4. Quit;


		_________________________________________
		""")

	@staticmethod
	def clear_everything():
		os.system("clear")