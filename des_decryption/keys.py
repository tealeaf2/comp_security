import permutations

def left_shift(amount, key):
    return key[amount:] + key[:amount]

def permute(key_combined):
    return ''.join([key_combined[i-1] for i in permutations.pc2])

def generate_keys(key):
    # apply first permutation, which already drops every 8th bit
    # Split the permuted keys into left and right halves, C0 and D0
    # Do shifts for left and right key based on their layer
    # Do permutations after shifts based on their layer to generate keys

    key_layer0 = ''.join([key[i-1] for i in permutations.pc1])

    half = len(key_layer0) // 2
    c0 = key_layer0[:half]
    d0 = key_layer0[half:]

    # print(c0, d0, len(c0), len(d0))

    # Starts from 0
    iterations = [[c0, d0]]
    keys = []

    for layer in range(16):
        amount = permutations.shift[layer]
        c, d = iterations[-1]
        c_shifted = left_shift(amount, c)
        d_shifted = left_shift(amount, d)
        
        iterations.append([c_shifted, d_shifted])
        
        permuted_key = permute(c_shifted + d_shifted)
        keys.append(permuted_key)
    
    #print(keys)
    return keys
