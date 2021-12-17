
target_y = [-114, -75]
# steps/2 is between 75 and 114
n = 114
steps = n*2

# velocity_y = steps - (2*y)/steps

# (vy+1)*n/2 = (n-1+1)*n/2
# vy = n-1

vy = n-1

print("Top of the arc at y = {}".format(vy*n/2))

# py = 0
# for step in range(steps):
#     py += vy - step
#     if
#     print(py)
# print("final {}".format(py))
