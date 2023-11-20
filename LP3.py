# DAA 1
# def recursive_fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

# def non_recursive_fibonacci(n):
#     first=0
#     second=1
#     print(first)
#     print(second)
#     while n-2>0:
#         third = first + second
#         first=second
#         second=third
#         print(third)
#         n-=1

# if __name__=="__main__":
#     n=10
#     for i in range(n):
#         print(recursive_fibonacci(i))
    
#     non_recursive_fibonacci(n)

# DAA 2
# import heapq

# Creating Huffman tree node
# class node:
#     def __init__(self,freq,symbol,left=None,right=None):
#         self.freq=freq # frequency of symbol
#         self.symbol=symbol # symbol name (character)
#         self.left=left # node left of current node
#         self.right=right # node right of current node
#         self.huff= '' # # tree direction (0/1)

#     def __lst__(self,nxt): # Check if curr frequency less than next nodes freq
#         return self.freq < nxt.freq

# def printnodes(node,val=''):
#     newval=val+str(node.huff)
#     # if node is not an edge node then traverse inside it
#     if node.left: 
#         printnodes(node.left,newval)
#     if node.right: 
#         printnodes(node.right,newval)

#     # if node is edge node then display its huffman code
#     if not node.left and not node.right:
#         print("{} -> {}".format(node.symbol,newval))

# if __name__=="__main__":
#     chars = ['a', 'b', 'c', 'd', 'e', 'f']
#     freq = [ 5, 9, 12, 13, 16, 45]
#     nodes=[]    

#     for i in range(len(chars)): # converting characters and frequencies into huffman tree nodes
#         heapq.heappush(nodes, node(freq[i],chars[i]))

#     while len(nodes)>1:
#         left=heapq.heappop(nodes)
#         right=heapq.heappop(nodes)

#         left.huff = 0
#         right.huff = 1
#         # Combining the 2 smallest nodes to create new node as their parent
#         newnode = node(left.freq + right.freq , left.symbol + right.symbol , left , right)
#         # node(freq,symbol,left,right)
#         heapq.heappush(nodes, newnode)

#     printnodes(nodes[0]) # Passing root of Huffman Tree

#DAA 3
# def frac_knapsack():
#     weights = [10,20,30]
#     values = [60,100,120]
#     capacity = 50
#     res = 0
#     for pair in sorted(zip(weights,values),key = lambda x:x[1]/x[0],reverse=True):
#         if capacity <= 0:
#             break
#         if pair[0] > capacity:
#             res += int(capacity*(pair[1]/pair[0]))
#             capacity = 0
#         elif pair[0] <= capacity:
#             res += pair[1]
#             capacity -= pair[0]
#     print(res)

# if __name__ == '__main__':
#     frac_knapsack()

#DAA 4
# def knapsack(values,weights,capacity):
#     dp = [[0 for i in range(capacity+1)] for j in range(len(values)+1)]

#     for item in range(1,len(values)+1):
#         for weight in  range(1,capacity+1):
#             if weights[item-1] <= weight:
#                 dp[item][weight] = max(dp[item-1][weight-weights[item-1]]+values[item-1],dp[item-1][weight])
#             else:
#                 dp[item][weight] = dp[item-1][weight]
#     return dp[-1][-1]

# while True:
#     print("press Ctrl+C to terminate")
#     n = int(input("Enter no. of items: "))
#     values = [int(i) for i in input("Enter values of items:").split(" ")]
#     weights = [int(i) for i in input("Enter weights of items:").split(" ")]
#     capacity = int(input("Enter maximum weight: "))
#     maximum_value = knapsack(values,weights,capacity)
#     print("The maximum value of items that can be carried: ",maximum_value)

#DAA 5
# def n_queens(n):
#     col = set()
#     posDiag = set()
#     negDiag = set()

#     res = []

#     board = [["0"]*n for i in range(n)]

#     def backtrack(r):
#         if r == n:
#             copy = [" ".join(row) for row in board]
#             res.append(copy)
#             return

#         for c in range(n):
#             if c in col or (r+c) in posDiag or (r-c) in negDiag:
#                 continue
#             col.add(c)
#             posDiag.add(r+c)
#             negDiag.add(r-c)
#             board[r][c] = "1"

#             backtrack(r+1)

#             col.remove(c)
#             posDiag.remove(r+c)
#             negDiag.remove(r-c)
#             board[r][c] = "0"
#     backtrack(0)
#     for sol in res:
#         for row in sol:
#             print(row)
#         print()

# if __name__ == '__main__':
#     n_queens(8)

