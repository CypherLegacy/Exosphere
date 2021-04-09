#NAME:  Compound Interest Calculator
#LANGUAGE:  Python
#CREATED BY:  Steven Ahlberg

#Defining the cpdint() function.
def cpdint():
    b = 0
    n = '\n'
    s = '     '
    a = int(input(f'{n}How many accounts do you want to calculate? '))
    while b < a:
        prin = float(input(f"What is the principal amount? "))
        rate = float(input(f"What is the annual interest rate (in decimal format)? "))
        time = int(input(f"What is the duration in years? "))
        number = int(input(f"How many times will interest be compounded each year? (Note: minimum is 1): "))
        print(f'{n*2}{s}FINAL VALUES...')
        print(f'{n*2}{s}Principal = {prin}'); print(f'{s}Interest rate = {rate}'); print(f'{s}Years = {time}');
        print(f'{s}Compounding = {number} time(s) per year{n*2}')

        amt1 = rate / number
        amt2 = time*number
        total = prin*(1+amt1)**amt2
        print(f'Your total is: {total}{n}')
        b = b + 1

#Conditional statement which triggers the program.
if __name__ == '__main__':
    cpdint()
