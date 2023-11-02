def findMinElemWithIndex(listForSearch: list):
    min_id = -1
    min_elem = float('inf')  
    
    for idx, elem in enumerate(listForSearch):
        if elem < min_elem:
            min_elem = elem
            min_id = idx
    
    return min_id, min_elem

def findMaxElemWithIndex(listForSearch: list):
    max_id = -1
    max_elem = float('-inf') 
    
    for idx, elem in enumerate(listForSearch):
        if elem > max_elem:
            max_elem = elem
            max_id = idx
    
    return max_id, max_elem

def main():
    listOfData = [11, 14, 22, 33, 7, 88, 123, 345, 64, 10, 5, 55, 66, 44, 20]
    
    min_result = findMinElemWithIndex(listOfData)
    print(f"Min id: {min_result[0]}, Min value: {min_result[1]}")  
    max_result = findMaxElemWithIndex(listOfData)
    print(f"Max id: {max_result[0]}, Max value: {max_result[1]}")  

if __name__ == "__main__":
    main()
