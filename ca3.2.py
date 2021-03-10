class node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data
class tree:
    def __init__(self):
        self.init_node = None
        self.longest_path = 0
    def add_node(self,data):
        new_node = node(data)
        if self.init_node == None:
            self.init_node = new_node
            return
        temp_node = self.init_node
        count = 0
        while 1:
            if data <= temp_node.data and temp_node.left !=None:
                temp_node = temp_node.left
                count +=1
            elif data > temp_node.data and temp_node.right != None:
                temp_node = temp_node.right
                count +=1
            else:
                break
        if data <= temp_node.data:
            temp_node.left = new_node
            count +=1
        else:
            temp_node.right = new_node
            count +=1
        if count > self.longest_path:
            self.longest_path = count
number_of_nums = input()
nums = list(map(int,input().split()[::-1]))
Tree = tree()
for i in nums:
    Tree.add_node(i)
print(Tree.longest_path)
