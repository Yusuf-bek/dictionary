import os

class Dictionary:

	def __init__(self):
		self.new_word_en = None
		self.new_word_uz = None

	def entrance(self):
		self.show_text()
		options = '1234'
		option = input(": ").strip()

		while option not in options:
			self.show_text()
			option = input("Invalid input. Enter only [1, 2, 3, 4]: ").strip()

		if option == options[0]:
			self.add_new_word()
		elif option == options[1]:
			self.show_words()
		elif option == options[2]:
			self.search_word()
		elif option == options[3]:
			self.quit()

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




	def show_words(self):
		print("Show words")


	def search_word(self):
		print("Search word")


	def quit(self):
		print("Quit")


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


en_uz = Dictionary()
en_uz.entrance()

