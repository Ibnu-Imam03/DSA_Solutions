class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
          c = set()
          for i, j in ranges:
             for b in range(i, j + 1):
                  c.add(b)

          for d in range(left, right + 1):
               if d not in c:
                        return False
          else:
                  return True
            