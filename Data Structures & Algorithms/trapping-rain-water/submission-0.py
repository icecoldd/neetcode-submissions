class Solution:
    def trap(self, height: List[int]) -> int:
        heightLen = len(height)
        i = 0
        j = heightLen - 1

        tallest_left_wall = []
        tallest_right_wall = []
        tallest_left = 0
        tallest_right = 0

        while (i < heightLen):
            if height[i] > tallest_left:
                tallest_left = height[i]
            if height[j] > tallest_right:
                tallest_right = height[j]
            
            tallest_left_wall.append(tallest_left)
            tallest_right_wall.append(tallest_right)
            
            i+=1
            j-=1

        tallest_right_wall.reverse()

        totalAmountOfWater = 0
        for i in range(heightLen):
            totalAmountOfWater += min(tallest_left_wall[i], tallest_right_wall[i]) - height[i]

        return totalAmountOfWater
