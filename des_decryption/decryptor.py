from keys import generate_keys
import permutations

def xor(i1, i2):
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(i1, i2))

def f(r, k):
    e_r = ''.join([r[i - 1] for i in permutations.e])
    k_e = xor(e_r, k)
    
    groups = [k_e[i:i+6] for i in range(0, 48, 6)]
    res = ""

    for num, group in enumerate(groups):
        f_bit = group[0]
        l_bit = group[-1]
        
        row = int(f_bit + l_bit, 2)
        col = int(group[1:-1], 2)

        s_res = permutations.s[num + 1][row][col]
        res += bin(s_res)[2:].zfill(4)

    return ''.join([res[i-1] for i in permutations.p])

def main():
    encrypted_text = "1100101011101101101000100110010101011111101101110011100001110011"
    key = "0100110001001111010101100100010101000011010100110100111001000100"

    list_keys = generate_keys(key)
    
    # To do DES decryption, apply initial permutation
    # Split to left and right keys
    # Ln = Rn - 1
    # Rn = Ln - 1 + f(Rn-1, K16-n)
    # Apply ip_1

    layer = ''.join([encrypted_text[i-1] for i in permutations.ip])

    half = len(layer) // 2
    prev_left = layer[:half]
    prev_right = layer[half:]

    for i in range(16):
        k = list_keys.pop()
       
        new_left = prev_right
        
        f_value = f(prev_right, k)
        new_right = xor(prev_left, f_value)
        
        prev_left = new_left
        prev_right = new_right

    layer16 = new_right + new_left
    final = ''.join([layer16[i-1] for i in permutations.ip_1])
    
    text = ''.join(chr(int(final[i:i+8], 2)) for i in range(0, len(final), 8))
    print(text) # UNDIRISH

if __name__ == '__main__':
    main()
