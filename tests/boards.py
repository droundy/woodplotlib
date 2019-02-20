import woodplotlib as wood

a = wood.Board(dim = '1x2', feet = 2)
#a.color = 'r'

c = wood.Board(dim = '1x4', feet = 2)
#c.color = 'tab:orange'
c.join(a, 'end-to-far-left-edge')

b = wood.Board(dim = '1x3', feet = 2)
b.length -= c.width
b.join(a, 'edge-to-left-edge')

d = wood.Board(dim = '1x4', feet = 1)
d.join(c, 'end-to-far-back')

e = wood.Board(dim = '1x4', feet = 1)
e.join(c, 'end-to-near-back')

wood.show3d()
