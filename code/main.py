class Solution:

    """ Constructor definition """
    def __init__(self):
        self.sideNumber = 6

    """ Function definition """
    @staticmethod
    def triangular(index: int) -> int:
        return index * (index + 1) // 2

    def polygon_number(self, s: int, i: int) -> int:

        # Given the number of sides of the polygon
        # and the index of the term of the sequence,
        # we can calculate any term of any polygon
        # sequence, by using the following function!
        if i == 1: return 1
        if i == 2: return s

        term0 = (s + (i - 2) * (s - 1))
        term1 = self.triangular(i - 2) * (s - 2)
        return term0 + term1

    def poly_sequence(self, s: int, bound: int) -> list:
        return [self.polygon_number(s, k) for k in range(1, bound)]

    def solve(self):

        polySequence = self.poly_sequence(self.sideNumber, 120)

        print()
        print(polySequence)

if __name__ == "__main__":

    solution = Solution()
    solution.solve()
