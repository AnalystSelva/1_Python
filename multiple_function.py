class SubfieldsInAI():
    def subfields(self):
        list_data = ['Machine Learning', 'Neural Networks', 'VisionRobotics',
                     'Speech Processing', 'Natural Language Processing']

        print('Sub-fields in AI are:')

        for i in list_data:
            print(i)
    def oddEven(self):
        number = int(input("Enter the number:"))
        if number % 2 == 0:
            print(f"{number} is even number")
        else:
            print(f"{number} is odd number")
    def Elegible(self):
        gender = input("Your Gender:")
        age = int(input("Your Age:"))
        if (gender == 'Male' and str(age) >= '21') | (gender == 'Female' and str(age) >= '18'):
            print(f"Eligible")
        else:
            print(f"Not Eligible")
    def percentage(self):
        subject1 = int(input('subject1:'))
        subject2 = int(input('subject2:'))
        subject3 = int(input('subject3:'))
        subject4 = int(input('subject4:'))
        subject5 = int(input('subject5:'))
        total = subject1 + subject2 + subject3 + subject4 + subject5
        print('Total', total)
        average = total / 5
        print('Average', average)
        
    def triangle(self):
        height = int(input('height:'))
        breadth = int(input('Breadth:'))
        print("Area of formula: (Height*Breadth)/2")
        triangle = (height * breadth) / 2
        print('Area of Triangle:', triangle)
        height1 = int(input('height1:'))
        height2 = int(input('height2:'))
        breadth = int(input('breadth:'))
        print('Perimeter formula: Height1+Height2+Breadth')
        perimeter = height1 + height2 + breadth
        print('Perimeter of Triangle:', perimeter)