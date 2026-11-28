class Solution:
    def trap(self, height: List[int]) -> int:
        heightLen = len(height)

        if heightLen == 1 or heightLen == 2:
            return 0

        i = 0
        j = heightLen - 1

        maxHeight = 0
        width = 0
        occupiedTiles = 0
        trappedWater = 0
        

        while i < heightLen:
            if height[i] >= maxHeight:
                trappedWater += (min(height[i], maxHeight) * width) - occupiedTiles
                width = 0
                occupiedTiles = 0
                maxHeight = height[i]
            else:
                width += 1
                occupiedTiles += height[i]
            i += 1
        
        maxHeight = 0
        width = 0
        occupiedTiles = 0
        
        while j >= 0:
            if height[j] > maxHeight:
                trappedWater += (maxHeight * width) - occupiedTiles
                width = 0
                occupiedTiles = 0
                maxHeight = height[j]
            else:
                width += 1
                occupiedTiles += height[j]
            j -= 1

        return trappedWater
