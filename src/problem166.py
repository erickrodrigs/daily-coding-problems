"""
This problem was asked by Uber. (Medium)

Implement a 2D iterator class. It will be initialized with an array of arrays,
and should implement the following methods:

  next(): returns the next element in the array of arrays. If there are no
          more elements, raise an exception.
  has_next(): returns whether or not the iterator still has elements left.

For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next()
repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
"""


class NoMoreElementsException(Exception):
    pass


class Iterator:
    def __init__(self, array):
        self.__array = array
        self.__pointer_element = 0
        self.__pointer_subarray = 0

    def next(self):
        if not self.has_next():
            raise NoMoreElementsException("no more elements to iterate over")

        subarray = self.__pointer_subarray
        element = self.__pointer_element
        result = None

        if len(self.__array[subarray]) == 0 or element == len(self.__array[subarray]):
            subarray += 1

            while len(self.__array[subarray]) == 0:
                subarray += 1

            result = self.__array[subarray][0]
            element = 1
        else:
            result = self.__array[subarray][element]
            element += 1

        self.__pointer_subarray = subarray
        self.__pointer_element = element
        return result

    def has_next(self):
        length = len(self.__array)
        subarray = self.__pointer_subarray
        element = self.__pointer_element

        if length == 0:
            return False

        if len(self.__array[subarray]) == 0:
            return self.__has_elements_in_next_subarrays(subarray + 1)
        elif element == len(self.__array[subarray]):
            return self.__has_elements_in_next_subarrays(subarray + 1)
        else:
            return True

    def __has_elements_in_next_subarrays(self, start_position):
        length = len(self.__array)
        for i in range(start_position, length):
            subarray = self.__array[i]

            if len(subarray) > 0:
                return True

        return False
