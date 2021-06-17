class Card:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return self.question

    def reveal(self):
        print(self.question)
        input("Press enter to see answer...")
        print(self.answer)

# first = Card("Did the 76ers blow it??", "YES")
# first.reveal()
# exit()
