
def runner(prgname, testcases):

    for result, inputs in testcases.items():
        answer = prgname(*inputs)
        print(f"Expected({result}): Output: {answer}")


        
