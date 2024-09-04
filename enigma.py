import numpy as np

# Converte uma mensagem de string para uma representação de matriz one-hot.
def para_one_hot(msg: str, alfabeto: str = "abcdefghijklmnopqrstuvwxyz ") -> np.ndarray:
    N = len(alfabeto)
    T = len(msg)
    one_hot_matrix = np.zeros((N, T))
    
    for i, char in enumerate(msg):
        if char in alfabeto:
            idx = alfabeto.index(char)
            one_hot_matrix[idx, i] = 1
    return one_hot_matrix

# Converte uma matriz one-hot para uma string.
def para_string(M: np.ndarray, alfabeto: str = "abcdefghijklmnopqrstuvwxyz ") -> str:
    indices = np.argmax(M, axis=0)
    return ''.join(alfabeto[idx] for idx in indices)

# Aplica uma cifra simples usando uma matriz de permutação P.
def cifrar(msg: str, P: np.ndarray, alfabeto: str = "abcdefghijklmnopqrstuvwxyz ") -> str:
    M = para_one_hot(msg, alfabeto)
    M_cifrada = P @ M
    return para_string(M_cifrada, alfabeto)

# Recupera uma mensagem cifrada usando a matriz de permutação P.
def de_cifrar(msg: str, P: np.ndarray, alfabeto: str = "abcdefghijklmnopqrstuvwxyz ") -> str:
    M_cifrada = para_one_hot(msg, alfabeto)
    P_inv = np.linalg.inv(P)
    M_recuperada = P_inv @ M_cifrada
    return para_string(M_recuperada, alfabeto)

# Faz a cifra Enigma na mensagem usando os cifradores P e E.
def enigma(msg: str, P: np.ndarray, E: np.ndarray, alfabeto: str = "abcdefghijklmnopqrstuvwxyz ") -> str:
    M = para_one_hot(msg, alfabeto)
    mensagem_cifrada = ""
    
    for i in range(M.shape[1]):
        char_vector = M[:, i:i+1]
        char_cifrado_vector = P @ char_vector
        mensagem_cifrada += para_string(char_cifrado_vector, alfabeto)
        P = E @ P
    
    return mensagem_cifrada

# Recupera uma mensagem cifrada como Enigma assumindo os cifradores P e E.
def de_enigma(msg: str, P: np.ndarray, E: np.ndarray, alfabeto: str = "abcdefghijklmnopqrstuvwxyz ") -> str:
    M_cifrada = para_one_hot(msg, alfabeto)
    mensagem_recuperada = ""
    P_inv = np.linalg.inv(P)
    E_inv = np.linalg.inv(E)
    
    for i in range(M_cifrada.shape[1]):
        char_vector = M_cifrada[:, i:i+1]
        char_recuperado_vector = P_inv @ char_vector
        mensagem_recuperada += para_string(char_recuperado_vector, alfabeto)
        P_inv = P_inv @ E_inv
    
    return mensagem_recuperada
