import random

class Card:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
        self.next = None

class Cards_Set:
    def __init__(self):
        self._head = None
        self.number = 0

    def addNewCards(self):
        x = raw_input("Do you want to add a word ")
        while True:
            if x == "yes":
                word = raw_input("Please input a word ")
                definition = raw_input("Please input a definition ")
                if (self.contains(word)):
                    print ("Word Exists")
                    print(word, definition)
                    print("add another one")
                    self.addNewCards()
                new_node = Card(word, definition)
                if self._head is None:
                    self._head = new_node
                else:
                    last_node = self._head
                    while last_node.next is not None:
                        last_node = last_node.next
                    last_node.next = new_node
                x = raw_input("Do you want to add a word ")
                self.number = self.number + 1

            elif x == "no":
                a = raw_input("want to turn on learning mode input yes or no ")
                if a == "yes":
                    self.randomcard()
                elif a == "no":
                    print "here is your list"
                    self.print_list()
                else:
                    print("please input valid answer ")
            else:
                x = raw_input("please input yes or no ")

    def deleteword(self, word):
        temp = self._head
        if temp.word == word:
            self._head = temp.next
        else:
            while temp is not None and temp.next.word != word:
                temp = temp.next
            temp.next = temp.next.next


    def randomcard(self):
    list_len = self.list_length()
    index = random.randint(0,list_len - 1)
    card = self.getNth(index)
    x = raw_input("Do you know the definition for " + card.word+ "?")
    while True:
        if x == "yes":
            y = raw_input("what is it ?")
            while True:
                if y == card.definition:
                    print "you got it, Good job"
                    print "lets move on"
                    self.randomcard()
                else:
                    y = raw_input("Wrong answer, please try again")
        elif x == "no":
            z = raw_input("Do you want to find other words ? ")
            while True:
                if z == "yes":
                    self.randomcard()
                elif z == "no":
                    print "have a nice day"
                    exit()
                else:
                    z = raw_input("please enter yes or no")
        else:
            x = raw_input("please enter yes or no")
    def getNth(self, index):
        current = self._head
        count = 0
        while (current):
            if (count == index):
                return current.word

            count = count + 1
            current = current.next
        return 0 # smth strange

    def list_length(self):
        count = 0
        current_node = self._head
        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count

    def is_empty(self):
        if self.list_length() == 0:
            print("You have no items in your list")
            self.addNewCards()
            return True
        else:
            self.randomcard()
            return False

    def len(self, node):
        if node is None:
            return 0
        return self.len(node.next) + 1

    def contains(self, word):
        cur_node = self._head
        while cur_node is not None:
            if (cur_node.word == word):
                return True
            cur_node = cur_node.next
        return False

    def print_list(self):
        cur_node = self._head
        while cur_node is not None:
            print"word: ", (str(cur_node.word))
            print"definition: ", (str(cur_node.definition))
            print("*"*27)
            cur_node = cur_node.next


def main():
    ca = Cards_Set()
    print("At first add new words")
    ca.addNewCards()

main()
