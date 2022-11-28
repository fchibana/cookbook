import math
from scipy.spatial.transform import Rotation as R

# row = pitch = yaw = 0
r1 = R.from_euler("z", math.pi / 3)

# row = pitch = 0; yaw = pi/4
r2 = R.from_euler("z", math.pi / 4)

print(f"R1: {r1.as_euler('xyz', degrees=True)}")
print(f"R2: {r2.as_euler('xyz', degrees=True)}")

# add rotations
dr = r1 * r2
print(f"R1.R2 = {dr.as_euler('xyz', degrees=True)}")

# subtract rotations
dr = r1 * r2.inv()
print(f"R1.R2^(-1) = {dr.as_euler('xyz', degrees=True)}")

# subtract rotations
dr = r1.inv() * r2
print(f"R1^(-1).R2 = {dr.as_euler('xyz', degrees=True)}")

# subtract rotations
dr = r2 * r1.inv()
print(f"R2.R1^(-1) = {dr.as_euler('xyz', degrees=True)}")