def test_function(content):
    print(f'this is an imported function with the parameter: {content}')

class Test:
    def __init__(self):
        self.name = 'my app'
        self.value = 12

    def do_something(self):
        print('hello')

def sum_of_numbers(*nums):
    return sum(nums)
    
            
    

