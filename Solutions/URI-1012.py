# URI Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1012
# Programmed by Marufur Rahman.

valor = input().split(" ")
a, b, c = valor
pi = 3.14159 # pi number

# Declaring var
triangulo = (float(a) * float(c))/2
circulo = pi * (float(c)* float(c))
trapezio = float(c) *(float(a) + float(b)) / 2
quadrado = float(b) * float(b)
retangulo = float(a) * float(b)


print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (triangulo, circulo, trapezio, quadrado, retangulo))