import math, os
W, H = 40, 30
R1, R2 = 10, 5
ax = 0
while True:
   grid = [["  " for _ in range(W)] for _ in range(H)]
   z_buffer = [[0 for _ in range(W)] for _ in range(H)]
   i = 0
   while i < 2*math.pi:
      j = 0
      while j < 2*math.pi:
         x = (R1 + R2*math.cos(i)) * math.cos(j)
         y = (R1 + R2*math.cos(i)) * math.sin(j)
         z = R2*math.sin(i)
         yr = z*math.sin(ax) + y*math.cos(ax)
         zr = z*math.cos(ax) - y*math.sin(ax)
         xr = x*math.cos(ax) - yr*math.sin(ax)
         yr = x*math.sin(ax) + yr*math.cos(ax)
         X = int((xr + W//2))
         Y = int((yr + H//2))
         nx = math.cos(i) * math.cos(j)
         ny = math.cos(i) * math.sin(j)
         nz = math.sin(i)
         ny_rot = nz*math.sin(ax) + ny*math.cos(ax)
         nz_rot = nz*math.cos(ax) - ny*math.sin(ax)
         nx_rot = nx*math.cos(ax) - ny_rot*math.sin(ax)
         ny_rot = nx*math.sin(ax) + ny_rot*math.cos(ax)
         L = ny_rot - nz_rot/2
         luminance_index = int(L*8)
         if(z_buffer[Y%H][X%W]==0 or z_buffer[Y%H][X%W] > zr):
            z_buffer[Y%H][X%W] = zr
            grid[Y%H][X%W] = 2*".,-~:;=!*#$@"[luminance_index%12]
         j+=0.07
      i+=0.07
   os.system("cls")
   for row in grid:print("".join(row))
   ax-=0.04