import pandas as pd
import numpy as np
import unittest

"""
MetaMat
Function that synchronizes list represented as
standard python list, np.Array and pd.Dataframe
"""


class MetaMat:

    def __init__(self, list):
        self.__List = list
        self.__PFrame = None
        self.__NMatrix = None
        self.updateFromL()

    def appendToList(self, number):
        self.__List.append(number)
        self.updateFromL()

    def changeNElement(self, x, y, value):
        self.__NMatrix[x, y] = value
        self.updateFromN()

    def changePRow(self, keys, row):
        raise Exception("I dont understand the question")

    def updateFromL(self):
        self.__PFrame = pd.DataFrame(
            [self.__List],
            columns=self.create_idx(len(self.__List)))
        self.__NMatrix = np.array(self.__List)

    def updateFromP(self):
        self.__List = self.__PFrame.iloc[1:][:].tolist()
        self.__NMatrix = self.__PFrame.iloc[1:][:].to_numpy()

    def updateFromN(self):
        self.__List = self.__NMatrix.tolist()
        self.__PFrame = pd.DataFrame(
            [self.__List],
            columns=self.create_idx(self.__NMatrix.size))


    def create_idx(self, len):
        return ["C" + str(number) for number in range(len)]

    def __eq__(self, other):
        if self.__List != other.__List:
            return False

        diff =  self.__NMatrix == other.__NMatrix
        if not diff.all():
            return False    

        if not self.__PFrame.equals(other.__PFrame):
            return False

        return True


class TestMetaMat(unittest.TestCase):

    def testUpdateFromNumpy(self):
        meta1 = MetaMat([1, 2, 3])
        meta1.appendToList(1)

        meta2 = MetaMat([1, 2, 3, 1])
        self.assertEqual(
            meta1, meta2,
            "Meta matricies are not the same after @appendToList()")

    def testUpdateFromPandas(self):
        meta1 = MetaMat([1, 2, 3])
        meta1.changeNElement(1, 0, 1)

        meta2 = MetaMat([1, 2, 1])
        self.assertEqual(
            meta1, meta2,
            "Meta matricies are not the same after @changeNElement()")

    def testUpdateFromList(self):
        pass



"""
If lib called as a script run the tests
"""
if __name__ == '__main__':
    unittest.main()