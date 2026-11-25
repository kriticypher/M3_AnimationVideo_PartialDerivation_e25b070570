# Mathematical Verification Document
**Course:** BTech Linear Algebra and Multivariable Calculus (M3)  
**Topic:** Understanding Partial Derivatives Through 3D Surface Visualization  
**Central Function:** $f(x, y) = x^2 + xy + y^2$  
**Evaluation Point:** $(a, b) = (1, 2)$  

---

## 1. Function Formulation and Point Elevation
We consider the scalar multivariable field:
$$z = f(x, y) = x^2 + xy + y^2$$

### Evaluation at $(1, 2)$:
$$z_0 = f(1, 2) = (1)^2 + (1)(2) + (2)^2 = 1 + 2 + 4 = 7$$
Hence, the target point on the three-dimensional surface is:
$$P(x_0, y_0, z_0) = (1, 2, 7) \quad \checkmark$$

---

## 2. Partial Derivative with Respect to $x$
By formal definition:
$$\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}$$
Here, variable $y$ is treated as an invariant constant scalar ($y = \text{const}$).

### Term-by-term Differentiation:
1. $\frac{\partial}{\partial x}(x^2) = 2x$ (by the single-variable power rule $\frac{d}{dx}[x^n] = n x^{n-1}$).
2. $\frac{\partial}{\partial x}(xy) = y \frac{d}{dx}[x] = y \cdot 1 = y$ (since $y$ is a constant multiplier).
3. $\frac{\partial}{\partial x}(y^2) = 0$ (since $y$ is independent of $x$, $y^2$ is an absolute constant scalar).

Summing the terms:
$$\frac{\partial f}{\partial x} = 2x + y + 0 = 2x + y \quad \checkmark$$

### Numerical Evaluation at $(1, 2)$:
$$\left. \frac{\partial f}{\partial x} \right|_{(1,2)} = 2(1) + 2 = 2 + 2 = 4 \quad \checkmark$$
**Geometric Meaning:** Holding $y=2$ fixed, the intersection of the surface with the plane $y=2$ is the parabola:
$$C_1(x) = f(x, 2) = x^2 + 2x + 4$$
Its derivative is $C_1'(x) = 2x + 2$. At $x=1$, $C_1'(1) = 4$. This is the exact slope of the tangent line in the $x$-direction.

---

## 3. Partial Derivative with Respect to $y$
By formal definition:
$$\frac{\partial f}{\partial y} = \lim_{h \to 0} \frac{f(x, y+h) - f(x, y)}{h}$$
Here, variable $x$ is treated as an invariant constant scalar ($x = \text{const}$).

### Term-by-term Differentiation:
1. $\frac{\partial}{\partial y}(x^2) = 0$ (since $x$ is independent of $y$, $x^2$ is an absolute constant scalar).
2. $\frac{\partial}{\partial y}(xy) = x \frac{d}{dy}[y] = x \cdot 1 = x$ (since $x$ is a constant multiplier).
3. $\frac{\partial}{\partial y}(y^2) = 2y$ (by the single-variable power rule).

Summing the terms:
$$\frac{\partial f}{\partial y} = 0 + x + 2y = x + 2y \quad \checkmark$$

### Numerical Evaluation at $(1, 2)$:
$$\left. \frac{\partial f}{\partial y} \right|_{(1,2)} = 1 + 2(2) = 1 + 4 = 5 \quad \checkmark$$
**Geometric Meaning:** Holding $x=1$ fixed, the intersection of the surface with the plane $x=1$ is the parabola:
$$C_2(y) = f(1, y) = 1 + y + y^2 = y^2 + y + 1$$
Its derivative is $C_2'(y) = 2y + 1$. At $y=2$, $C_2'(2) = 2(2) + 1 = 5$. This is the exact slope of the tangent line in the $y$-direction.

---

## 4. Difference Quotient Limits Verification (First Principles)

### Limit along $x$ at $(1, 2)$:
$$\frac{f(1+h, 2) - f(1, 2)}{h} = \frac{\left[(1+h)^2 + (1+h)(2) + (2)^2\right] - 7}{h}$$
Expand numerator:
$$(1 + 2h + h^2) + (2 + 2h) + 4 - 7 = h^2 + 4h$$
Divide by $h$ ($h \neq 0$):
$$\frac{h(h + 4)}{h} = h + 4$$
Take the limit as $h \to 0$:
$$\lim_{h \to 0} (h + 4) = 4 \quad \checkmark$$

### Limit along $y$ at $(1, 2)$:
$$\frac{f(1, 2+h) - f(1, 2)}{h} = \frac{\left[1^2 + 1(2+h) + (2+h)^2\right] - 7}{h}$$
Expand numerator:
$$1 + (2 + h) + (4 + 4h + h^2) - 7 = h^2 + 5h$$
Divide by $h$ ($h \neq 0$):
$$\frac{h(h + 5)}{h} = h + 5$$
Take the limit as $h \to 0$:
$$\lim_{h \to 0} (h + 5) = 5 \quad \checkmark$$

Both first-principle limits match the differential calculus calculations identically.

---

## 5. Tangent Plane and Surface Normal Vector Verification

The equation of the tangent plane to a surface $z = f(x, y)$ at point $(x_0, y_0, z_0)$ is given by:
$$z - z_0 = f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)$$

Substituting $(x_0, y_0, z_0) = (1, 2, 7)$, $f_x(1, 2) = 4$, and $f_y(1, 2) = 5$:
$$z - 7 = 4(x - 1) + 5(y - 2)$$
Expanding:
$$z - 7 = 4x - 4 + 5y - 10$$
$$z - 7 = 4x + 5y - 14$$
$$z = 4x + 5y - 7 \quad \checkmark$$
Or in standard linear form:
$$4x + 5y - z - 7 = 0$$

### Surface Normal Vector:
Let $F(x, y, z) = x^2 + xy + y^2 - z = 0$.
The gradient vector $\nabla F$ is normal to the level surface:
$$\nabla F = \left\langle \frac{\partial F}{\partial x}, \frac{\partial F}{\partial y}, \frac{\partial F}{\partial z} \right\rangle = \langle 2x + y, \, x + 2y, \, -1 \rangle$$
At $(1, 2, 7)$:
$$\vec{n} = \langle 4, 5, -1 \rangle \quad \text{or upward normal} \quad \vec{n}_{\text{up}} = \langle -4, -5, 1 \rangle \quad \checkmark$$

---

## 6. Hessian Matrix and Local Geometry Check
Second partial derivatives:
$$f_{xx} = \frac{\partial}{\partial x}(2x + y) = 2$$
$$f_{yy} = \frac{\partial}{\partial y}(x + 2y) = 2$$
$$f_{xy} = f_{yx} = \frac{\partial}{\partial y}(2x + y) = 1$$

The Hessian matrix $H$:
$$H = \begin{bmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$
Determinant of Hessian:
$$D = \det(H) = (2)(2) - (1)(1) = 4 - 1 = 3 > 0$$
Since $D > 0$ and $f_{xx} = 2 > 0$, the surface is strictly convex (an elliptic paraboloid), opening upwards with a global minimum at $(0, 0, 0)$.

All calculations and visual models are mathematically sound and verified.
