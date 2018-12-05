class Card:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
        self.next = None

class Cards_Set:
    def __init__(self):
        self._head = None

    def sethead(self):
        return self._head

    def gethead(self):
        return self._head

    def append(self, data, data2):
        new_node = Card(data, data2)
        if self._head is None:
            self._head = new_node
            return new_node

        last_node = self._head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self._head
        while cur_node:
            print(str(cur_node.word))
            print(str(cur_node.definition))
            cur_node = cur_node.next


def main():
    ca = Cards_Set()
    ca.append(raw_input("Please input a word "), raw_input("Please input a definition "))
    print("add another word?")
    x = raw_input
    if x == "yes":
         ca.append(raw_input("Please input a word "), raw_input("Please input a definition "))
    else:
        print("*****")

    print(" ")
    print("Here is the word with a definition")
    ca.print_list()


main()

