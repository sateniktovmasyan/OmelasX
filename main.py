class Card:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
        self.next = None

class Cards_Set:
    def __init__(self, head):
        self._head = head

    def sethead(self):
        return self._head

    def gethead(self):
        return self._head

    def append(self, data, data2):
        new_node = Card(data == raw_input(), data2 == raw_input())

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next





def main():
    ca = Cards_Set("")
    ca.append(raw_input("Please input a word "), raw_input("Please input a definition "))
    ca.print_list()


main()