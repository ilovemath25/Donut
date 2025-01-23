# **Donut in Python**

### **Used Libraries**
- **`math`**: For trigonometry (e.g., sine, cosine).
- **`os`**: For clearing terminal.

---

### **How It Works**

**1. Define the Display and Torus Dimensions**
```python
W, H = 40, 30   # Width and height of the ASCII grid (terminal display size)
R1, R2 = 10, 5  # Radius and thickness of the torus
ax = 0          # Initial rotation angle
```
- `W` and `H`: The resolution of the ASCII grid.
- `R1`: Radius of the torus.
- `R2`: Thickness of the torus.
- `ax`: Rotation angle.

---

**2. Initialize the Grid and Z-Buffer**
```python
grid = [["  " for _ in range(W)] for _ in range(H)]   # 2D grid for ASCII characters
z_buffer = [[0 for _ in range(W)] for _ in range(H)]  # 2D grid for depth values
```
- The `grid` holds the ASCII characters to display the donut.
- The `z_buffer` stores depth (`z`) values for each pixel to manage overlapping points.

---

**3. Loop Through Torus Points**
```python
i = 0
while i < 2 * math.pi:                             # Loop around the small circle
    j = 0
    while j < 2 * math.pi:                         # Loop around the large circle
        x = (R1 + R2 * math.cos(i)) * math.cos(j)  # 3D x-coordinate
        y = (R1 + R2 * math.cos(i)) * math.sin(j)  # 3D y-coordinate
        z = R2 * math.sin(i)                       # 3D z-coordinate
```
- `i` and `j`: Represent angles around the small and large circles of the torus.
- The parametric equations generate 3D coordinates (`x`, `y`, `z`) for each point on the torus.

---

**4. Apply Rotation**
```python
yr = z * math.sin(ax) + y * math.cos(ax)   # Rotate y-axis
zr = z * math.cos(ax) - y * math.sin(ax)   # Rotate z-axis
xr = x * math.cos(ax) - yr * math.sin(ax)  # Rotate x-axis
yr = x * math.sin(ax) + yr * math.cos(ax)  # Adjust rotation
```
- Uses trigonometric transformations to rotate points around the y-axis.
- `ax` changes continuously to create the spinning animation.

---

**5. Project 3D Points to 2D**
```python
X = int((xr + W // 2))  # Map 3D x to 2D grid's X-coordinate
Y = int((yr + H // 2))  # Map 3D y to 2D grid's Y-coordinate
```
- Translates and scales the rotated 3D points into 2D coordinates for the grid.

---

**6. Compute Lighting and Shading**
```python
nx = math.cos(i) * math.cos(j)                  # Surface normal x-component
ny = math.cos(i) * math.sin(j)                  # Surface normal y-component
nz = math.sin(i)                                # Surface normal z-component
ny_rot = nz * math.sin(ax) + ny * math.cos(ax)  # Rotate normal for lighting
nz_rot = nz * math.cos(ax) - ny * math.sin(ax)  # Adjust rotation
L = ny_rot - nz_rot / 2                         # Compute brightness (dot product with light source)
luminance_index = int(L * 8)                    # Map brightness to ASCII index
```
- Computes the surface normal at each point.
- Simulates lighting by taking the dot product of the normal with a light direction.
- Maps brightness levels to an ASCII character set (`".,-~:;=!*#$@"`).

---

**7. Update the Grid and Z-Buffer**
```python
if z_buffer[Y % H][X % W] == 0 or z_buffer[Y % H][X % W] > zr:
    z_buffer[Y % H][X % W] = zr                                    # Update depth buffer
    grid[Y % H][X % W] = 2 * ".,-~:;=!*#$@"[luminance_index % 12]  # Set character
```
- Updates the grid only if the current point is closer to the viewer (`zr` is smaller).
- Ensures proper rendering of overlapping points using the **z-buffer**.

---

**8. Animate the Donut**
```python
os.system("cls")                      # Clear the terminal (use "clear" for Linux/Mac)
for row in grid: print("".join(row))  # Print the grid row by row
ax -= 0.04                            # Increment rotation angle
```
- Clears the terminal and redraws the grid in each iteration.
- Continuously updates the rotation angle (`ax`) for smooth spinning.
