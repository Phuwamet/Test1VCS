import random
def generate_list():
    alist = [x for x in range(random.randint(-10,10))]
    assert len(alist)>1 ,"alist is NULL"
    assert sum(alist)<100 ,"alist < 100"
    return alist
    
"""
print a generated list
"""
    
def printIt():
    print(generate_list())
    
def main():
    printIt()
    
"""
If this script file is called, it will run main() directly
"""
    
if __name__=='__main__':
    print("Test printIt():")
    main()