# 2) Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter

class MyNode:
    '''
    Класс: узел бинарного дерева
    '''
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class MyLeaf:
    '''
    Класс: листок бинарного дерева
    '''
    def __init__(self, value, name):
        self.value = value
        self.name = name

def leaf_sort(leaf):
    '''
    Функция для сортировки листьев по весу
    '''
    return leaf.value

def create_leaf(data):
    '''
    Функция для подсчёта частоты вхождения символа в последовательность
    и создания листьев бинарного дерева
    '''
    count = Counter(data)
    leaves = []
    for name, value in count.items():
        leaves.append(MyLeaf(value, name))
    leaves.sort(key=leaf_sort)
    return leaves

def create_node(nodes):
    '''
    Функция создания узлов бинарного дерева
    '''
    while len(nodes) > 1:
        node1 = nodes.pop(0)
        node2 = nodes.pop(0)
        new_node = MyNode(node1.value + node2.value, node1, node2)
        for i in range(len(nodes)):
            if nodes[i].value < new_node.value:
                continue
            else:
                nodes.insert(i, new_node)
                break
        else:
            nodes.append(new_node)

    return nodes[0]

def create_code_dict(node, code_dict={}, path=''):
    '''
    Функция создания словаря, содержащего код для каждого символа
    '''
    if isinstance(node, MyLeaf):
        code_dict[node.name] = path
    if isinstance(node, MyNode):
        create_code_dict(node.left, code_dict, path=path+'0')
        create_code_dict(node.right, code_dict, path=path+'1')
    return code_dict

def encode(data):
    '''
    Функция кодировки 
    '''
    leaves = create_leaf(data)
    nodes = create_node(leaves)
    code_dict = create_code_dict(nodes)

    code = ''
    for char in data:
        # code += code_dict[char]
        code = code + code_dict[char] + ' '

    return code

data = 'beep boop beer!'
print(encode(data))

# Символы ' ' и 'o' имеют код отличный от кода в методичке, т.к. ' ' встречается в последовательности раньше