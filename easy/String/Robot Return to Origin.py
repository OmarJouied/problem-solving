class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

        You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

        Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

        Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

        for ref:
        class Solution:
          def judgeCircle(self, moves: str) -> bool:
              return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

              # ans=0
              # ans1=0
              # for i in moves:
              #     if i=="U":
              #         ans+=1
              #     elif i=="D":
              #         ans-=1
              #     elif i=="L":
              #         ans1-=1
              #     elif i=="R":
              #         ans1+=1
              # return ans==0 and ans1==0    
        c++
        class Solution {
        public:
            bool judgeCircle(string moves) {
                int x = 0, y = 0;

                for (char move : moves) {
                    if (move == 'R') x++;
                    else if (move == 'L') x--;
                    else if (move == 'U') y++;
                    else y--;
                }
                return (x == 0 && y == 0);
            }
        };  
        """
        moves_directions = {"U": 0,"D": 0,"R": 0,"L": 0}
        for i in moves:
          moves_directions[i] += 1
        
        return not (moves_directions["D"] - moves_directions["U"] or moves_directions["R"] - moves_directions["L"])
