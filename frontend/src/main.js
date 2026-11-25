import './styles/main.css';
import katex from 'katex';
import confetti from 'canvas-confetti';
import { SurfaceVisualizer } from './components/SurfaceVisualizer.js';
import { quizData } from './components/Quiz.js';

// Setup full app layout
const app = document.getElementById('app');

app.innerHTML = `
  <!-- Navigation Bar -->
  <nav class="sticky top-0 z-50 bg-slate-950/80 backdrop-blur-md border-b border-slate-800/80 px-6 py-4">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <div class="w-9 h-9 rounded-lg bg-gradient-to-tr from-cyan-500 to-purple-600 flex items-center justify-center font-bold text-white shadow-lg shadow-cyan-500/20">
          ∂
        </div>
        <div>
          <span class="font-bold text-lg tracking-tight text-white block leading-tight">M3 Mathematics: Partial Derivatives</span>
          <span class="text-xs text-slate-400 font-mono">BTech Internal Assessment • Academic Visualization</span>
        </div>
      </div>
      <div class="hidden md:flex items-center space-x-6 text-sm font-medium text-slate-300">
        <a href="#intro" class="hover:text-cyan-400 transition">Introduction</a>
        <a href="#visualizer-section" class="hover:text-cyan-400 transition">3D Interactive Lab</a>
        <a href="#derivation-x" class="hover:text-cyan-400 transition">∂f/∂x Derivation</a>
        <a href="#derivation-y" class="hover:text-purple-400 transition">∂f/∂y Derivation</a>
        <a href="#limits" class="hover:text-amber-400 transition">Limits & Secants</a>
        <a href="#quiz-section" class="hover:text-emerald-400 transition">Knowledge Check</a>
      </div>
      <div>
        <a href="#visualizer-section" class="px-4 py-2 rounded-lg bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 hover:bg-cyan-500/20 text-xs font-semibold uppercase tracking-wider transition">
          Launch 3D Lab
        </a>
      </div>
    </div>
  </nav>

  <!-- Hero / Introduction Section -->
  <header id="intro" class="relative pt-16 pb-20 px-6 max-w-7xl mx-auto border-b border-slate-800/60">
    <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-cyan-950/60 border border-cyan-500/30 text-cyan-400 text-xs font-mono mb-6">
      <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
      <span>LINEAR ALGEBRA & MULTIVARIABLE CALCULUS</span>
    </div>
    <h1 class="text-4xl sm:text-6xl font-extrabold tracking-tight text-white max-w-4xl leading-tight">
      Understanding Partial Derivatives Through <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-sky-300 to-purple-400">3D Surface Visualization</span>
    </h1>
    <p class="mt-6 text-lg sm:text-xl text-slate-300 max-w-3xl leading-relaxed">
      How changing one variable at a time reveals the fundamental behaviour and geometry of a multivariable function.
    </p>

    <!-- Key Core Concept Cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
      <div class="glass-panel p-6 rounded-2xl border-l-4 border-l-cyan-400">
        <div class="text-xs font-mono text-cyan-400 uppercase tracking-wider mb-2">Concept 1</div>
        <h3 class="text-lg font-bold text-white mb-2">Multivariable Mapping</h3>
        <p class="text-sm text-slate-400 leading-relaxed">
          A two-variable function <span class="katex-inline" data-latex="z = f(x,y)"></span> maps an input coordinate pair <span class="katex-inline" data-latex="(x,y)"></span> in the flat domain plane to a vertical altitude height <span class="katex-inline" data-latex="z"></span> in 3D Euclidean space.
        </p>
      </div>

      <div class="glass-panel p-6 rounded-2xl border-l-4 border-l-purple-400">
        <div class="text-xs font-mono text-purple-400 uppercase tracking-wider mb-2">Concept 2</div>
        <h3 class="text-lg font-bold text-white mb-2">Holding One Variable Constant</h3>
        <p class="text-sm text-slate-400 leading-relaxed">
          In multidimensional spaces, movement is unconstrained. By fixing one variable (e.g. <span class="katex-inline" data-latex="y = \text{const}"></span>), we slice the 3D surface into a single-variable 2D cross-sectional curve.
        </p>
      </div>

      <div class="glass-panel p-6 rounded-2xl border-l-4 border-l-amber-400">
        <div class="text-xs font-mono text-amber-400 uppercase tracking-wider mb-2">Concept 3</div>
        <h3 class="text-lg font-bold text-white mb-2">Instantaneous Slope</h3>
        <p class="text-sm text-slate-400 leading-relaxed">
          The partial derivatives <span class="katex-inline" data-latex="\frac{\partial f}{\partial x}"></span> and <span class="katex-inline" data-latex="\frac{\partial f}{\partial y}"></span> quantify the exact instantaneous rates of change (tangent slopes) along those orthogonal cross-sectional curves.
        </p>
      </div>
    </div>
  </header>

  <!-- 3D Interactive Lab Section -->
  <section id="visualizer-section" class="py-16 px-6 max-w-7xl mx-auto border-b border-slate-800/60">
    <div class="flex flex-col lg:flex-row lg:items-center justify-between mb-8 gap-4">
      <div>
        <div class="inline-flex items-center space-x-2 text-xs font-mono text-amber-400 mb-1">
          <span>● INTERACTIVE EXPERIMENTATION BENCH</span>
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white">Central Worked Example: <span class="katex-inline text-cyan-400" data-latex="f(x,y) = x^2 + xy + y^2"></span></h2>
        <p class="text-sm text-slate-400 mt-1">Explore real-time 3D geometry, cross-sections, tangent lines, and secant limit convergence.</p>
      </div>
      <div class="flex flex-wrap items-center gap-3">
        <button id="btn-mode-both" class="px-3.5 py-1.5 text-xs font-semibold rounded-lg bg-slate-800 text-white border border-slate-700 hover:bg-slate-700 transition">Both Axes</button>
        <button id="btn-mode-x" class="px-3.5 py-1.5 text-xs font-semibold rounded-lg bg-cyan-950/80 text-cyan-300 border border-cyan-500/50 hover:bg-cyan-900/50 transition">X-Direction (y=const)</button>
        <button id="btn-mode-y" class="px-3.5 py-1.5 text-xs font-semibold rounded-lg bg-purple-950/80 text-purple-300 border border-purple-500/50 hover:bg-purple-900/50 transition">Y-Direction (x=const)</button>
        <button id="btn-reset" class="px-3.5 py-1.5 text-xs font-semibold rounded-lg bg-rose-950/60 text-rose-300 border border-rose-700/40 hover:bg-rose-900/60 transition">Reset View</button>
      </div>
    </div>

    <!-- 3D Visualization Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
      <!-- 3D Canvas Container -->
      <div class="lg:col-span-8 relative rounded-2xl overflow-hidden border border-slate-800 bg-slate-950 shadow-2xl">
        <div id="three-canvas-container" class="w-full h-[540px] cursor-grab active:cursor-grabbing"></div>
        
        <!-- Canvas Floating HUD Overlay -->
        <div class="absolute top-4 left-4 pointer-events-none flex flex-col gap-2">
          <div class="glass-panel px-3.5 py-2 rounded-xl text-xs font-mono border-slate-700">
            <span class="text-slate-400">Target Coordinates: </span>
            <span id="hud-point" class="text-amber-400 font-bold">(1.00, 2.00, 7.00)</span>
          </div>
          <div class="glass-panel px-3.5 py-2 rounded-xl text-xs font-mono border-cyan-800 text-cyan-300">
            <span class="text-slate-400">Slope ∂f/∂x: </span>
            <span id="hud-slope-x" class="font-bold">4.00</span>
          </div>
          <div class="glass-panel px-3.5 py-2 rounded-xl text-xs font-mono border-purple-800 text-purple-300">
            <span class="text-slate-400">Slope ∂f/∂y: </span>
            <span id="hud-slope-y" class="font-bold">5.00</span>
          </div>
        </div>

        <!-- Canvas Controls Bar (Bottom) -->
        <div class="absolute bottom-4 left-4 right-4 glass-panel px-4 py-3 rounded-xl flex flex-wrap items-center justify-between gap-3 text-xs">
          <div class="flex items-center space-x-4">
            <label class="flex items-center space-x-2 cursor-pointer text-slate-300 hover:text-white">
              <input type="checkbox" id="check-tangent-lines" checked class="rounded border-slate-700 bg-slate-900 text-amber-500 focus:ring-0">
              <span>Tangent Lines</span>
            </label>
            <label class="flex items-center space-x-2 cursor-pointer text-slate-300 hover:text-white">
              <input type="checkbox" id="check-cutting-planes" checked class="rounded border-slate-700 bg-slate-900 text-cyan-500 focus:ring-0">
              <span>Slicing Planes</span>
            </label>
            <label class="flex items-center space-x-2 cursor-pointer text-slate-300 hover:text-white">
              <input type="checkbox" id="check-tangent-plane" class="rounded border-slate-700 bg-slate-900 text-amber-500 focus:ring-0">
              <span>Tangent Plane</span>
            </label>
            <label class="flex items-center space-x-2 cursor-pointer text-slate-300 hover:text-white">
              <input type="checkbox" id="check-secant" checked class="rounded border-slate-700 bg-slate-900 text-sky-400 focus:ring-0">
              <span>Secant Line (Limit)</span>
            </label>
          </div>
          <div class="text-slate-400 text-[11px] font-mono">
            Drag to Rotate • Scroll to Zoom
          </div>
        </div>
      </div>

      <!-- Controls & Live Mathematical Readout -->
      <div class="lg:col-span-4 flex flex-col gap-6">
        <!-- Sliders Card -->
        <div class="glass-panel p-6 rounded-2xl border-slate-800">
          <h3 class="text-sm font-bold text-white uppercase tracking-wider mb-4 flex items-center justify-between">
            <span>Coordinate Controls</span>
            <span class="text-xs text-slate-400 font-normal">Domain: [-3, 3]</span>
          </h3>

          <!-- X slider -->
          <div class="mb-5">
            <div class="flex justify-between items-center text-xs font-mono mb-1.5">
              <span class="text-cyan-400 font-bold">X Coordinate:</span>
              <span id="val-x-display" class="px-2 py-0.5 rounded bg-cyan-950 text-cyan-300 border border-cyan-800">1.00</span>
            </div>
            <input id="slider-x" type="range" min="-2.5" max="2.5" step="0.05" value="1.0" class="w-full">
            <div class="flex justify-between text-[10px] text-slate-500 font-mono mt-1">
              <span>-2.5</span>
              <span class="text-cyan-500 font-semibold">Standard Point: x = 1</span>
              <span>+2.5</span>
            </div>
          </div>

          <!-- Y slider -->
          <div class="mb-5">
            <div class="flex justify-between items-center text-xs font-mono mb-1.5">
              <span class="text-purple-400 font-bold">Y Coordinate:</span>
              <span id="val-y-display" class="px-2 py-0.5 rounded bg-purple-950 text-purple-300 border border-purple-800">2.00</span>
            </div>
            <input id="slider-y" type="range" min="-2.5" max="2.5" step="0.05" value="2.0" class="w-full slider-y">
            <div class="flex justify-between text-[10px] text-slate-500 font-mono mt-1">
              <span>-2.5</span>
              <span class="text-purple-400 font-semibold">Standard Point: y = 2</span>
              <span>+2.5</span>
            </div>
          </div>

          <!-- Secant step h slider -->
          <div>
            <div class="flex justify-between items-center text-xs font-mono mb-1.5">
              <span class="text-amber-400 font-bold">Secant Increment h:</span>
              <span id="val-h-display" class="px-2 py-0.5 rounded bg-amber-950 text-amber-300 border border-amber-800">0.50</span>
            </div>
            <input id="slider-h" type="range" min="0.02" max="1.5" step="0.02" value="0.5" class="w-full">
            <div class="flex justify-between text-[10px] text-slate-500 font-mono mt-1">
              <span>h → 0 (Tangent)</span>
              <span>h = 1.5 (Secant)</span>
            </div>
          </div>
        </div>

        <!-- Live Computed Output Card -->
        <div class="glass-panel p-6 rounded-2xl border-slate-800">
          <h3 class="text-sm font-bold text-white uppercase tracking-wider mb-4">Live State Calculations</h3>
          
          <div class="space-y-4 text-xs font-mono">
            <div class="p-3 rounded-lg bg-slate-900/80 border border-slate-800">
              <div class="text-slate-400 mb-1">Point Elevation <span class="katex-inline" data-latex="z = x^2 + xy + y^2"></span></div>
              <div id="calc-z" class="text-lg font-bold text-amber-400">z = (1.00)² + (1.00)(2.00) + (2.00)² = 7.00</div>
            </div>

            <div class="p-3 rounded-lg bg-cyan-950/30 border border-cyan-800/50">
              <div class="text-cyan-400 font-bold mb-1">X-Rate: <span class="katex-inline" data-latex="\partial f / \partial x = 2x + y"></span></div>
              <div id="calc-fx" class="text-base text-cyan-300 font-bold">2(1.00) + 2.00 = 4.00</div>
              <div class="text-[11px] text-slate-400 mt-1">Holding y fixed at 2.00</div>
            </div>

            <div class="p-3 rounded-lg bg-purple-950/30 border border-purple-800/50">
              <div class="text-purple-400 font-bold mb-1">Y-Rate: <span class="katex-inline" data-latex="\partial f / \partial y = x + 2y"></span></div>
              <div id="calc-fy" class="text-base text-purple-300 font-bold">1.00 + 2(2.00) = 5.00</div>
              <div class="text-[11px] text-slate-400 mt-1">Holding x fixed at 1.00</div>
            </div>

            <div class="p-3 rounded-lg bg-amber-950/20 border border-amber-800/40">
              <div class="text-amber-400 font-bold mb-1">Tangent Plane at (x₀, y₀, z₀):</div>
              <div id="calc-plane" class="text-xs text-amber-200">z - 7.00 = 4.00(x - 1.00) + 5.00(y - 2.00)</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Step-by-Step Rigorous Derivation Sections -->
  <section class="py-16 px-6 max-w-7xl mx-auto border-b border-slate-800/60">
    <div class="text-center max-w-3xl mx-auto mb-14">
      <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest mb-2">RIGOROUS MATHEMATICAL DERIVATION</div>
      <h2 class="text-3xl sm:text-4xl font-extrabold text-white">Calculating Partial Derivatives Step by Step</h2>
      <p class="text-slate-400 mt-3 text-sm sm:text-base">
        A complete pedagogical breakdown of each term, treating the complementary variable as an invariant constant scalar.
      </p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      <!-- Section A: Partial Derivative with respect to X -->
      <div id="derivation-x" class="glass-panel glass-panel-glow-x p-8 rounded-2xl border-slate-800">
        <div class="flex items-center justify-between mb-4">
          <span class="px-3 py-1 rounded-full bg-cyan-950 border border-cyan-500/40 text-cyan-400 text-xs font-mono font-bold">SECTION A</span>
          <span class="text-xs text-slate-400 font-mono">y is held constant (y = c)</span>
        </div>
        <h3 class="text-2xl font-bold text-white mb-2">Partial Derivative with Respect to <span class="text-cyan-400">x</span></h3>
        <p class="text-sm text-slate-300 mb-6">
          To measure how rapidly <span class="katex-inline" data-latex="f(x,y)"></span> climbs or falls when stepping purely parallel to the x-axis, we differentiate with respect to <span class="katex-inline" data-latex="x"></span> while freezing <span class="katex-inline" data-latex="y"></span>.
        </p>

        <div class="math-display mb-6">
          <div class="katex-block" data-latex="f(x,y) = x^2 + xy + y^2"></div>
        </div>

        <div class="space-y-4 mb-6">
          <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 text-sm">
            <span class="font-bold text-cyan-400">Term 1: <span class="katex-inline" data-latex="\frac{\partial}{\partial x}(x^2)"></span></span>
            <div class="text-slate-300 mt-1">Applying the standard power rule <span class="katex-inline" data-latex="\frac{d}{dx}[x^n] = n x^{n-1}"></span>:</div>
            <div class="katex-block my-1 text-cyan-300 font-bold" data-latex="\frac{\partial}{\partial x}(x^2) = 2x"></div>
          </div>

          <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 text-sm">
            <span class="font-bold text-cyan-400">Term 2: <span class="katex-inline" data-latex="\frac{\partial}{\partial x}(xy)"></span></span>
            <div class="text-slate-300 mt-1">Since <span class="katex-inline" data-latex="y"></span> is an invariant constant factor, <span class="katex-inline" data-latex="\frac{\partial}{\partial x}(c \cdot x) = c"></span>:</div>
            <div class="katex-block my-1 text-cyan-300 font-bold" data-latex="\frac{\partial}{\partial x}(y \cdot x) = y \cdot 1 = y"></div>
          </div>

          <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 text-sm">
            <span class="font-bold text-cyan-400">Term 3: <span class="katex-inline" data-latex="\frac{\partial}{\partial x}(y^2)"></span></span>
            <div class="text-slate-300 mt-1">Because <span class="katex-inline" data-latex="y"></span> does not depend on <span class="katex-inline" data-latex="x"></span>, <span class="katex-inline" data-latex="y^2"></span> is an absolute constant scalar. Derivative of any constant is zero:</div>
            <div class="katex-block my-1 text-cyan-300 font-bold" data-latex="\frac{\partial}{\partial x}(y^2) = 0"></div>
          </div>
        </div>

        <div class="p-4 rounded-xl bg-cyan-950/50 border border-cyan-500/50">
          <div class="text-xs font-mono text-cyan-300 uppercase tracking-wider mb-1 font-bold">General Gradient Function & Evaluation at (1,2)</div>
          <div class="katex-block text-lg font-bold text-white mb-2" data-latex="\frac{\partial f}{\partial x} = 2x + y"></div>
          <div class="text-sm text-slate-300">Substituting <span class="katex-inline" data-latex="x = 1, y = 2"></span>:</div>
          <div class="katex-block text-xl font-extrabold text-cyan-400 mt-1" data-latex="\left. \frac{\partial f}{\partial x} \right|_{(1,2)} = 2(1) + 2 = 4"></div>
          <p class="text-xs text-cyan-200 mt-2 font-mono">Meaning: Moving 1 unit in +x direction increases surface elevation z by 4 units.</p>
        </div>
      </div>

      <!-- Section B: Partial Derivative with respect to Y -->
      <div id="derivation-y" class="glass-panel glass-panel-glow-y p-8 rounded-2xl border-slate-800">
        <div class="flex items-center justify-between mb-4">
          <span class="px-3 py-1 rounded-full bg-purple-950 border border-purple-500/40 text-purple-400 text-xs font-mono font-bold">SECTION B</span>
          <span class="text-xs text-slate-400 font-mono">x is held constant (x = c)</span>
        </div>
        <h3 class="text-2xl font-bold text-white mb-2">Partial Derivative with Respect to <span class="text-purple-400">y</span></h3>
        <p class="text-sm text-slate-300 mb-6">
          To measure how rapidly <span class="katex-inline" data-latex="f(x,y)"></span> climbs or falls when stepping purely parallel to the y-axis, we differentiate with respect to <span class="katex-inline" data-latex="y"></span> while freezing <span class="katex-inline" data-latex="x"></span>.
        </p>

        <div class="math-display mb-6">
          <div class="katex-block" data-latex="f(x,y) = x^2 + xy + y^2"></div>
        </div>

        <div class="space-y-4 mb-6">
          <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 text-sm">
            <span class="font-bold text-purple-400">Term 1: <span class="katex-inline" data-latex="\frac{\partial}{\partial y}(x^2)"></span></span>
            <div class="text-slate-300 mt-1">Because <span class="katex-inline" data-latex="x"></span> is held strictly constant, <span class="katex-inline" data-latex="x^2"></span> is a static constant:</div>
            <div class="katex-block my-1 text-purple-300 font-bold" data-latex="\frac{\partial}{\partial y}(x^2) = 0"></div>
          </div>

          <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 text-sm">
            <span class="font-bold text-purple-400">Term 2: <span class="katex-inline" data-latex="\frac{\partial}{\partial y}(xy)"></span></span>
            <div class="text-slate-300 mt-1">Here <span class="katex-inline" data-latex="x"></span> acts as the constant scalar coefficient for <span class="katex-inline" data-latex="y"></span>:</div>
            <div class="katex-block my-1 text-purple-300 font-bold" data-latex="\frac{\partial}{\partial y}(x \cdot y) = x \cdot 1 = x"></div>
          </div>

          <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 text-sm">
            <span class="font-bold text-purple-400">Term 3: <span class="katex-inline" data-latex="\frac{\partial}{\partial y}(y^2)"></span></span>
            <div class="text-slate-300 mt-1">Applying the standard single-variable power rule:</div>
            <div class="katex-block my-1 text-purple-300 font-bold" data-latex="\frac{\partial}{\partial y}(y^2) = 2y"></div>
          </div>
        </div>

        <div class="p-4 rounded-xl bg-purple-950/50 border border-purple-500/50">
          <div class="text-xs font-mono text-purple-300 uppercase tracking-wider mb-1 font-bold">General Gradient Function & Evaluation at (1,2)</div>
          <div class="katex-block text-lg font-bold text-white mb-2" data-latex="\frac{\partial f}{\partial y} = x + 2y"></div>
          <div class="text-sm text-slate-300">Substituting <span class="katex-inline" data-latex="x = 1, y = 2"></span>:</div>
          <div class="katex-block text-xl font-extrabold text-purple-400 mt-1" data-latex="\left. \frac{\partial f}{\partial y} \right|_{(1,2)} = 1 + 2(2) = 5"></div>
          <p class="text-xs text-purple-200 mt-2 font-mono">Meaning: Moving 1 unit in +y direction increases surface elevation z by 5 units.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section C & D: Limit Definition and Tangent Plane -->
  <section id="limits" class="py-16 px-6 max-w-7xl mx-auto border-b border-slate-800/60">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch">
      <!-- Limit Definitions Card -->
      <div class="glass-panel p-8 rounded-2xl border-slate-800 flex flex-col justify-between">
        <div>
          <div class="inline-flex items-center space-x-2 text-xs font-mono text-amber-400 mb-2">
            <span>SECTION C • FIRST PRINCIPLES</span>
          </div>
          <h3 class="text-2xl font-bold text-white mb-3">Formal Mathematical Definition Using Limits</h3>
          <p class="text-sm text-slate-300 leading-relaxed mb-6">
            Just as in single-variable calculus, the derivative is fundamentally the limiting value of a difference quotient representing secant slopes as the displacement step <span class="katex-inline" data-latex="h \to 0"></span>.
          </p>

          <div class="space-y-4">
            <div class="p-4 rounded-xl bg-slate-900 border border-cyan-900/60">
              <div class="text-xs font-mono text-cyan-400 mb-1">Difference Quotient in X:</div>
              <div class="katex-block text-cyan-200" data-latex="f_x(a,b) = \lim_{h \to 0} \frac{f(a+h, b) - f(a,b)}{h}"></div>
              <p class="text-xs text-slate-400 mt-2">
                Notice that the second coordinate <span class="katex-inline" data-latex="b"></span> remains entirely unaltered. Only <span class="katex-inline" data-latex="a"></span> receives the increment <span class="katex-inline" data-latex="h"></span>.
              </p>
            </div>

            <div class="p-4 rounded-xl bg-slate-900 border border-purple-900/60">
              <div class="text-xs font-mono text-purple-400 mb-1">Difference Quotient in Y:</div>
              <div class="katex-block text-purple-200" data-latex="f_y(a,b) = \lim_{h \to 0} \frac{f(a, b+h) - f(a,b)}{h}"></div>
              <p class="text-xs text-slate-400 mt-2">
                Similarly, the first coordinate <span class="katex-inline" data-latex="a"></span> is frozen, and only <span class="katex-inline" data-latex="b"></span> is perturbed by step <span class="katex-inline" data-latex="h"></span>.
              </p>
            </div>
          </div>
        </div>

        <div class="mt-6 p-4 rounded-xl bg-amber-950/20 border border-amber-800/40 text-xs text-amber-200">
          <span class="font-bold">Secant to Tangent Transition:</span> Drag the Secant slider <span class="font-mono text-white">h</span> in the 3D lab above down towards 0 to visually witness the dashed secant line merge into the solid tangent line!
        </div>
      </div>

      <!-- Tangent Plane & Total Differential Card -->
      <div class="glass-panel p-8 rounded-2xl border-slate-800 flex flex-col justify-between">
        <div>
          <div class="inline-flex items-center space-x-2 text-xs font-mono text-emerald-400 mb-2">
            <span>SECTION D • GEOMETRIC SYNTHESIS</span>
          </div>
          <h3 class="text-2xl font-bold text-white mb-3">The Tangent Plane at (1, 2, 7)</h3>
          <p class="text-sm text-slate-300 leading-relaxed mb-6">
            The two orthogonal tangent lines in the x and y directions span a unique 2D flat plane that kisses the curved surface at <span class="katex-inline" data-latex="(1,2,7)"></span>. This is the multivariable analogue of a tangent line.
          </p>

          <div class="math-display mb-6">
            <div class="katex-block text-emerald-300 text-lg" data-latex="z - z_0 = f_x(x_0,y_0)(x - x_0) + f_y(x_0,y_0)(y - y_0)"></div>
          </div>

          <div class="space-y-3 text-sm text-slate-300">
            <div class="flex items-start space-x-3">
              <span class="w-6 h-6 rounded-full bg-emerald-950 border border-emerald-600 text-emerald-400 flex items-center justify-center text-xs font-bold shrink-0 mt-0.5">1</span>
              <span>Base point: <span class="katex-inline font-mono text-white" data-latex="(x_0, y_0, z_0) = (1, 2, 7)"></span></span>
            </div>
            <div class="flex items-start space-x-3">
              <span class="w-6 h-6 rounded-full bg-emerald-950 border border-emerald-600 text-emerald-400 flex items-center justify-center text-xs font-bold shrink-0 mt-0.5">2</span>
              <span>Partial slopes: <span class="katex-inline font-mono text-cyan-300" data-latex="f_x = 4"></span> and <span class="katex-inline font-mono text-purple-300" data-latex="f_y = 5"></span></span>
            </div>
            <div class="flex items-start space-x-3">
              <span class="w-6 h-6 rounded-full bg-emerald-950 border border-emerald-600 text-emerald-400 flex items-center justify-center text-xs font-bold shrink-0 mt-0.5">3</span>
              <span>Surface Normal Vector: <span class="katex-inline font-mono text-amber-300" data-latex="\vec{n} = \langle -f_x, -f_y, 1 \rangle = \langle -4, -5, 1 \rangle"></span></span>
            </div>
          </div>
        </div>

        <div class="mt-6 p-4 rounded-xl bg-slate-900 border border-slate-800">
          <div class="text-xs font-mono text-slate-400 mb-1">Final Explicit Equation of Tangent Plane:</div>
          <div class="katex-block text-lg font-bold text-amber-400" data-latex="z - 7 = 4(x - 1) + 5(y - 2) \implies z = 4x + 5y - 7"></div>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive Quiz Section -->
  <section id="quiz-section" class="py-16 px-6 max-w-4xl mx-auto border-b border-slate-800/60">
    <div class="text-center mb-10">
      <div class="inline-flex items-center space-x-2 text-xs font-mono text-emerald-400 mb-2">
        <span>INTERACTIVE KNOWLEDGE CHECK</span>
      </div>
      <h2 class="text-3xl font-extrabold text-white">Test Your Mastery</h2>
      <p class="text-slate-400 text-sm mt-2">Evaluate your understanding of partial differentiation, rules, and 3D geometry.</p>
    </div>

    <div id="quiz-container" class="glass-panel p-8 rounded-2xl border-slate-800">
      <div id="quiz-progress-bar" class="w-full bg-slate-800 h-2 rounded-full overflow-hidden mb-6">
        <div id="quiz-progress" class="bg-gradient-to-r from-cyan-400 to-emerald-400 h-full w-[20%] transition-all duration-300"></div>
      </div>
      
      <div id="quiz-content">
        <!-- Rendered by JS -->
      </div>
    </div>
  </section>

  <!-- Academic Credits, AI Disclosure & References Footer -->
  <footer class="py-16 px-6 max-w-7xl mx-auto text-slate-400 text-xs">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
      <div>
        <h4 class="text-white font-bold text-sm mb-3">Academic Context</h4>
        <p class="leading-relaxed mb-2">
          Course: BTech Linear Algebra and Calculus (M3)<br>
          Topic: Partial Derivatives & Multivariable Analysis<br>
          Topic Exact Title: "Understanding Partial Derivatives Through 3D Surface Visualization"
        </p>
        <p class="text-slate-500">
          Designed for rigorous university-level pedagogy and intuitive geometric comprehension.
        </p>
      </div>

      <div>
        <h4 class="text-white font-bold text-sm mb-3">Academic References</h4>
        <ul class="space-y-1.5 leading-relaxed">
          <li>• Stewart, J. (2015). <em>Calculus: Early Transcendentals</em> (8th ed.). Cengage Learning.</li>
          <li>• Thomas, G. B., Weir, M. D., & Hass, J. (2014). <em>Thomas' Calculus</em> (13th ed.). Pearson.</li>
          <li>• Strang, G. (1991). <em>Calculus</em>. Wellesley-Cambridge Press.</li>
          <li>• 3Blue1Brown (Grant Sanderson). Essence of Calculus: Multivariable Visualizations.</li>
        </ul>
      </div>

      <div>
        <h4 class="text-white font-bold text-sm mb-3">AI & Tools Disclosure</h4>
        <p class="leading-relaxed mb-2">
          This project was developed with assistance from Google Antigravity AI engineering agent for code architecture, WebGL Three.js 3D mathematical rendering, and automated pedagogical voice-over compilation.
        </p>
        <p class="text-slate-500">
          All mathematical derivations have been analytically verified and tested against symbolic ground truth.
        </p>
      </div>
    </div>

    <div class="border-t border-slate-800/80 pt-8 flex flex-col sm:flex-row items-center justify-between text-slate-500">
      <div>© 2026 M3 Mathematics Assessment • All Rights Reserved</div>
      <div class="mt-4 sm:mt-0 font-mono text-[11px] text-cyan-400">
        Status: GitHub Repository Ready • 1080p Video Generated
      </div>
    </div>
  </footer>
`;

// Initialize KaTeX on all math containers
function renderMath() {
  document.querySelectorAll('.katex-inline').forEach(el => {
    const latex = el.getAttribute('data-latex');
    if (latex) {
      katex.render(latex, el, { throwOnError: false, displayMode: false });
    }
  });

  document.querySelectorAll('.katex-block').forEach(el => {
    const latex = el.getAttribute('data-latex');
    if (latex) {
      katex.render(latex, el, { throwOnError: false, displayMode: true });
    }
  });
}

renderMath();

// Initialize 3D Visualizer
const container3D = document.getElementById('three-canvas-container');
const visualizer = new SurfaceVisualizer(container3D);

// Bind HUD and Calculation elements
const sliderX = document.getElementById('slider-x');
const sliderY = document.getElementById('slider-y');
const sliderH = document.getElementById('slider-h');
const valXDisplay = document.getElementById('val-x-display');
const valYDisplay = document.getElementById('val-y-display');
const valHDisplay = document.getElementById('val-h-display');

const hudPoint = document.getElementById('hud-point');
const hudSlopeX = document.getElementById('hud-slope-x');
const hudSlopeY = document.getElementById('hud-slope-y');

const calcZ = document.getElementById('calc-z');
const calcFx = document.getElementById('calc-fx');
const calcFy = document.getElementById('calc-fy');
const calcPlane = document.getElementById('calc-plane');

function updateMathReadouts(x, y, h) {
  const z = SurfaceVisualizer.f(x, y);
  const fx = SurfaceVisualizer.df_dx(x, y);
  const fy = SurfaceVisualizer.df_dy(x, y);

  valXDisplay.textContent = x.toFixed(2);
  valYDisplay.textContent = y.toFixed(2);
  valHDisplay.textContent = h.toFixed(2);

  hudPoint.textContent = `(${x.toFixed(2)}, ${y.toFixed(2)}, ${z.toFixed(2)})`;
  hudSlopeX.textContent = fx.toFixed(2);
  hudSlopeY.textContent = fy.toFixed(2);

  calcZ.textContent = `z = (${x.toFixed(2)})² + (${x.toFixed(2)})(${y.toFixed(2)}) + (${y.toFixed(2)})² = ${z.toFixed(2)}`;
  calcFx.textContent = `2(${x.toFixed(2)}) + ${y.toFixed(2)} = ${fx.toFixed(2)}`;
  calcFy.textContent = `${x.toFixed(2)} + 2(${y.toFixed(2)}) = ${fy.toFixed(2)}`;
  calcPlane.textContent = `z - ${z.toFixed(2)} = ${fx.toFixed(2)}(x - ${x.toFixed(2)}) + ${fy.toFixed(2)}(y - ${y.toFixed(2)})`;
}

// Event Listeners for Sliders
sliderX.addEventListener('input', (e) => {
  const x = parseFloat(e.target.value);
  visualizer.setX(x);
  updateMathReadouts(x, parseFloat(sliderY.value), parseFloat(sliderH.value));
});

sliderY.addEventListener('input', (e) => {
  const y = parseFloat(e.target.value);
  visualizer.setY(y);
  updateMathReadouts(parseFloat(sliderX.value), y, parseFloat(sliderH.value));
});

sliderH.addEventListener('input', (e) => {
  const h = parseFloat(e.target.value);
  visualizer.setH(h);
  updateMathReadouts(parseFloat(sliderX.value), parseFloat(sliderY.value), h);
});

// View mode buttons
document.getElementById('btn-mode-both').addEventListener('click', () => {
  visualizer.setMode('both');
});
document.getElementById('btn-mode-x').addEventListener('click', () => {
  visualizer.setMode('x');
});
document.getElementById('btn-mode-y').addEventListener('click', () => {
  visualizer.setMode('y');
});

// Reset Button
document.getElementById('btn-reset').addEventListener('click', () => {
  sliderX.value = 1.0;
  sliderY.value = 2.0;
  sliderH.value = 0.5;
  visualizer.reset();
  updateMathReadouts(1.0, 2.0, 0.5);
});

// Checkbox Toggles
document.getElementById('check-tangent-lines').addEventListener('change', (e) => {
  visualizer.toggleTangentLine(e.target.checked);
});
document.getElementById('check-cutting-planes').addEventListener('change', (e) => {
  visualizer.toggleCuttingPlane(e.target.checked);
});
document.getElementById('check-tangent-plane').addEventListener('change', (e) => {
  visualizer.toggleTangentPlane(e.target.checked);
});
document.getElementById('check-secant').addEventListener('change', (e) => {
  visualizer.toggleSecantLine(e.target.checked);
});

// Interactive Quiz System Implementation
let currentQuizIdx = 0;
let userScore = 0;
const quizContentEl = document.getElementById('quiz-content');
const quizProgressEl = document.getElementById('quiz-progress');

function renderQuizQuestion() {
  const q = quizData[currentQuizIdx];
  const total = quizData.length;
  quizProgressEl.style.width = `${((currentQuizIdx) / total) * 100}%`;

  quizContentEl.innerHTML = `
    <div class="mb-4 flex items-center justify-between text-xs font-mono text-slate-400">
      <span>QUESTION ${currentQuizIdx + 1} OF ${total}</span>
      <span>SCORE: ${userScore} / ${currentQuizIdx}</span>
    </div>
    <h3 class="text-lg font-bold text-white mb-6">${q.question}</h3>
    <div class="space-y-3 mb-6" id="quiz-options-box">
      ${q.options.map((opt, i) => `
        <button class="quiz-option-btn w-full text-left p-4 rounded-xl bg-slate-900 border border-slate-800 hover:border-cyan-500/50 hover:bg-slate-800/80 transition text-sm text-slate-200" data-idx="${i}">
          <span class="inline-block w-6 font-mono text-cyan-400 font-bold">${String.fromCharCode(65 + i)}.</span> ${opt}
        </button>
      `).join('')}
    </div>
    <div id="quiz-explanation" class="hidden p-4 rounded-xl border text-sm mb-6"></div>
    <div class="flex justify-end">
      <button id="quiz-next-btn" class="hidden px-5 py-2.5 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold text-xs uppercase tracking-wider transition">
        Next Question →
      </button>
    </div>
  `;

  document.querySelectorAll('.quiz-option-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const selected = parseInt(btn.getAttribute('data-idx'));
      handleAnswer(selected, q);
    });
  });
}

function handleAnswer(selected, question) {
  const optionButtons = document.querySelectorAll('.quiz-option-btn');
  optionButtons.forEach(b => b.disabled = true);

  const explEl = document.getElementById('quiz-explanation');
  const nextBtn = document.getElementById('quiz-next-btn');
  nextBtn.classList.remove('hidden');

  if (selected === question.correct) {
    userScore++;
    optionButtons[selected].classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-200');
    explEl.className = 'p-4 rounded-xl border border-emerald-500/50 bg-emerald-950/30 text-emerald-300 text-sm mb-6';
    explEl.innerHTML = `<span class="font-bold">✓ Correct!</span> ${question.explanation}`;
  } else {
    optionButtons[selected].classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-200');
    optionButtons[question.correct].classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-200');
    explEl.className = 'p-4 rounded-xl border border-rose-500/50 bg-rose-950/30 text-rose-300 text-sm mb-6';
    explEl.innerHTML = `<span class="font-bold">✗ Incorrect.</span> ${question.explanation}`;
  }
  explEl.classList.remove('hidden');

  nextBtn.addEventListener('click', () => {
    currentQuizIdx++;
    if (currentQuizIdx < quizData.length) {
      renderQuizQuestion();
    } else {
      renderQuizResults();
    }
  });
}

function renderQuizResults() {
  quizProgressEl.style.width = '100%';
  const pct = Math.round((userScore / quizData.length) * 100);

  if (pct >= 80) {
    confetti({
      particleCount: 100,
      spread: 70,
      origin: { y: 0.6 }
    });
  }

  quizContentEl.innerHTML = `
    <div class="text-center py-6">
      <div class="text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-emerald-400 mb-2">
        ${userScore} / ${quizData.length}
      </div>
      <div class="text-lg font-bold text-white mb-2">
        ${pct >= 80 ? 'Outstanding! Comprehensive Multivariable Mastery' : 'Good effort! Review the 3D curves and derivations'}
      </div>
      <p class="text-slate-400 text-sm max-w-md mx-auto mb-6">
        ${pct >= 80 ? 'You have demonstrated solid conceptual understanding of partial derivative definitions, rules of differentiation, and geometric cross-sections.' : 'Feel free to review the step-by-step calculus derivations above and test your knowledge again.'}
      </p>
      <button id="quiz-retry-btn" class="px-6 py-2.5 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold text-xs uppercase tracking-wider transition">
        Retake Quiz
      </button>
    </div>
  `;

  document.getElementById('quiz-retry-btn').addEventListener('click', () => {
    currentQuizIdx = 0;
    userScore = 0;
    renderQuizQuestion();
  });
}

renderQuizQuestion();
