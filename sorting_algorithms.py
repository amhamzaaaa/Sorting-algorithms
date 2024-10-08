class Sorting:
    def __init__(self):
        pass

    def bubbleSort(self, array: list)-> list:
        """
        this algorithm works like:
        it picks the current value and compare it with the next value (adjecent)
        if current value is smaller than the next value then it swaps the adjecent values
        """
        self.array = array

        for i in range(len(self.array)-1):
            for j in range(len(self.array)-1-i):

                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
        
        return self.array
    
    def selectionSort(self, array: list)-> list:
        """
        this algorithm works like:
        it saves the current value's index as smallest value's index then it finds the 
        smallest value on the basis of current value when it finds the smallest value 
        then it swaps the current value with the smallest value and the smallest value comes at start
        """
        self.array = array

        for i in range(len(self.array)):

            index_of_min_value = i

            for j in range(i,len(self.array)):
                if self.array[j] < self.array[i]:
                    index_of_min_value = j
                
            self.array[i], self.array[index_of_min_value] = self.array[index_of_min_value], self.array[i]

        return self.array
    
    def insertionSort(self, array: list)-> list:
        """
        this algorithm works like:
        it assumes that list is already partially sorted (first value sorted) and starts from 2nd value
        it picks the current value and compares it with the previous sorted value as it finds the current value
        smaller than previous it swaps the current value with the previous if not then moves for the next value
        and considers it sorted
        """
        
        self.array = array

        for i in range(1, len(self.array)):

            while i > 0:
                if self.array[i] < self.array[i-1]:
                    self.array[i], self.array[i-1] = self.array[i-1], self.array[i]
                    i -= 1
                else:
                    break

        return self.array
    
    def mergeSort(self, array: list)-> list:

        self.array = array
        pass



arr = [1,2,6,4,3,9,7,8,9,90]
a = Sorting()
print(a.bubbleSort(arr))
print(a.selectionSort(arr))
print(a.insertionSort(arr))
