# Viva Voce Examination Questions & Answers
**Course:** BTech Linear Algebra & Multivariable Calculus (M3)  
**Project:** Understanding Partial Derivatives Through 3D Surface Visualization  
**Target Topic:** Partial Derivatives of Two-Variable Functions  

---

### Q1: What is a two-variable function, and what does its graph represent in $\mathbb{R}^3$?
**Answer:** A two-variable function $f: \mathbb{R}^2 \to \mathbb{R}$ is a mathematical rule that assigns a unique real scalar output $z = f(x, y)$ to every ordered coordinate pair $(x, y)$ in its domain. Geometrically, plotting all points $(x, y, f(x, y))$ in three-dimensional Euclidean space forms a continuous, curved 2D surface sitting in 3D space.

---

### Q2: Why can we not simply define a single ordinary derivative for a function of two variables like we do in single-variable calculus?
**Answer:** In single-variable calculus ($y = f(x)$), the input $x$ resides on a one-dimensional line, so there is only one axis of motion (left or right). However, in multivariable calculus ($z = f(x, y)$), the input $(x, y)$ resides on a 2D plane. From any point, there are infinitely many distinct directions along which one could move. Therefore, we must specify the direction of movement. Partial derivatives represent the fundamental rates of change specifically parallel to the coordinate axes.

---

### Q3: What is the formal mathematical limit definition of $\frac{\partial f}{\partial x}$?
**Answer:** At a point $(a, b)$, the partial derivative with respect to $x$ is defined as:
$$f_x(a, b) = \frac{\partial f}{\partial x}(a, b) = \lim_{h \to 0} \frac{f(a+h, b) - f(a, b)}{h}$$
In this difference quotient, the $y$-coordinate is fixed at $b$, and only $x$ is given an incremental displacement $h$.

---

### Q4: What does "holding one variable constant" mean algebraically and geometrically?
**Answer:**
- **Algebraically:** We treat that variable as an invariant numerical scalar (like 5 or $\pi$), meaning its derivative is zero, and when multiplied by the other variable, it acts as a constant coefficient.
- **Geometrically:** It corresponds to intersecting the 3D surface $z = f(x, y)$ with a vertical cutting plane parallel to one of the coordinate planes (e.g., $y = b$ or $x = a$). The resulting intersection is a 1D curve (trace) residing on a 2D plane.

---

### Q5: For the central project function $f(x, y) = x^2 + xy + y^2$, explain how you differentiate the middle term $xy$ with respect to $x$.
**Answer:** When differentiating with respect to $x$, $y$ is treated as a constant scalar factor. Using the constant multiple rule of differentiation $\frac{d}{dx}[c \cdot g(x)] = c \cdot g'(x)$, where $c = y$ and $g(x) = x$:
$$\frac{\partial}{\partial x}(y \cdot x) = y \cdot \frac{d}{dx}(x) = y \cdot 1 = y$$

---

### Q6: Why is $\frac{\partial}{\partial x}(y^2) = 0$ in $f(x, y) = x^2 + xy + y^2$?
**Answer:** Because $x$ and $y$ are independent coordinate variables. When holding $y$ constant, $y^2$ is also a constant scalar value. The derivative of any constant with respect to an independent variable is identically zero: $\frac{d}{dx}(c) = 0$.

---

### Q7: What are the exact numerical values of $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$ for $f(x, y) = x^2 + xy + y^2$ at the point $(1, 2)$?
**Answer:**
1. With respect to $x$: $\frac{\partial f}{\partial x} = 2x + y$. Substituting $(1, 2)$:
   $$\left. \frac{\partial f}{\partial x} \right|_{(1,2)} = 2(1) + 2 = 4$$
2. With respect to $y$: $\frac{\partial f}{\partial y} = x + 2y$. Substituting $(1, 2)$:
   $$\left. \frac{\partial f}{\partial y} \right|_{(1,2)} = 1 + 2(2) = 5$$

---

### Q8: What is the geometric interpretation of the value $\frac{\partial f}{\partial x}(1, 2) = 4$?
**Answer:** It is the slope of the tangent line to the cross-sectional curve $z = f(x, 2) = x^2 + 2x + 4$ lying in the vertical plane $y = 2$ at the point $(1, 2, 7)$. It means that if we step forward by $1$ unit parallel to the positive $x$-axis from $(1, 2)$, the surface altitude $z$ initially rises at an instantaneous rate of $4$ units.

---

### Q9: What is the formula for the tangent plane to a surface $z = f(x, y)$ at point $(x_0, y_0, z_0)$, and what is its equation for your project example?
**Answer:** The tangent plane formula is:
$$z - z_0 = f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)$$
For our point $(1, 2, 7)$ with $f_x = 4$ and $f_y = 5$:
$$z - 7 = 4(x - 1) + 5(y - 2)$$
Simplifying:
$$z = 4x + 5y - 7 \quad \text{or} \quad 4x + 5y - z = 7$$

---

### Q10: How are the two tangent lines related to the tangent plane?
**Answer:** The tangent line in the $x$-direction (vector $\vec{v}_x = \langle 1, 0, f_x \rangle$) and the tangent line in the $y$-direction (vector $\vec{v}_y = \langle 0, 1, f_y \rangle$) are both tangent to the surface at $P$ and lie completely inside the tangent plane. In fact, their cross product gives the normal vector to the tangent plane:
$$\vec{n} = \vec{v}_x \times \vec{v}_y = \langle 1, 0, f_x \rangle \times \langle 0, 1, f_y \rangle = \langle -f_x, -f_y, 1 \rangle$$

---

### Q11: How does your interactive 3D laboratory demonstrate the transition from a secant line to a tangent line?
**Answer:** The interactive laboratory features an incremental slider $h$ representing the secant difference quotient step size $\frac{f(x+h, y) - f(x, y)}{h}$. As the user drags the $h$ slider from $1.5$ down towards $0$, the secondary point moves closer and closer to $P(x_0, y_0, z_0)$, and the dashed secant line rotates continuously until it merges seamlessly with the solid tangent line. This visually proves the limit definition of the derivative.

---

### Q12: What type of surface does $f(x, y) = x^2 + xy + y^2$ generate? How can you prove its classification?
**Answer:** It is an elliptic paraboloid opening upwards with a global minimum at the origin $(0, 0, 0)$. We prove this using the Second Derivative Test:
- $f_{xx} = 2$, $f_{yy} = 2$, $f_{xy} = 1$
- Discriminant $D = f_{xx}f_{yy} - (f_{xy})^2 = (2)(2) - (1)^2 = 4 - 1 = 3 > 0$
- Since $D > 0$ and $f_{xx} > 0$, the Hessian is positive-definite, confirming that the quadratic form is strictly convex and bowl-shaped.

---

### Q13: In your 3D WebGL implementation, how did you map mathematical coordinates to Three.js coordinates?
**Answer:** In standard Three.js, the $Y$-axis is vertical (pointing up), whereas in multivariable mathematics, the $Z$-axis is traditionally the vertical altitude $z = f(x, y)$. In our custom `SurfaceVisualizer` class, we mapped:
- Three.js $X$ = Mathematical $x$
- Three.js $Y$ = Mathematical height $z = f(x, y)$
- Three.js $Z$ = Mathematical $y$
This orientation allows students to look down onto the $xz$-floor as the domain and see the surface height rise vertically as expected in engineering textbooks.

---

### Q14: How does Clairaut's Theorem (Schwarz's Theorem) apply to mixed second partial derivatives of this function?
**Answer:** Clairaut's theorem states that if the mixed partial derivatives are continuous on an open set containing $(a, b)$, then $f_{xy}(a, b) = f_{yx}(a, b)$. For our polynomial function:
- $f_x = 2x + y \implies f_{xy} = \frac{\partial}{\partial y}(2x + y) = 1$
- $f_y = x + 2y \implies f_{yx} = \frac{\partial}{\partial x}(x + 2y) = 1$
Both are continuous constant functions equal to $1$, satisfying Clairaut's theorem.

---

### Q15: What is the gradient vector $\nabla f(1, 2)$, and what is its geometric relationship to the level curves and the steepest ascent?
**Answer:** The gradient vector $\nabla f$ is composed of the partial derivatives:
$$\nabla f(x, y) = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right\rangle \implies \nabla f(1, 2) = \langle 4, 5 \rangle$$
Geometrically:
1. It points in the direction of greatest initial rate of increase (steepest ascent) on the surface from $(1, 2)$.
2. Its magnitude $|\nabla f| = \sqrt{4^2 + 5^2} = \sqrt{41} \approx 6.403$ is the maximum directional derivative.
3. In the $xy$-domain plane, $\nabla f(1, 2)$ is strictly perpendicular (orthogonal) to the level curve $x^2 + xy + y^2 = 7$ passing through $(1, 2)$.

---

### Q16: How did you ensure visual accessibility and academic clarity across the UI/UX and animation design?
**Answer:**
1. **Color Coding Consistency:** We established a strict chromatic standard: Cyan/Blue exclusively represents the $x$-direction ($y = \text{const}$), Purple represents the $y$-direction ($x = \text{const}$), Amber represents tangent structures, and Red highlights the target point $P(1, 2, 7)$.
2. **Typography & Layout:** We used `Inter` for clean prose, `Fira Code` for numerical readouts, and `KaTeX` for crisp mathematical typesetting.
3. **Pacing:** Explanations build progressively from 3D intuition to 2D slicing, then to algebraic differentiation, and finally to geometric tangent planes.
