
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

	def entrance(self):
		self.show_text()
		options = '1234'
		option = input(": ").strip()

		if option == '':
			option = ' '

		while option not in options:
			self.clear_everything()
			self.show_text()
			option = input("Invalid input. Enter only [1, 2, 3, 4]: ").strip()
			if option == '':
				option = ' '

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

		if self.is_exists(new_word):
			print("This word already exists in dictionary")
			self.add_new_word()

		new_word_translate = input('Input translation of word: ').strip().lower()
		while not new_word_translate.isalpha():
			self.clear_everything()
			print("Invalid input. Input only should be letters[a-z] and not be an empty")
			new_word_translate = input('Input translation of word: ').strip().lower()

		self.save_to_database(new_word, new_word_translate)


		### To choose quit or go back to main menu ###
		self.menu_or_quit()


	def show_words(self):
		mycursor.execute("select * from table_words")
		var_show = mycursor.fetchall()

		self.clear_everything()

		print("\n")
		print("[id]   [English]   [Uzbek]")
		for i in var_show:
			print("------------------------")
			print(f"{i[0]}| {i[1]} - {i[2]}")

		### To choose quit or go back to main menu ###
		self.menu_or_quit()




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
			search_word = input("Enter the word you are searching[uzbek]: ").strip().lower()

			while self.is_input_exists_if(search_word):
				self.clear_everything()
				print("Invalid input. Try again.")
				search_word = input("Enter the word you are searching[uzbek]: ").strip().lower()

			mycursor.execute(f"select * from table_words where uzbek='{search_word}'")
			prt = mycursor.fetchall()
			print(prt[0][1])

		else:
			self.clear_everything()
			search_word = input("Enter the word you are searching[english]: ").strip().lower()
			while self.is_input_exists_else(search_word):
				self.clear_everything()
				print("Invalid input. Try again.")
				search_word = input("Enter the word you are searching[english]: ").strip().lower()

			mycursor.execute(f"select * from table_words where english='{search_word}'")
			prt = mycursor.fetchall()
			print(prt[0][2])

		### To choose quit or go back to main menu ###
		self.menu_or_quit()



	def quit(self):
		self.clear_everything()
		print("\n")
		print(">>> Thanks for using our dictionary! <<<")
		print("    ________________________________     ")


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


	def menu_or_quit(self):
		print("\n")
		quit_menu = input("[Quit/Menu]: ").strip().lower()
		while quit_menu != 'quit' and quit_menu != 'menu':
			self.clear_everything()
			print("Invalid input! >>>")
			quit_menu = input("[Quit/Menu]: ").strip().lower()

		if quit_menu == 'quit':
			self.quit()
		elif quit_menu == 'menu':
			self.clear_everything()
			self.entrance()



	@staticmethod
	def save_to_database(new_word_en, new_word_uz):
		mycursor.execute(f"insert into table_words (english, uzbek) values ('{new_word_en}', '{new_word_uz}')")
		mydb.commit()

	@staticmethod
	def is_exists(something):
		mycursor.execute("select english from table_words")
		check = mycursor.fetchall()
		for word in check:
			if word[0][0] == something:
				return True
		return False

	@staticmethod
	def clear_everything():
		os.system("clear")

	@staticmethod
	def is_input_exists_if(input_word):
		mycursor.execute(f"select * from table_words where uzbek='{input_word}'")
		list_check = mycursor.fetchall()

		if not list_check:
			return True
		else:
			return False

	@staticmethod
	def is_input_exists_else(input_word):
		mycursor.execute(f"select * from table_words where english='{input_word}'")
		list_check = mycursor.fetchall()

		if not list_check:
			return True
		else:
			return False



en_uz = Dictionary()
en_uz.entrance()

