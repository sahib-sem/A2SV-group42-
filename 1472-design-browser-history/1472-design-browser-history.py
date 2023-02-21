class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr=[homepage]
        self.curr=0
        

    def visit(self, url: str) -> None:
        if self.curr+1==len(self.arr):
            self.arr.append(url)
            self.curr+=1
        else:
            arr=[]
            for i in range(self.curr+1):
                arr.append(self.arr[i])
            arr.append(url)
            self.arr=arr
            self.curr=len(arr)-1
        

    def back(self, steps: int) -> str:
        if self.curr-steps>=0:
            self.curr-=steps
        else:
            self.curr=0
        return self.arr[self.curr]
        

    def forward(self, steps: int) -> str:
        if self.curr + steps < len(self.arr):
            self.curr += steps
            return self.arr[self.curr]
        else:
            self.curr=len(self.arr)-1
            return self.arr[self.curr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)