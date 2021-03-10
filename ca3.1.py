class node:
    def __init__(self,data,index):
        self.right = None
        self.left = None
        self.data = data
        self.index = index
class huffman:
    def __init__(self):
        self.init_node = None
        self.nodes_list = []
    def make_nodes(self,freq):
        for i in range(len(freq)):
            new_node = node(freq[i],i+1)
            self.nodes_list.append(new_node)
        self.nodes_list.sort(key=lambda x:x.data,reverse = False)
        while len(self.nodes_list) >1:
            self.nodes_list.sort(key=lambda x:x.data,reverse = False)
            new_node = node(self.nodes_list[0].data+self.nodes_list[1].data,0)
            new_node.left = self.nodes_list[0]
            new_node.right = self.nodes_list[1]
            self.nodes_list = self.nodes_list[2:]
            self.nodes_list.insert(0,new_node)
        self.root = self.nodes_list[0]
    def print_answers(self,code):
        temp_node = self.root
        ans = ""
        i =0
        for i in range(len(code)):
            if code[i] =="1":
                temp_node = temp_node.right
            else:
                temp_node = temp_node.left
            if temp_node.right is None:
                ans +=str(temp_node.index)+","
                temp_node = self.root
        return ans[:-1]
a = input()
code = input()
freq = list(map(int,input().split()))
Tree = huffman()
Tree.make_nodes(freq)
print(Tree.print_answers(code))