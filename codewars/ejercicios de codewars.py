"""
En este kata se requiere que, dada una cadena, reemplace cada letra con su posición en el alfabeto.

Si algo en el texto no es una letra, ignórelo y no lo devuelva.

"a" = 1, "b" = 2etc.
"""

# def alphabet_position(string:str,letters_minus="abcdefghijklmnopqrstuvwxyz",letters_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
#     position = ""
#     for l in string:
#         if l in letters_minus:
#             position += str(letters_minus.index(l)+1) + " "
#         elif l in letters_mayus:
#             position += str(letters_mayus.index(l)+1) + " "
#     position = position[:len(position)-1]
#     return position

# print(alphabet_position("The sunset sets at twelve o' clock."))

"""
Dado el triángulo de números impares consecutivos:
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calcule la suma de los números en la enésima fila de este triángulo (comenzando en el índice 1), por ejemplo:
row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
"""
# def row_sum_odd_numbers(n):
#     return n ** 3
    
# print(row_sum_odd_numbers(1))
# print(row_sum_odd_numbers(2))
# print(row_sum_odd_numbers(3))
# print(row_sum_odd_numbers(4))
# print(row_sum_odd_numbers(5))
# print(row_sum_odd_numbers(6))

""" 
Encuentra la letra que falta

Escriba un método que tome una matriz de letras consecutivas (crecientes) como entrada y 
que devuelva la letra que falta en la matriz.

Siempre obtendrá una matriz válida. 
Y siempre faltará exactamente una letra. La longitud de la matriz siempre será de al menos 2.
La matriz siempre contendrá letras en un solo caso.

Ejemplo:

['a', 'b', 'c', 'd', 'f'] -> 'e' ['O', 'Q', 'R', 'S'] -> 'P'
"""
"""
def find_missing_letter(v,alfabet="abcdefghijklmnopqrstuvwxyz"):
    if not v[0].islower():
        alfabet = alfabet.upper()
    alfabet = alfabet[alfabet.index(v[0]):alfabet.index(v[-1])+1]
    for alfab in alfabet:
        if not alfab in v:
            return alfab
# print(find_missing_letter(["a","b","d"]))
# print(find_missing_letter(["O","Q","R","S"]))
# print(find_missing_letter(["P","Q","S"]))
#print(find_missing_letter(["l","n","o"]))
"""

"""
Escriba un algoritmo que identifique direcciones IPv4 válidas en formato decimal de punto. Las IP deben considerarse válidas si constan de cuatro octetos, con valores entre 0y 255, inclusive.

Ejemplos de entradas válidas:
Examples of valid inputs:
1.2.3.4
123.45.67.89
Ejemplos de entrada no válida:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Notas:
Los ceros iniciales (p 01.02.03.04. Ej. ) Se consideran inválidos
Se garantiza que las entradas sean una sola cadena
"""
# def is_valid_IP(address:str):
#     if len(address) == 0:return False
#     address = address.split(".")
#     for octeto in address:
#         if octeto[0] == "0" or not len(address) == 4 or octeto.isalpha() or int(octeto) > 255 or int(octeto) <= -1:
#             return False
#     return True

# print(is_valid_IP(""))
# print(is_valid_IP("abc.dsd.frr.FGg"))
# print(is_valid_IP("12.34.56.-1"))
# print(is_valid_IP("1.2.3"))
# print(is_valid_IP("123.45.67.89"))
# print(is_valid_IP("01.02.03.04"))
# print(is_valid_IP("123.045.067.089"))
# print(is_valid_IP("256.1.2.3"))

# def create_phone_number(a:list):
#     if len(a) == 10: 
#         return "("+str(a[0])+str(a[1])+str(a[2])+")"+str(a[3])+str(a[4])+str(a[5]) + "-"+str(a[6])+str(a[7])+str(a[8])+str(a[9])

# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

"""
    The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""

# def rgb(r, g, b):
#     if r < 0 :
#         r = 0
#     if r > 255:
#         r = 255
#     if g <0:
#         g = 0
#     if g > 255:
#         g = 255
#     if b < 0:
#         b = 0
#     if b > 255:
#         b = 255
#     vh = f"{hex(r)}{hex(g)}{hex(b)}".upper()
#     vh = ["0"+v if len(v) == 1 else v[0:2] for v in vh.split("0X")]
#     return vh[1]+vh[2]+vh[3]

# print(rgb(1,2,3))
# print(rgb(255, 255, 255))
# print(rgb(255, 255, 300))
# print(rgb(0,0,0))
# print(rgb(148, 0, 211))

"""
Complete la solución para que divida la cadena en pares de dos caracteres. 
Si la cadena contiene un número impar de caracteres, 
entonces debe reemplazar el segundo carácter faltante del par final con un guión bajo ('_').

Ejemplos:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""
# def solution(s):
#     if len(s) %2 != 0:
#         s += "_"
#     return [s[c:c+2] for c in range(0,len(s),2)]

# print(solution("abc"))

"""
Cuente el número de duplicados
Escriba una función que devuelva el recuento de caracteres alfabéticos y dígitos numéricos distintos que no distinguen entre mayúsculas y minúsculas que aparecen más de una vez en la cadena de entrada. Se puede suponer que la cadena de entrada contiene solo alfabetos (mayúsculas y minúsculas) y dígitos numéricos.

Ejemplo
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibilidad" -> 1 # 'i' occurs six times
"Indivisibilidades" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""

# def duplicate_count(text:str):
#     l = []
#     text = text.lower()
#     cont = 0
#     for c in text:
#         if text.count(c) > 1 and not c in l:
#             cont += 1
#             l.append(c)
#     return cont
    
# print(duplicate_count("PYw73tMdNWFQeUEvTr6CvUzmakEhvksWiw5ouP6rQHo3OE"))


"""
Probablemente conozca el sistema "Me gusta" de Facebook y otras páginas. Las personas pueden "dar me gusta" a publicaciones de blogs, imágenes u otros elementos. Queremos crear el texto que debería mostrarse junto a dicho elemento.

Implemente la función likesque toma una matriz que contiene los nombres de las personas a las que les gusta un elemento. Debe devolver el texto de la pantalla como se muestra en los ejemplos:

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
Para 4 o más nombres, el número and 2 otherssimplemente aumenta.
"""

# def likes(names):
#     message = 'no one likes this'  if len(names) == 0 else f"{names[0]} likes this" if len(names) == 1 else f"{names[0]} and {names[1]} like this" if len(names) == 2 else f"{names[0]}, {names[1]} and {names[2]} like this" if len(names) == 3 else f"{names[0]}, {names[1]} and {len(names)-2} others like this"
#     return  message
# print(likes([]))


"""
Escriba una función nombrada first_non_repeating_letterque tome una entrada de cadena y devuelva el primer carácter que no se repite en ninguna parte de la cadena.

Por ejemplo, si se le da la entrada 'stress', la función debería regresar 't', ya que la letra t solo aparece una vez en la cadena y aparece primero en la cadena.

Como desafío adicional, las letras mayúsculas y minúsculas se consideran el mismo carácter , pero la función debe devolver el caso correcto para la letra inicial. Por ejemplo, la entrada 'sTreSS'debería regresar 'T'.

Si una cadena contiene todos los caracteres que se repiten , debe devolver una cadena vacía ( "") o None- vea pruebas de muestra.
"""

# def first_non_repeating_letter(string:str):
#     string2 = string.lower()
#     for c in range(len(string2)):
#         if string2.count(string2[c]) == 1:
#             return string[c] 
#     return ""

# print(first_non_repeating_letter("sTreSS"))



"""
Polycarpus trabaja como DJ en la mejor discoteca de Berland y, a menudo, utiliza música dubstep en su actuación. Recientemente, ha decidido tomar un par de canciones antiguas y hacer remixes de dubstep a partir de ellas.

Supongamos que una canción consta de varias palabras (que no contienen WUB). Para hacer el remix dubstep de esta canción, Polycarpus inserta un cierto número de palabras "WUB" antes de la primera palabra de la canción (el número puede ser cero), después de la última palabra (el número puede ser cero) y entre palabras ( al menos una entre cualquier par de palabras vecinas), y luego el niño pega todas las palabras, incluido "WUB", en una cuerda y toca la canción en el club.

Por ejemplo, una canción con las palabras "I AM X" se puede transformar en un remix de dubstep como "WUBWUBIWUBAMWUBWUBX" y no se puede transformar en "WUBWUBIAMWUBX".

Recientemente, Jonny escuchó la nueva pista de dubstep de Polycarpus, pero como no le gusta la música moderna, decidió averiguar cuál era la canción inicial que Polycarpus remezcló. Ayuda a Jonny a restaurar la canción original.

Aporte
La entrada consiste en una sola cadena no vacía, que consta solo de letras mayúsculas en inglés, la longitud de la cadena no excede los 200 caracteres

Producción
Devuelve las palabras de la canción inicial que Polycarpus usó para hacer un remix de dubsteb. Separe las palabras con un espacio.

Ejemplos de
song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND
"""
# def song_decoder(song:str,a = ""):
#     s=  song.split("WUB")
#     for i in range(len(s)):
#         if not s[i] == "":
#             a += s[i]+" "
#     return a[0:len(a)-1]
    
# print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))

"""
La codicia es un juego de dados que se juega con cinco dados de seis caras. Su misión, si decide aceptarla, es marcar un lanzamiento de acuerdo con estas reglas. Siempre se le dará una matriz con cinco valores de dados de seis lados.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
Un solo dado solo se puede contar una vez en cada tirada. Por ejemplo, un "5" dado solo puede contar como parte de un triplete (contribuyendo a los 500 puntos) o como un solo 50 puntos, pero no ambos en la misma tirada.

Puntuación de ejemplo

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
En algunos idiomas, es posible mutar la entrada a la función. Esto es algo que nunca debes hacer. Si modifica la entrada, no podrá aprobar todas las pruebas."""

# def score(dice:list):
#     points = {1:(100,1000),2:200,3:300,4:400,5:(50,500),6:600}
#     value_examin = set()
#     point_total = 0
#     for n in dice:
#         if not n in value_examin:
#             c_repeat = 0
#             x = dice.count(n)
#             for i in range(x):
#                 c_repeat += 1
#                 if c_repeat == 3:
#                     if n == 1:
#                         point_total += points[1][1]
#                     elif n == 5:
#                         point_total += points[5][1]
#                     else:
#                         point_total += points[n]
#                     c_repeat = 0
#             if n == 1 and c_repeat in (1,2):
#                 point_total += points[1][0] * c_repeat
#             elif n == 5 and c_repeat in (1,2):
#                 point_total += points[5][0] * c_repeat
#             value_examin.add(n)
#     return point_total
    
# print(score([1,1,1,2,1]))
# print(score([4, 4, 4, 3, 3]))

"""
Implemente una función que reciba dos direcciones IPv4 y devuelva la cantidad de direcciones entre ellas (incluida la primera,
excluida la última).

Todas las entradas serán direcciones IPv4 válidas en forma de cadenas. La última dirección siempre será mayor que la primera.
"""
# def ips_between(start:str, end:str):
#     x1,x2 = start.split(".")[-1],end.split(".")[-1]
#     x1,x2 = int(x1),int(x2)
#     x3 = 0
#     if x1 > x2 and x2 != 0:
#         x3 = x1 -x2
#     elif x2 > x1 and x1 != 0:
#         x3 = x2 -x1
#     elif x1 == 0 and x2 == 0:
#         x3 = 256
#     elif x1 == 0 and x2 != 0:
#         x3 = 256 -x2
#     elif x1 != 0 and x2 == 0:
#         x3 = 256 - x2
#     return x3

# print(ips_between("10.0.0.0", "10.0.0.50"))#  ==   50 
# print(ips_between("10.0.0.0", "10.0.1.0"))#   ==  256 
# print(ips_between("20.0.0.10", "20.0.1.0"))#  ==  246

"""
En este ejemplo, debe validar si una cadena de entrada de usuario es alfanumérica. La cadena dada no nil/null/NULL/Nonelo es , por lo que no tiene que verificar eso.

La cadena tiene las siguientes condiciones para ser alfanumérica:

Al menos un carácter ( ""no es válido)
Los caracteres permitidos son letras latinas mayúsculas / minúsculas y dígitos del 0a9
Sin espacios en blanco / subrayado
"""

# def alphanumeric(password:str):
#     return password.isalnum()

# print(alphanumeric("PassWr0od1"))

"""
En este kata, debe crear todas las permutaciones de una cadena de entrada y eliminar los duplicados, si están presentes. Esto significa que debe mezclar todas las letras de la entrada en todos los órdenes posibles.

Ejemplos:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
El orden de las permutaciones no importa.
"""
# def permutations(string:str):
#     from itertools import permutations 
#     p = {string,string[::-1]}
#     t_p = permutations(string,len(string))
#     x=""
#     for i in t_p:
#         for j in i:
#             x += j
#         p.add(x)
#         x = ""
#     return list(p)

# print(permutations('a'))


"""
Una potencia perfecta es una clasificación de números enteros positivos:

En matemáticas, una potencia perfecta es un número entero positivo que se puede expresar como una potencia entera de otro número entero positivo. Más formalmente, n es una potencia perfecta si existen números naturales m> 1 y k> 1 tales que m k = n.

Su tarea es verificar si un número entero es una potencia perfecta. Si es una potencia perfecta, devuelve un par my kcon m k = n como prueba. De lo contrario, volver Nothing, Nil, null, NULL, Noneo el equivalente en su idioma.

Nota: Para una potencia perfecta, puede haber varios pares. Por ejemplo 81 = 3^4 = 9^2, así (3,4)y (9,2)son soluciones válidas. Sin embargo, las pruebas se encargan de esto, por lo que si un número es una potencia perfecta, devuelve cualquier par que lo demuestre.

Ejemplos de
isPP(4) => [2,2]
isPP(9) => [3,2]
isPP(5) => None
"""
# def isPP(n):
#     for m in range(2,n+1):
#         for k in range(2,n+1):
#             if m**k == n:
#                 return [m,k]
#     return None

# print(isPP(4))
# print(isPP(9))
# print(isPP(5))