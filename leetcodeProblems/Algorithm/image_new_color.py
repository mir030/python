class Solution:
    def floodFill(self, image, sr, sc, newColor):
        old, col, row = image[sr][sc], len(image), len(image[0])
        if old != newColor:
            stack = [(sr, sc)]
            while stack:
                i, j = stack.pop()
                image[i][j] = newColor
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < col and 0 <= y < row and image[x][y] == old:
                        stack.append((x, y))
                                                                                                                                                                                                                                                                                                                                                                                                                                                     return image


s = Solution()
print(s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
