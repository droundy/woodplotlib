import woodplotlib as wood

front = wood.Board(dim = '1x3', feet = 3)
left = wood.Board(dim = '1x2', feet = 2)
left.join(front, 'end-to-near-back')

right = wood.Board(dim = '1x2', feet = 2)
right.join(front, 'end-to-far-back')
#front = wood.Board(dim = '1x2', feet = 3)

leftbrace = wood.Board(dim = '1x2', feet = 1)
leftbrace.join(left, 'end-to-near-right-edge')

leftbrace = wood.Board(dim = '1x2', feet = 1)
leftbrace.join(left, 'end-to-far-right-edge')

rightbrace = wood.Board(dim = '1x2', feet = 1)
rightbrace.join(right, 'end-to-near-right-edge')

rightbrace = wood.Board(dim = '1x2', feet = 1)
rightbrace.join(right, 'end-to-far-right-edge')

wood.show3d()
