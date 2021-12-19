from back_functions import caching
import random

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def printTree(self):
        if self.hasLeftChild():
            self.leftChild.printTree()
        print(self.payload, self.key)
        if self.hasRightChild():
            self.rightChild.printTree()


    def hasRightChild(self):
        return self.rightChild

    def hasLeftChild(self):
        return self.leftChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self



class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        for i in range(0, self.length()):
            return self.root.printTree()

    def put(self, key, val):
        if self.root:

            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)


    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)


    def inorderTraversal(self, root):
        res = []
        res_dict = {}
        if root:
            res = self.inorderTraversal(root.hasLeftChild())
            res_dict[root.key] = root.payload
            res.append(res_dict)
            res = res + self.inorderTraversal(root.hasRightChild())
        return res

    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.payload)
            res = res + self.preorderTraversal(root.hasLeftChild())
            res = res + self.preorderTraversal(root.hasRightChild())
        return res


    def add_more_than_one(self, song_obj):
        self.put(song_obj.score, song_obj)

    def create_tree_from_cache(self, file):
        content = caching.open_cache(file)
        print('this is the cache')

        print('\n\ncontent stuff')
        key_list = list(content.keys())
        print(key_list)
        for item in key_list:
            print('testing', content.get(item))
            self.put(content.get(item)['score'], content.get(item))
        return self


    def find_range(self, root, lower, higher, range_list=[]):
        if root is None:
            return

        if lower < root.payload['score']:
            self.find_range(root.leftChild, lower, higher)

        if lower <= root.payload['score'] <= higher:
            print(root.payload['score'])
            range_list.append(root.payload['score'])

        self.find_range(root.rightChild, lower, higher)
        return range_list


    def find_recommendation(self, range_of_scores):
        key = random.choice(range_of_scores)
        obj = self.get(key)
        return obj['name'], obj['artist']


    def access_and_recommend(self,file, lower_bound=0, upper_bound=100):
        cached_tree = self.create_tree_from_cache(file)
        ranges = cached_tree.find_range(cached_tree.root, lower_bound, upper_bound)
        return cached_tree.find_recommendation(ranges)


songtree = BinarySearchTree()


