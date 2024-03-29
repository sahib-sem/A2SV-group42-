class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numbers=[str(i) for i in range(1,10)]
        for r in range(len(board)):
            is_unique=[]
            for c in range(len(board[0])):
                if board[r][c] in numbers:
                    is_unique.append(board[r][c])
            count_num=Counter(is_unique)
            for val in count_num.values():
                if val>1:
                    return False
        for c in range(len(board[0])):
            is_unique=[]
            for r in range(len(board)):
                if board[r][c] in numbers:
                    is_unique.append(board[r][c])
            count_num=Counter(is_unique)
            for val in count_num.values():
                if val>1:
                    return False
        dic={}

        for row in range(len(board)):
            for col in range(len(board[0])):
                r=row//3
                c=col//3
                if dic.get((r,c)):
                    dic[(r,c)].append(board[row][col])
                else:
                    dic[(r,c)]=[board[row][col]]
        print(dic)
        for lst in dic.values():
            lst_counter=Counter(lst)
            for key,val in lst_counter.items():
                if key!='.' and val>1:
                    return False
        return True
        
            


