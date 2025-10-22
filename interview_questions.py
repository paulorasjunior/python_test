# Importe o módulo matemático para acessar funções matemáticas
import  math

# Três maneiras de inverter uma string
def test_invert():
    # Defina a string original
    original_string = "olá"

    # Inverta a string original usando a função reversed()
    # e junte os caracteres novamente em uma nova string

    reversed_string = ''.join(reversed(original_string))

    # Imprima a string invertida
    print(reversed_string)

def test_invert_2():
    # Defina a string original
    original_string = "olá"
    # Inverta a string original usando a função reversed()
    # Nota: reversed() retorna um objeto, não uma string
    reversed_string = reversed(original_string)
    # Declare uma string vazia para construir a string invertida usando um ciclo
    reversed_string_using_loop = ''
    # Crie um ciclo que vai iterar sobre cada caractere no objeto invertido
    for i in reversed_string:
        # Concatene cada caractere ao reversed_string_using_loop
        reversed_string_using_loop = reversed_string_using_loop + i
    # Imprima a string invertida final
    print(reversed_string_using_loop)

# Função que inverte uma string
def reverse_string(word):
    return ''.join(reversed(word))

# Teste. Verificação da função reverse_string
def test_reverse_string():
    input_str = "TripleTen"
    reversed_str = reverse_string(input_str)
    assert reversed_str == "neTelpirT"
    print("Teste Aprovado! " + input_str + " invertido é " + reversed_str)

# Função para verificar palíndromo
def is_palindrome(word):
    # Inverta a string usando reversed() e join().
     reversed_str = ''.join(reversed(word))
     return word == reversed_str

def test_is_palindrome():
    input_str = "osso"
    result = is_palindrome(input_str)
    assert result == True
    print("Teste aprovado! '" + input_str + "' é um palíndromo.")


def compute_factorial(number):
    # Calcule o fatorial de "number" usando a função fatorial interna do Python no módulo math.
    return math.factorial(number)

# Teste. Verificação da função compute_factorial
def test_compute_factorial():
    # Defina o número de entrada
    input_number = 5

    # Realize o cálculo fatorial
    result = compute_factorial(input_number)

    # Verifique se o resultado é igual ao valor fatorial esperado
    assert result == 120

    print("Teste aprovado! O fatorial de " + str(input_number) + " é " + str(result))
