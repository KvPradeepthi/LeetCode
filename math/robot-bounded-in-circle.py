class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y=0,0
        direction="N"
        for ch in instructions:
            if ch=='G':
                if direction=="N":
                    y=y+1
                elif direction=="S":
                    y=y-1
                elif direction=="E":
                    x=x+1
                else:
                    x=x-1
            if ch=='L':
                if direction=="N":
                    direction="W"
                elif direction=="W":
                    direction="S"
                elif direction=="S":
                    direction="E"
                else:
                    direction="N"
            if ch=='R':
                if direction=="N":
                    direction="E"
                elif direction=="E":
                    direction="S"
                elif direction=="S":
                    direction="W"
                else:
                    direction="N"
        return (x==0 and y==0) or direction!="N"
