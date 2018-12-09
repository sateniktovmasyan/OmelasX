class Card:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
        self.next = None

class Cards_Set:
    def __init__(self):
        self._head = None
        self.number = 0

    def sethead(self):
        return self._head
    def gethead(self):
        return self._head

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

    def remove1(self, node_value):
        previous_node = None
        current_node = self.__head
        while current_node:
            if current_node.data == node_value:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.__head = current_node.next
                return True

            previous_node = current_node
            current_node = current_node.next

    def remove(self, item_id):
        current_id = 1
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    return
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1
        return

    def randomcard(self):
        print(self.getNth(1))


    def getNth(self, index):
        current = self._head
        count = 0
        while (current):
            if (count == index):
                return current.word
            count += 1
            current = current.next
        return 0

    def list_length(self):
        count = 0
        current_node = self.__head

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
            print("*"*40)
            cur_node = cur_node.next


def main():
    ca = Cards_Set()
    print("At first add new words")
    ca.addNewCards()

main()

