# from fpdf import FPDF


# pdf = FPDF(orientation='P', unit='pt', format='A4')
# pdf.add_page()

# pdf.set_font(family='Times', size=24, style='B')
# pdf.cell(w=0, h=80, txt="Flatmate Bill", border=1, align="C", ln=1)
# pdf.cell(w=100, h=40, txt="Period:", border=1)
# pdf.cell(w=150, h=40, txt="March 2021", border=1)

# pdf.output("bill.pdf")


# class Rectangle:

#     def __init__(self, width, height, x, y):
#         self.width = width
#         self.height = height
#         self.x = x
#         self.y = y

#     def area(self):
#         return self.width * self.height

#     def distance_to_point(self, x, y):
#         dist = ((self.x - x)**2 + (self.y - y)**2) ** 0.5
#         return dist
        
        
#     def time_to_point(self, x, y, speed):
#         dist = self.distance_to_point(x, y)
#         return dist / speed


# if __name__ == "__main__":
    
#     R = Rectangle(width=3, height=4, x=1, y=2)
#     print(R.time_to_point(x=2, y=3, speed=20))