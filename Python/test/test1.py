class test_class:
    def __init__(self) -> None:
        pass
    
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        print(23)
        
    def other_function(self, num):
        return(num + 2)
        
test_object = test_class()

test_object.finalValueAfterOperations(['hello', 'bye'])

print(test_object.other_function(5))

another_num = 28

