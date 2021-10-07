import os
import mysql.connector

mydb = mysql.connector.connect(
			host='localhost',
			user='Abdulaziz',
			password='123123123',
			database='words'
		)

mycursor = mydb.cursor()


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

		self.save_to_database(new_word, new_word_translate)



	def show_words(self):
		pass


	def search_word(self):
		en_or_uz = input("""
Input:  1 -> uz - en
	2 -> en - uz
>>> """).strip()
		opt = ['1', '2']
		while en_or_uz not in opt:
			self.clear_everything()
			print("Invalid input. You can input only 1 or 2!")
			en_or_uz = input("""
Input:  1 -> uz - en
	2 -> en - uz
>>> """).strip()

		if en_or_uz == opt[0]:
			self.clear_everything()
			search_word = input("Enter the word you are searching: ").strip().lower()
			while not search_word.isalpha():
				self.clear_everything()
				print("Invalid input. Try again.")
				search_word = input("Enter the word you are searching: ").strip().lower()

			mycursor.execute(f"select english from table_words where uzbek='{search_word}'")
			prt = mycursor.fetchall()
			print(prt[0][0])

		else:
			self.clear_everything()
			search_word = input("Enter the word you are searching: ").strip().lower()
			while not search_word.isalpha():
				self.clear_everything()
				print("Invalid input. Try again.")
				search_word = input("Enter the word you are searching: ").strip().lower()

			mycursor.execute(f"select uzbek from table_words where english='{search_word}'")
			prt = mycursor.fetchall()
			print(prt[0][0])


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


	def save_to_database(self, new_word_en, new_word_uz):

		mycursor.execute(f"insert into table_words (english, uzbek) values ('{new_word_en}', '{new_word_uz}')")
		mydb.commit()


	@staticmethod
	def clear_everything():
		os.system("clear")


en_uz = Dictionary()
en_uz.entrance()

