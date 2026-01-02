class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        a=[1]
        b=self.getRow(rowIndex-1)
        for i in range(len(b)-1):
            a.append(b[i]+b[i+1])
        a.append(1)
        return a