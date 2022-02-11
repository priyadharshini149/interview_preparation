import numpy as np
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        l=np.array(mat)
        try:
            return (l.reshape([r,c]))
        except:
            return mat
        