class Addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def Calculate(self):
        return self.a+self.b
class Subtraction(Addition):
    def Calculate(self):
        return self.a-self.b
class Multiplication(Subtraction):
    def Calculate(self):
        return self.a*self.b
class Division(Multiplication):
    def Calculate(self):
        return self.a/self.b
while True:
    a=int(input('Enter the First Value:'))
    b=int(input('Enter the Second Value:'))
    print('Please Select the Following any one Operation:\n1.Add\n2.Sub\nMul\nDiv')
    Choices=str(input('Enter Your Choice:'))
    if Choices=='Add':
        Add=Addition(a,b)
        print('Answer is:',Add.Calculate())
        break
    elif Choices=='Sub':
        Sub=Subtraction(a,b)
        print('Answer is:',Sub.Calculate())
        break
    elif Choices=='Mul':
        Mul=Multiplication(a,b)
        print('Answer is:',Mul.Calculate())
        break
    elif Choices=='Div':
        Div=Division(a,b)
        print('Answer is:',Div.Calculate())
        break
    else:
        print('Invalid Input')
        break