# Understanding Partial Derivatives Through 3D Surface Visualization
> *"How changing one variable at a time reveals the behaviour of a multivariable function."*

**Course:** BTech Linear Algebra and Multivariable Calculus (M3)  
**Academic Assessment:** Individual Internal Assessment  
**Candidate:** Individual Student Submission  
**Central Worked Example:** $f(x, y) = x^2 + xy + y^2$ evaluated at $(1, 2)$  

---

## 📌 Executive Overview

This repository hosts a premier, mathematically rigorous, and visually immersive educational project engineered specifically to teach partial differentiation to engineering students.

The project pairs an interactive **Three.js WebGL 3D Laboratory** with a full **1080p Master Video Animation** (approx. 4.8 minutes, synchronized voice narration, 6 distinct pedagogical scenes), a formal **Storyboard PDF**, **Step-by-Step Analytical Verifications**, and an extensive **16-Question Viva Voce Preparation Guide**.

---

## 🎯 Learning Objectives

By exploring this repository and running the application, students will learn:
1. **Multivariable Input-Output Geometry:** How coordinate pairs $(x, y) \in \mathbb{R}^2$ map to elevation $z = f(x, y) \in \mathbb{R}$ forming continuous 3D landscapes.
2. **Concept of Partial Derivatives:** Why infinite directional choices in 2D necessitate isolating orthogonal rates along coordinate axes.
3. **Holding Variables Constant:** How treating $y$ (or $x$) as an invariant scalar slices a 3D surface into a 2D planar cross-sectional curve.
4. **Calculus from First Principles:** The difference quotient limit definition:
   $$f_x(a,b) = \lim_{h \to 0} \frac{f(a+h,b) - f(a,b)}{h}, \quad f_y(a,b) = \lim_{h \to 0} \frac{f(a,b+h) - f(a,b)}{h}$$
5. **Analytical Term-by-Term Differentiation:** Applying power rules and constant rules to multivariable polynomials.
6. **Geometric Tangent Synthesis:** How orthogonal tangent lines with slopes $f_x=4$ and $f_y=5$ span the local tangent plane $z - 7 = 4(x - 1) + 5(y - 2)$.

---

## 🧮 Mathematical Ground Truth Summary

For the model function $f(x,y) = x^2 + xy + y^2$ at point $(1, 2)$:
- **Point Elevation:** $z_0 = f(1, 2) = 1^2 + (1)(2) + 2^2 = 7 \implies P(1, 2, 7)$
- **Partial Derivative w.r.t $x$:**
  $$\frac{\partial f}{\partial x} = 2x + y \implies \left. \frac{\partial f}{\partial x} \right|_{(1,2)} = 2(1) + 2 = 4$$
- **Partial Derivative w.r.t $y$:**
  $$\frac{\partial f}{\partial y} = x + 2y \implies \left. \frac{\partial f}{\partial y} \right|_{(1,2)} = 1 + 2(2) = 5$$
- **Tangent Plane Equation:**
  $$z - 7 = 4(x - 1) + 5(y - 2) \iff z = 4x + 5y - 7$$
- **Normal Vector:** $\vec{n} = \langle -4, -5, 1 \rangle$

---

## 🚀 Key Features

### 1. Interactive 3D WebGL Laboratory (`/frontend`)
- **Real-Time Orbit Controls:** Smooth mouse/touch 3D rotation, pan, and zoom.
- **Dynamic Coordinate Sliders:** Real-time adjustments of $x \in [-2.5, 2.5]$, $y \in [-2.5, 2.5]$, and secant increment $h \in [0.02, 1.5]$.
- **Cross-Sectional Cutting Planes:** Interactive translucent vertical slicing planes ($y=\text{const}$ in cyan, $x=\text{const}$ in purple).
- **Secant-to-Tangent Limit Demonstration:** Watch the dashed secant line merge into the solid tangent line as $h \to 0$.
- **Tangent Plane Visualization:** Toggleable golden tangent plane hugging the surface.
- **Interactive Knowledge Check:** 5-question multiple choice quiz with instant feedback, explanations, and celebratory completion effects.

### 2. High-Definition 1080p Video Animation (`/deliverables/final_video.mp4`)
- **Strict 6-Scene Structure:**
  - *Scene 1 (0:00–0:30):* Hook & Multivariable Context
  - *Scene 2 (0:30–1:10):* Concept Introduction & Mapping
  - *Scene 3 (1:10–2:10):* Visual Intuition: 3D Cross-Sections
  - *Scene 4 (2:10–3:40):* Step-by-Step Analytical Derivation
  - *Scene 5 (3:40–4:30):* Geometric Synthesis & Tangent Plane
  - *Scene 6 (4:30–5:00):* Summary, Credits & AI Disclosure
- **Studio Narration:** Synchronized, crystal-clear voiceover across all six scenes.

---

## 📁 Repository Structure

```text
M3_Partial_Derivatives/
├── frontend/                     # Interactive 3D Web Application
│   ├── index.html                # Entry HTML shell
│   ├── package.json              # Dependencies (Three.js, KaTeX, Vite, Tailwind)
│   ├── vite.config.js            # Bundler configuration
│   ├── tailwind.config.js        # Design tokens & color system
│   ├── postcss.config.js         # PostCSS plugins
│   ├── dist/                     # Optimized production build assets
│   └── src/
│       ├── main.js               # Application orchestration & reactive state
│       ├── components/
│       │   ├── SurfaceVisualizer.js  # Modular Three.js 3D engine & shaders
│       │   └── Quiz.js               # 5-question knowledge check dataset
│       └── styles/
│           └── main.css          # Glassmorphism design system & typography
├── animation/                    # Video Generation Pipeline
│   ├── render_video.py           # 6-scene 1080p MP4 renderer & FFmpeg compositor
│   ├── generate_narration.py     # Speech synthesis audio generation
│   ├── generate_storyboard_pdf.py# Storyboard PDF generation engine
│   ├── assets/                   # Broadcast-quality WAV audio assets
│   └── scenes/                   # Rendered scene video files & frame caches
├── deliverables/                 # Ready-to-Submit Academic Deliverables
│   ├── final_video.mp4           # Master 1080p educational video
│   ├── storyboard.pdf            # 6-scene landscape storyboard document
│   └── narration_script.md       # Complete verbatim narration transcript
├── documentation/                # Rigorous Academic Documentation
│   ├── mathematical_verification.md # Formal step-by-step proofs & Hessian check
│   ├── viva_questions.md         # 16 in-depth viva examination Q&As
│   └── references.md             # Textbook citations & AI disclosure
└── README.md                     # Comprehensive project documentation
```

---

## 🛠️ Installation & Setup Instructions

### Prerequisites
- **Node.js** (v18+ recommended, tested on v24)
- **Python** (v3.9+)
- **FFmpeg** (for video and audio encoding)

### 1. Running the Interactive 3D Web Platform
```bash
cd M3_Partial_Derivatives/frontend
npm install
npm run dev
```
Open your browser at `http://localhost:3000` to interact with the 3D surface, sliders, and interactive quiz.

To preview the production build:
```bash
npx vite preview
```

### 2. Rendering the Mathematical Video Animation
```bash
# Generate the narration audio (if re-synthesizing)
python3 animation/generate_narration.py

# Render all 6 scenes and concatenate into final_video.mp4
python3 animation/render_video.py
```

### 3. Re-generating the Storyboard PDF
```bash
python3 animation/generate_storyboard_pdf.py
```

---

## 📚 Academic References

1. **Stewart, James** (2015). *Calculus: Early Transcendentals* (8th ed.). Cengage Learning. (Chapter 14: Partial Derivatives).
2. **Thomas, George B., Weir, Maurice D., & Hass, Joel** (2014). *Thomas' Calculus* (13th ed.). Pearson.
3. **Strang, Gilbert** (1991). *Calculus*. Wellesley-Cambridge Press (MIT OpenCourseWare).
4. **Sanderson, Grant (3Blue1Brown)**. *Essence of Calculus: Multivariable Visualizations*.

---

## 🤖 AI Disclosure

In accordance with academic policies, this project was developed with assistance from Google Antigravity AI engineering agent for WebGL Three.js visual structure, automated voice synthesis pipelines, and high-performance frame rendering. All mathematical proofs, derivatives, and geometric models were rigorously calculated and verified.
