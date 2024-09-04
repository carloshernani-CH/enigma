# Enigma

## Descrição

Esta biblioteca implementa uma simulação da máquina Enigma usando técnicas de álgebra linear. A biblioteca permite criptografar e descriptografar mensagens usando cifragem simples e Enigma.

## Instalação

Clone o repositório e navegue até o diretório principal.

```bash
git clone https://github.com/carloshernani-CH/enigma
```

## Uso

### Rodando o Demo

Para ver a biblioteca em ação, execute o script `demo.py`:

```bash
python demo.py
```

### Funções Disponíveis

- **para_one_hot(msg: str):** Converte uma mensagem em uma matriz one-hot.
- **para_string(M: np.array):** Converte uma matriz one-hot de volta para uma string.
- **cifrar(msg: str, P: np.array):** Cifra uma mensagem usando uma matriz de permutação.
- **de_cifrar(msg: str, P: np.array):** Decifra uma mensagem cifrada.
- **enigma(msg: str, P: np.array, E: np.array):** Cifra uma mensagem usando o método Enigma.
- **de_enigma(msg: str, P: np.array, E: np.array):** Decifra uma mensagem cifrada pelo método Enigma.

## Modelo Matemático

A cifra simples é implementada como uma multiplicação de matriz:

\[
M_c = P M
\]

onde \(M\) é a matriz one-hot da mensagem e \(P\) é a matriz de permutação.

Para decifrar, usamos a inversa de \(P\):

\[
M = P^{-1} M_c
\]

O método Enigma aplica uma nova permutação a cada caractere cifrado, alterando a matriz de permutação de acordo com um padrão definido.

## Testes

Para executar os testes, use os exemplos fornecidos no script `demo.py`.
