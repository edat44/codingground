from itertools import product

def main():
    inputs = [6, 9, 20]
    inputs.sort()
    inputs.reverse()
    totals = [];
    combinations(*inputs)
    for num in combinations(*inputs):
        totals.append(num)
        totals = list(set(totals))
        totals.sort()
        length = len(totals)
        #print length
        #print totals
        result = foundResult(totals)
        if result != False:
            print "Found a result: ", result
            print totals
            break
        

def foundResult(totals):
    length = len(totals)
    results = []
    if length >= 6:
        inOrder = 0
        for i in xrange(length - 1):
            dif = totals[i+1] - totals[i]
            #print totals[i+1], " - ", totals[i], " = ", dif
            if (dif) > 1:
                inOrder = 0
            else:
                inOrder += 1
            if inOrder == 6:
                results.append(totals[i] - 6)
        if len(results) > 0:
            return results
        return False
    return False
        

def combinations(*inputs):
    numbers = list(inputs)
    numLists = [0] * len(numbers)
    num = lcm(*numbers)
    for i in xrange(len(numbers)):
        multiples = range(0, (num + numbers[i]), numbers[i])
        numLists[i] = multiples

    for items in product(*numLists):
        summ = sum(items)
        yield summ
    
    '''
    multipliers = [0] * len(numbers)
    for i in xrange(len(numbers)):
        for j in xrange(0, (num + numbers[i]) / numbers[i]):
            multipliers[i] = j
            summ = 0
            for k in xrange(len(numbers)):
                print multipliers[k], " ", numbers[k], " = ", numbers[k] * multipliers[k]
                summ += numbers[k] * multipliers[k]
            print summ
            print
            yield summ
    '''
    
    '''     
    for i in xrange(0, num, a):
        for j in xrange(0, num, b):
            for k in xrange(0, num, c):
                summ = i + j + k
                #print i, j, k, ":\t", summ
                yield summ
    '''
    

# Greatest common divisor of more than 2 numbers.
def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from fractions import gcd
    return reduce(gcd, numbers)

# Least common multiple is not in standard libraries? It's in gmpy, but this is simple enough:
def lcm(*numbers):
    """Return lowest common multiple."""    
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)

def clear(num):
    print("\n" * num)

main()