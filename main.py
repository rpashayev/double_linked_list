import math
class DLNode:
    def __init__(self, val):
        self.value = val
        self.previous = None
        self.next = None


class DLList:
    def __init__(self):
        self.first = None
        self.last = None
    
    def print_values(self):
        runner = self.first
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self
    
    def print_values_bw(self):
        runner = self.last
        while runner != None:
            print(runner.value)
            runner = runner.previous
        return self
    
    def add_to_front(self, val):
        new_node = DLNode(val)
        if self.first != None:
            current_first = self.first
            new_node.next = current_first
            current_first.previous = new_node
            self.first = new_node
        else:
            self.first = new_node
            self.last = new_node
        return self
        
    def add_to_end(self, val):
        new_node = DLNode(val)
        if self.last != None:
            current_last = self.last
            new_node.previous = current_last
            current_last.next = new_node
            self.last = new_node
        else:
            self.add_to_front(val)
        return self
    
    def insert_after(self, prev_val, val):
        new_node = DLNode(val)
        runner = self.first
        while runner != None:
            if runner.value == prev_val:
                new_node.next = runner.next
                new_node.previous = runner
                new_node.next.previous = new_node
                new_node.previous.next = new_node
            runner = runner.next
        return self

    def insert_between(self, val1, val2, val):
        new_node = DLNode(val)
        runner = self.first
        while runner != None:
            if runner.value == val1 and runner.next.value == val2:
                new_node.next = runner.next
                new_node.previous = runner
                new_node.next.previous = new_node
                new_node.previous.next = new_node
            runner = runner.next
        return self
    
    def remove_node(self, val):
        if self.first.value == val: # if val is the first item
            self.first = self.first.next
            self.first.previous = None
        elif self.last.value == val: # if val is the last item
            self.last = self.last.previous
            self.last.next = None
        else:
            runner = self.first.next
            while runner != None:
                if runner.value == val:
                    runner.next.previous = runner.previous
                    runner.previous.next = runner.next
                runner = runner.next
        return self

    def mid_of_list(self):
        n = 0
        runner = self.first
        while runner != None:
            n += 1
            runner = runner.next
        
        runner = self.first
        for i in range (int(round((n-1)/2,0))):
            runner = runner.next
        print(runner.value)

    def mid_of_list_alt(self):
        runner_inner = self.first
        runner_outer = self.first
        while runner_outer != None and runner_outer.next != None:
            runner_inner = runner_inner.next
            runner_outer = runner_outer.next.next
        print(runner_inner.value)

    def reverse_list(self):
        runner = self.first
        while runner is not None:
            runner.previous, runner.next = runner.next, runner.previous
            runner = runner.previous
        self.first, self.last = self.last, self.first
        self.print_values()
        
        
new_list = DLList()
new_list.add_to_end('!').add_to_front('world').add_to_end('end1').add_to_front('Hello').add_to_end('the end').insert_after('Hello', 'my').insert_between('my', 'world', 'lovely').remove_node('Hello').remove_node('end1').remove_node('the end').add_to_front('day').add_to_front('beautiful').add_to_front('What a').remove_node('!').print_values()

new_list.reverse_list()

new_list.mid_of_list() # if even shows the 1st mid node
new_list.mid_of_list_alt() # if even shows the 2nd mid node
