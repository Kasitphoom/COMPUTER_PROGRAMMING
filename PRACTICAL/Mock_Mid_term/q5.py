import turtle

t = turtle.Turtle()

def draw_sq(n):
	for i in range(4):
		t.fd(n)
		t.lt(90)

def spiral_sq(s):
	n = s
	t.pu()
	half = 0
	while n > 5:
		half = n / 2
		t.bk(half)
		t.rt(90)
		t.fd(half)
		t.lt(90)
		t.pd()
		draw_sq(n)
		t.pu()
		t.fd(half)
		t.lt(90)
		t.fd(half)
		t.rt(90)
		t.lt(10)
		n *= 0.75

spiral_sq(150)

turtle.done()