import woodplotlib as wood

a = wood.Board(dim = '1x2', feet = 4)

b = wood.Board(dim = '1x2', feet = 4)
b.origin[0] = 4

wood.show3d()
