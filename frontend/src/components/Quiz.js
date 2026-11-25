export const quizData = [
  {
    id: 1,
    question: "When evaluating the partial derivative ∂f/∂x of f(x,y), what is the fundamental rule regarding y?",
    options: [
      "y is differentiated normally as if it were x",
      "y is treated as an independent constant",
      "y must always be set equal to zero",
      "y is substituted with 1 before differentiating"
    ],
    correct: 1,
    explanation: "By formal definition, the partial derivative ∂f/∂x analyzes the rate of change strictly along the x-direction. Hence, variable y is held fixed (treated as an unchanging constant)."
  },
  {
    id: 2,
    question: "For f(x,y) = x² + xy + y², what is the derivative of the term 'xy' with respect to x?",
    options: [
      "x",
      "y",
      "2xy",
      "0"
    ],
    correct: 1,
    explanation: "Because y is treated as a constant scalar multiple (like 5x has derivative 5), d/dx [c * x] = c. Therefore, ∂/∂x [y * x] = y."
  },
  {
    id: 3,
    question: "What is the numerical value of ∂f/∂y for f(x,y) = x² + xy + y² evaluated at the point (1, 2)?",
    options: [
      "4",
      "5",
      "7",
      "3"
    ],
    correct: 1,
    explanation: "Differentiating with respect to y treats x as constant: ∂f/∂y = 0 + x + 2y = x + 2y. At (1, 2), ∂f/∂y = 1 + 2(2) = 1 + 4 = 5."
  },
  {
    id: 4,
    question: "What does the partial derivative ∂f/∂x geometrically represent on the 3D surface z = f(x,y)?",
    options: [
      "The volume enclosed under the entire surface",
      "The normal vector pointing perpendicular to the xy plane",
      "The slope of the tangent line to the curve formed by intersecting the surface with the vertical plane y = constant",
      "The curvature of the level curve at the origin"
    ],
    correct: 2,
    explanation: "Geometrically, holding y constant corresponds to slicing the surface with a vertical plane y = b. The intersection is a 2D trace, and ∂f/∂x is the slope of the tangent line to that trace at the given point."
  },
  {
    id: 5,
    question: "At point (1,2,7), given ∂f/∂x = 4 and ∂f/∂y = 5, what is the equation of the tangent plane?",
    options: [
      "z - 7 = 4(x - 1) + 5(y - 2)",
      "z = 4x + 5y",
      "z - 7 = 5(x - 1) + 4(y - 2)",
      "4x + 5y + 7z = 0"
    ],
    correct: 0,
    explanation: "The tangent plane formula is z - z₀ = f_x(x₀,y₀)(x - x₀) + f_y(x₀,y₀)(y - y₀). Substituting x₀=1, y₀=2, z₀=7, f_x=4, f_y=5 gives z - 7 = 4(x - 1) + 5(y - 2)."
  }
];
