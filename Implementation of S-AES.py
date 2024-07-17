# S-AES Parameters
SBOX = [[0x9, 0x4, 0xA, 0xB],[0xD, 0x1, 0x8, 0x5],[0x6, 0x2, 0x0, 0x3],[0xC, 0xE, 0xF, 0x7]]

INV_SBOX = [[0xA, 0x5, 0x9, 0xB],[0x1, 0x7, 0x8, 0xF],[0x6, 0x0, 0x2, 0x3],[0xC, 0x4, 0xD, 0xE]]

MIXCOL_MATRIX = [[1, 4],[4, 1]]

def sub_bytes(state):
    return [[SBOX[b >> 4][b & 0x0F] for b in row] for row in state]

def shift_rows(state):
    return [state[0], state[1][1:] + state[1][:1]]

def mix_columns(state):
    return [
        [(state[0][0] ^ 4 * state[1][0]) & 0xF, (state[0][1] ^ 4 * state[1][1]) & 0xF],
        [(state[1][0] ^ 4 * state[0][0]) & 0xF, (state[1][1] ^ 4 * state[0][1]) & 0xF]
    ]

def add_round_key(state, round_key):
    return [[state[i][j] ^ round_key[i][j] for j in range(2)] for i in range(2)]

def key_expansion(key):
    round_keys = [key]
    for i in range(1, 3):
        round_keys.append([
            [round_keys[i-1][0][0] ^ SBOX[round_keys[i-1][1][1] >> 4][round_keys[i-1][1][1] & 0x0F] ^ (0x8 >> (i-1)), round_keys[i-1][0][1] ^ round_keys[i-1][0][0]],
            [round_keys[i-1][1][0] ^ round_keys[i-1][0][1], round_keys[i-1][1][1] ^ round_keys[i-1][1][0]]
        ])
    return round_keys

def encrypt(plaintext, key):
    state = plaintext
    round_keys = key_expansion(key)
    
    state = add_round_key(state, round_keys[0])
    
    for i in range(1, 2):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[i])
    
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[2])
    
    return state

# Example Usage
plaintext = [[0x3, 0x6], [0x7, 0x9]]
key = [[0x2, 0x4], [0x6, 0x8]]

ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
