class node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data
class tree:
    def __init__(self,nums):
        self.root_node = None
        self.nums = nums
        self.answer = None
    def build_tree(self):
        i = 0
        num = ""
        while i<len(self.nums):
            if self.nums[i] == '*' or self.nums[i] =='/':
                break
            num += self.nums[i]
            i += 1
        new_node =node(num)
        self.root_node = new_node
        while i<len(self.nums):
            if self.nums[i] == '*' or self.nums[i] == '/':
                temp_node = self.root_node
                self.root_node = node(self.nums[i])
                self.root_node.left = temp_node
            i += 1
            num = ""
            while i<len(self.nums):
                if self.nums[i] == '*' or self.nums[i] =='/':
                    break
                num += self.nums[i]
                i += 1
            self.root_node.right = node(num)
        self.answer = self.calculate_answer(self.root_node)
    
    def calculate_answer(self,Node):
        if Node.left == None and Node.right == None:
            num = ""
            splited = Node.data.split()
            for i in splited:
                num+=i
            if num == '' or num == '+':
                return 1
            if num == '-':
                return -1
            return float(num)
        if Node.data == '*':
            return self.calculate_answer(Node.left) * self.calculate_answer(Node.right)
        if Node.data == '/':
            return self.calculate_answer(Node.left) / self.calculate_answer(Node.right)
    

def seperate_x_and_nums(eq):
    Xs = []
    nums = []
    i= 0
    num = ""
    while i < len(eq):
        j= i
        while eq[j] !='+' and eq[j] !='-'  :
            num +=eq[j]
            if j < len(eq) -1 :
                j+=1
            else:
                break
        if j == 0:
            num = eq[j]
            if eq[j] == 'x':
                Xs.append('x')
            elif len(eq) == 1:
                nums.append(num)  
            i+=1
            continue
        if 'x' in num:
            Xs.append(num)
        else:
            nums.append(num)
        if eq[j] == '-':
            num = '-'
        else:
            num = "+"
        i = j+1
    return Xs , nums

def calc_nums(nums):
    sum = 0
    for i in nums:
        Tree = tree(i)
        Tree.build_tree()
        sum +=Tree.answer
    return sum

def calc_Xs(Xs):
    sum = 0
    for i in Xs:
        j = 0
        num = ""
        while j<len(i):
            if i[j] != 'x':
                if not (i[j] == '*' and i[j+1] == 'x' and j<len(i)-1):
                    num +=i[j]
            j +=1
        Tree = tree(num)
        Tree.build_tree()
        sum +=Tree.answer
    return sum
    
def calc_final_answer_tree():
    sum_left_nums = calc_nums(left_nums)
    sum_right_nums = calc_nums(right_nums)
    sum_left_Xs = calc_Xs(left_Xs)
    sum_right_Xs = calc_Xs(right_Xs)
    return (sum_right_nums -sum_left_nums)/(sum_left_Xs - sum_right_Xs)

equation = input()
splited_eq = equation.split('=')
left_eq = splited_eq[0]
right_eq = splited_eq[1]
left_Xs , left_nums = seperate_x_and_nums(left_eq)
right_Xs , right_nums = seperate_x_and_nums(right_eq)
print(round(calc_final_answer_tree(),3))
