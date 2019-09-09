#用check函数判断一个位置是否能够放Q
#从0行0列开始往下递归放置Q，如果位置合适，则放置一枚Q，并继续向下一行进行递归
def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def check(k,j,board):
            for i in range(k):
                if board[i]==j or abs(k-i)==abs(board[i]-j):
                    return False
            return True
        def dfs(depth,board,valuelist,solution):
            if depth==len(board):
                solution.append(valuelist)
            for row in range(len(board)):
                if check(depth,row,board):
                    s='.'*len(board)
                    board[depth]=row
                    dfs(depth+1,board,valuelist+[s[:row]+'Q'+s[row+1:]],solution)
        board=[-1 for i in range(n)]
        solution=[]
        dfs(0,board,[],solution)
        return solution