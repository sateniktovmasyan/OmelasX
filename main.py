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

    def append(self):
        x = raw_input("Do you want to add a word ")
        while True:
            if x == "yes":

                word = raw_input("Please input a word ")
                definition = raw_input("Please input a definition ")
                new_node = Card(word, definition)
                if self._head is None:
                    self._head = new_node
                else:
                    last_node = self._head
                    while last_node.next:
                        last_node = last_node.next
                    last_node.next = new_node
                x = raw_input("Do you want to add a word ")

            elif x == "no":
                self.print_list()
                return

            else:
                x = raw_input("please input yes or no ")

    def print_list(self):
        cur_node = self._head
        while cur_node is not None:
            print"word: ", (str(cur_node.word))
            print"definition: ", (str(cur_node.definition))
            cur_node = cur_node.next


def main():
    ca = Cards_Set()
    ca.append()


main()

