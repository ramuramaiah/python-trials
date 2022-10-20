from __future__ import annotations
from typing import List

class TreeNode:
    """
    A class to represent TreeNode
    """
    root_nodes:List[TreeNode] = []
    def __init__(self,data:str,children:List[TreeNode]):
        self.data = data
        self.children = children

    def __str__(self,level:int=0):
        ret = " " * level + str(self.data) + '\n'
        for child in self.children:
            ret += child.__str__(level+1)

        return ret

    def addchildren(self,node:TreeNode):
        """
        Add children to the TreeNode
        """
        self.children.append(node)

    def haschildren(self,name:str):
        """
        Returns True if the TreeNode has a children matching the given name
        """
        for child in self.children:
            if name == child.data:
                return True
        return False

    def findchildren(self,name:str):
        """
        Finds the children with the given name
        """
        for child in self.children:
            if name == child.data:
                return child
        return None

    @staticmethod
    def find_node(name:str):
        """
        Find the TreeNode in the root_nodes
        """
        for node in TreeNode.root_nodes:
            if node.data == name:
                return node
        return None

    @staticmethod
    def print_root():
        """
        Prints the root nodes in a hierarchy
        """
        for node in TreeNode.root_nodes:
            print(node)

def flat_to_hierarchy(entries:List[str]):
    """
    Converts the flat representation to a hierarchical representation
    """
    for entry in entries:
        parent:TreeNode=None
        child:TreeNode=None
        splits:List[str] = entry.split("/")
        for i, val in enumerate(splits):
            if splits[i] == "":
                continue
            if i == 0:
                temp:TreeNode = TreeNode.find_node(splits[i])
                if temp is None:
                    temp = TreeNode(splits[i],[])
                    TreeNode.root_nodes.append(temp)
            else:
                if parent.haschildren(splits[i]) is False:
                    child = TreeNode(splits[i],[])
                    print(f"adding children {child.data} for parent {parent.data}")
                    parent.addchildren(child)
                else:
                    child = parent.findchildren(splits[i])
            if i == 0:
                parent = temp
            else:
                parent = child

def print_hierarchy():
    """
    Print the root_nodes in a hierarchical way
    """
    TreeNode.print_root()

if __name__ == "__main__":
    flat_entries:List[str] = ["Drinks/Cold/Cola", "Drinks/Hot/Cappuccino"]
    flat_to_hierarchy(flat_entries)
    print_hierarchy()
