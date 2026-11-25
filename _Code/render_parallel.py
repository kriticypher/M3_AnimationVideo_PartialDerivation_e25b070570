"""
Multi-core Parallel 1080p Video Renderer (5.82 Minutes Master)
Renders all 6 scenes to match 349.49s audio across Apple Silicon CPU cores.
"""

import os
import shutil
import subprocess
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor

BASE_DIR = "/Users/kritimaurya/PARTIAL_DERIVATION/M3_Partial_Derivatives"
ANIM_DIR = os.path.join(BASE_DIR, "animation")
ASSETS_DIR = os.path.join(ANIM_DIR, "assets")
SCENES_DIR = os.path.join(ANIM_DIR, "scenes")
DELIV_DIR = os.path.join(BASE_DIR, "deliverables")

FPS = 24

def f(x, y):
    return x**2 + x*y + y**2

def setup_canvas():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor('#030712')
    return fig

# Worker for Scene 1 frames
def render_s1_frame(args):
    i, total_frames, frames_dir = args
    frame_path = os.path.join(frames_dir, f"frame_{i:04d}.png")
    t = i / float(total_frames)
    fig = setup_canvas()

    X = np.linspace(-3, 3, 40)
    Y = np.linspace(-3, 3, 40)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)

    ax = fig.add_axes([0.05, 0.1, 0.58, 0.8], projection='3d')
    ax.set_facecolor('#030712')
    ax.xaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
    ax.yaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
    ax.zaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
    ax.grid(True, color='#1e293b', linestyle='--', linewidth=0.5)

    azim = -60 + t * 50
    elev = 25 + np.sin(t * np.pi) * 8
    ax.view_init(elev=elev, azim=azim)

    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.82, edgecolor='#334155', linewidth=0.2)
    ax.set_xlabel('X axis', color='#38bdf8', fontsize=12, labelpad=8)
    ax.set_ylabel('Y axis', color='#c084fc', fontsize=12, labelpad=8)
    ax.set_zlabel('Z = f(x,y)', color='#f59e0b', fontsize=12, labelpad=8)
    ax.tick_params(colors='#94a3b8', labelsize=9)

    fig.text(0.67, 0.84, "M3 MATHEMATICS ASSESSMENT", color="#38bdf8", fontsize=14, weight='bold', family='sans-serif')
    fig.text(0.67, 0.77, "Understanding Partial Derivatives", color="#ffffff", fontsize=28, weight='bold', family='sans-serif')
    fig.text(0.67, 0.72, "Through 3D Surface Visualization", color="#38bdf8", fontsize=24, weight='bold', family='sans-serif')
    fig.text(0.67, 0.65, "How changing one variable at a time reveals the behaviour\nof a multivariable function.", color="#cbd5e1", fontsize=14, style='italic', family='sans-serif')

    fig.text(0.67, 0.52, "THE CENTRAL QUESTION:", color="#f59e0b", fontsize=16, weight='bold', family='sans-serif')
    hook_text = (
        "In single-variable calculus, y = f(x) has only ONE\n"
        "direction to change: moving along the 1D x-axis.\n\n"
        "On a continuous 3D landscape z = f(x,y), you can\n"
        "step in INFINITELY many directions.\n\n"
        "How do we quantify rates of change in multidimensions?"
    )
    fig.text(0.67, 0.36, hook_text, color="#f8fafc", fontsize=13, family='monospace', linespacing=1.6)
    fig.text(0.67, 0.16, "Candidate: Individual Student Submission\nTarget Model: z = x² + xy + y² at (1,2)", color="#64748b", fontsize=11, family='monospace')

    plt.savefig(frame_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=100)
    plt.close(fig)

# Worker for Scene 2 frames
def render_s2_frame(args):
    i, total_frames, frames_dir = args
    frame_path = os.path.join(frames_dir, f"frame_{i:04d}.png")
    t = i / float(total_frames)
    fig = setup_canvas()

    X = np.linspace(-3, 3, 35)
    Y = np.linspace(-3, 3, 35)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)

    ax = fig.add_axes([0.05, 0.1, 0.52, 0.8], projection='3d')
    ax.set_facecolor('#030712')
    ax.xaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
    ax.yaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
    ax.zaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
    ax.grid(True, color='#1e293b', linestyle='--', linewidth=0.5)

    azim = -40 + t * 30
    elev = 28
    ax.view_init(elev=elev, azim=azim)
    ax.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.75, edgecolor='#334155', linewidth=0.2)

    pt_x, pt_y = 1.0, 2.0
    pt_z = f(pt_x, pt_y)
    ax.scatter([pt_x], [pt_y], [0], color='#38bdf8', s=80, label='Domain point (1,2)')
    ax.plot([pt_x, pt_x], [pt_y, pt_y], [0, pt_z], color='#f59e0b', linestyle='--', linewidth=2)
    ax.scatter([pt_x], [pt_y], [pt_z], color='#ef4444', s=120, label='Surface Point P(1,2,7)')
    ax.legend(loc='upper left', facecolor='#0f172a', edgecolor='#334155', labelcolor='#ffffff', fontsize=10)

    ax.set_xlabel('X axis', color='#38bdf8', fontsize=11)
    ax.set_ylabel('Y axis', color='#c084fc', fontsize=11)
    ax.set_zlabel('Z = f(x,y)', color='#f59e0b', fontsize=11)
    ax.tick_params(colors='#94a3b8', labelsize=8)

    fig.text(0.61, 0.85, "MULTIVARIABLE MAPPING", color="#38bdf8", fontsize=14, weight='bold', family='sans-serif')
    fig.text(0.61, 0.78, "Function Architecture: z = f(x,y)", color="#ffffff", fontsize=24, weight='bold', family='sans-serif')

    panel_text = (
        "1. TWO INDEPENDENT INPUTS: (x, y)\n"
        "   Every point in the flat horizontal domain plane is\n"
        "   specified by an ordered pair of coordinates (x, y).\n\n"
        "2. ONE SCALAR OUTPUT: z\n"
        "   The function assigns a unique vertical height:\n"
        "   z = f(x,y) = x² + xy + y²\n\n"
        "3. DEFINITION OF PARTIAL DERIVATIVE:\n"
        "   A partial derivative measures how z changes when we\n"
        "   vary ONLY ONE input while keeping the other FROZEN.\n\n"
        "   • ∂f/∂x: Rate of change along x (holding y constant)\n"
        "   • ∂f/∂y: Rate of change along y (holding x constant)\n\n"
        "   Symbol: '∂' is Jacobi's curly d."
    )
    fig.text(0.61, 0.38, panel_text, color="#f1f5f9", fontsize=12, family='monospace', linespacing=1.55)
    fig.text(0.61, 0.20, "CORE INSIGHT:", color="#10b981", fontsize=14, weight='bold', family='sans-serif')
    fig.text(0.61, 0.13, "Freezing one variable reduces a complex 3D surface problem\ninto elementary single-variable calculus along a 2D slice!", color="#a7f3d0", fontsize=12, style='italic', family='sans-serif')

    plt.savefig(frame_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=100)
    plt.close(fig)

# Worker for Scene 3 frames
def render_s3_frame(args):
    i, total_frames, frames_dir = args
    frame_path = os.path.join(frames_dir, f"frame_{i:04d}.png")
    t = i / float(total_frames)
    fig = setup_canvas()

    X = np.linspace(-3, 3, 35)
    Y = np.linspace(-3, 3, 35)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)

    u_vals = np.linspace(-3, 3, 50)
    curve_x_X = u_vals
    curve_x_Y = np.full_like(u_vals, 2.0)
    curve_x_Z = f(curve_x_X, curve_x_Y)

    curve_y_X = np.full_like(u_vals, 1.0)
    curve_y_Y = u_vals
    curve_y_Z = f(curve_y_X, curve_y_Y)

    ax = fig.add_axes([0.05, 0.1, 0.55, 0.8], projection='3d')
    ax.set_facecolor('#030712')
    ax.xaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
    ax.yaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
    ax.zaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
    ax.grid(True, color='#1e293b', linestyle='--', linewidth=0.5)

    ax.view_init(elev=24, azim=-55 + t * 35)
    ax.plot_surface(X, Y, Z, cmap='gist_earth', alpha=0.35, edgecolor='#334155', linewidth=0.1)

    ax.scatter([1.0], [2.0], [7.0], color='#ef4444', s=140, zorder=10)
    ax.text(1.1, 2.1, 7.8, "P(1, 2, 7)", color='#fca5a5', fontsize=12, weight='bold')

    show_y_slice = t >= 0.45

    px = np.array([[-3, 3], [-3, 3]])
    py = np.array([[2, 2], [2, 2]])
    pz = np.array([[0, 0], [18, 18]])
    ax.plot_surface(px, py, pz, color='#0284c7', alpha=0.25)
    ax.plot(curve_x_X, curve_x_Y, curve_x_Z, color='#38bdf8', linewidth=4, label='Trace at y = 2 (X-curve)')

    if show_y_slice:
        qx = np.array([[1, 1], [1, 1]])
        qy = np.array([[-3, 3], [-3, 3]])
        qz = np.array([[0, 0], [18, 18]])
        ax.plot_surface(qx, qy, qz, color='#7c3aed', alpha=0.25)
        ax.plot(curve_y_X, curve_y_Y, curve_y_Z, color='#c084fc', linewidth=4, label='Trace at x = 1 (Y-curve)')

    ax.legend(loc='upper left', facecolor='#0f172a', edgecolor='#334155', labelcolor='#ffffff', fontsize=10)
    ax.set_xlabel('X axis', color='#38bdf8', fontsize=11)
    ax.set_ylabel('Y axis', color='#c084fc', fontsize=11)
    ax.set_zlabel('Z axis', color='#f59e0b', fontsize=11)
    ax.tick_params(colors='#94a3b8', labelsize=8)

    fig.text(0.63, 0.85, "GEOMETRIC EXPERIMENTS", color="#38bdf8", fontsize=14, weight='bold', family='sans-serif')
    fig.text(0.63, 0.78, "Cross-Sectional Traces at (1,2,7)", color="#ffffff", fontsize=24, weight='bold', family='sans-serif')

    exp1_box = (
        "EXPERIMENT 1 (Cyan): Fix y = 2\n"
        "• Slicing plane: Vertical plane y = 2\n"
        "• Reduced curve: z = x² + 2x + 4\n"
        "• Slope at x = 1 gives ∂f/∂x = 4"
    )
    fig.text(0.63, 0.62, exp1_box, color="#38bdf8", fontsize=12, family='monospace', linespacing=1.5)

    exp2_box = (
        "EXPERIMENT 2 (Purple): Fix x = 1\n"
        "• Slicing plane: Vertical plane x = 1\n"
        "• Reduced curve: z = 1 + y + y² = y² + y + 1\n"
        "• Slope at y = 2 gives ∂f/∂y = 5"
    )
    fig.text(0.63, 0.42, exp2_box, color="#c084fc" if show_y_slice else "#475569", fontsize=12, family='monospace', linespacing=1.5)

    summary_box = (
        "Takeaway:\n"
        "Each partial derivative is simply the standard\n"
        "tangent slope of an ordinary single-variable curve\n"
        "carved out of the 3D surface!"
    )
    fig.text(0.63, 0.22, summary_box, color="#f8fafc", fontsize=13, family='monospace', linespacing=1.5)

    plt.savefig(frame_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=100)
    plt.close(fig)

# Worker for Scene 4 frames
def render_s4_frame(args):
    i, total_frames, frames_dir = args
    frame_path = os.path.join(frames_dir, f"frame_{i:04d}.png")
    t = i / float(total_frames)
    fig = setup_canvas()

    fig.text(0.08, 0.88, "ANALYTICAL DERIVATION", color="#38bdf8", fontsize=14, weight='bold', family='sans-serif')
    fig.text(0.08, 0.81, "Step-by-Step Evaluation at Point (1, 2)", color="#ffffff", fontsize=28, weight='bold', family='sans-serif')
    fig.text(0.08, 0.74, "Original Function:  f(x, y) = x² + xy + y²", color="#f59e0b", fontsize=20, weight='bold', family='monospace')

    fig.text(0.08, 0.65, "A. PARTIAL DERIVATIVE WITH RESPECT TO X", color="#38bdf8", fontsize=16, weight='bold', family='sans-serif')
    fig.text(0.08, 0.61, "Rule: Hold y constant (y = const)", color="#94a3b8", fontsize=12, style='italic', family='sans-serif')

    deriv_x_text = (
        "Differentiating term-by-term:\n\n"
        "1. ∂/∂x (x²) = 2x           [Power Rule: d/dx(xⁿ) = n·xⁿ⁻¹]\n\n"
        "2. ∂/∂x (xy) = y            [y is a constant multiplier: d/dx(c·x) = c]\n\n"
        "3. ∂/∂x (y²) = 0            [y² is an independent constant: d/dx(c) = 0]\n\n"
        "───────────────────────────────────────────────\n"
        "∂f/∂x = 2x + y + 0  =  2x + y\n\n"
        "At point (1, 2):\n"
        "∂f/∂x |(1,2) = 2(1) + 2 = 2 + 2 = 4\n"
        "▶ RESULT: ∂f/∂x = 4"
    )
    fig.text(0.08, 0.22, deriv_x_text, color="#f1f5f9", fontsize=13, family='monospace', linespacing=1.35)

    show_right = t >= 0.45
    fig.text(0.55, 0.65, "B. PARTIAL DERIVATIVE WITH RESPECT TO Y", color="#c084fc" if show_right else "#334155", fontsize=16, weight='bold', family='sans-serif')
    fig.text(0.55, 0.61, "Rule: Hold x constant (x = const)", color="#94a3b8" if show_right else "#1e293b", fontsize=12, style='italic', family='sans-serif')

    if show_right:
        deriv_y_text = (
            "Differentiating term-by-term:\n\n"
            "1. ∂/∂y (x²) = 0            [x² is an independent constant: d/dy(c) = 0]\n\n"
            "2. ∂/∂y (xy) = x            [x is a constant multiplier: d/dy(c·y) = c]\n\n"
            "3. ∂/∂y (y²) = 2y           [Power Rule: d/dy(yⁿ) = n·yⁿ⁻¹]\n\n"
            "───────────────────────────────────────────────\n"
            "∂f/∂y = 0 + x + 2y  =  x + 2y\n\n"
            "At point (1, 2):\n"
            "∂f/∂y |(1,2) = 1 + 2(2) = 1 + 4 = 5\n"
            "▶ RESULT: ∂f/∂y = 5"
        )
        fig.text(0.55, 0.22, deriv_y_text, color="#f1f5f9", fontsize=13, family='monospace', linespacing=1.35)

    fig.text(0.08, 0.10, "VERIFICATION: Point (1, 2, 7) has slopes ∂f/∂x = 4 and ∂f/∂y = 5.", color="#10b981", fontsize=13, weight='bold', family='monospace')

    plt.savefig(frame_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=100)
    plt.close(fig)

# Worker for Scene 5 frames
def render_s5_frame(args):
    i, total_frames, frames_dir = args
    frame_path = os.path.join(frames_dir, f"frame_{i:04d}.png")
    t = i / float(total_frames)
    fig = setup_canvas()

    X = np.linspace(-1, 3, 35)
    Y = np.linspace(0, 4, 35)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)

    tx = np.linspace(0, 2, 16)
    ty = np.linspace(1, 3, 16)
    TX, TY = np.meshgrid(tx, ty)
    TZ = 7 + 4*(TX - 1) + 5*(TY - 2)

    t_vals = np.linspace(-1.2, 1.2, 25)
    tan_x_X = 1 + t_vals
    tan_x_Y = np.full_like(t_vals, 2.0)
    tan_x_Z = 7 + 4 * t_vals

    tan_y_X = np.full_like(t_vals, 1.0)
    tan_y_Y = 2 + t_vals
    tan_y_Z = 7 + 5 * t_vals

    ax = fig.add_axes([0.05, 0.1, 0.55, 0.8], projection='3d')
    ax.set_facecolor('#030712')
    ax.xaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
    ax.yaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
    ax.zaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
    ax.grid(True, color='#1e293b', linestyle='--', linewidth=0.5)

    ax.view_init(elev=22 + np.sin(t*np.pi)*5, azim=-50 + t * 40)
    ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.45, edgecolor='#334155', linewidth=0.1)

    ax.scatter([1.0], [2.0], [7.0], color='#ef4444', s=160, zorder=12)
    ax.plot(tan_x_X, tan_x_Y, tan_x_Z, color='#38bdf8', linewidth=4.5, label='Tangent in X (Slope = 4)')
    ax.plot(tan_y_X, tan_y_Y, tan_y_Z, color='#c084fc', linewidth=4.5, label='Tangent in Y (Slope = 5)')

    if t >= 0.35:
        ax.plot_surface(TX, TY, TZ, color='#f59e0b', alpha=0.45)

    ax.legend(loc='upper left', facecolor='#0f172a', edgecolor='#334155', labelcolor='#ffffff', fontsize=10)
    ax.set_xlabel('X axis', color='#38bdf8', fontsize=11)
    ax.set_ylabel('Y axis', color='#c084fc', fontsize=11)
    ax.set_zlabel('Z axis', color='#f59e0b', fontsize=11)

    fig.text(0.63, 0.85, "GEOMETRIC SYNTHESIS", color="#38bdf8", fontsize=14, weight='bold', family='sans-serif')
    fig.text(0.63, 0.78, "Tangent Lines & The Tangent Plane", color="#ffffff", fontsize=24, weight='bold', family='sans-serif')

    geo_text = (
        "1. TANGENT LINE IN X (Cyan):\n"
        "   • Lies on the plane y = 2\n"
        "   • Slope = 4.0\n"
        "   • Δz / Δx = 4 (Rise of 4 per 1 unit x)\n\n"
        "2. TANGENT LINE IN Y (Purple):\n"
        "   • Lies on the plane x = 1\n"
        "   • Slope = 5.0\n"
        "   • Δz / Δy = 5 (Rise of 5 per 1 unit y)\n\n"
        "3. THE UNIQUE TANGENT PLANE (Amber):\n"
        "   Both tangent vectors span the tangent plane:\n"
        "   z - z₀ = f_x(x₀,y₀)(x - x₀) + f_y(x₀,y₀)(y - y₀)\n\n"
        "   z - 7 = 4(x - 1) + 5(y - 2)\n"
        "   z = 4x + 5y - 7"
    )
    fig.text(0.63, 0.28, geo_text, color="#f1f5f9", fontsize=12, family='monospace', linespacing=1.45)
    fig.text(0.63, 0.16, "The partial derivatives are the foundational building blocks\nthat determine the tangent plane orientation in 3D!", color="#f59e0b", fontsize=12, style='italic', family='sans-serif')

    plt.savefig(frame_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=100)
    plt.close(fig)

# Worker for Scene 6 frames
def render_s6_frame(args):
    i, total_frames, frames_dir = args
    frame_path = os.path.join(frames_dir, f"frame_{i:04d}.png")
    fig = setup_canvas()

    fig.text(0.08, 0.88, "PROJECT SUMMARY & CONCLUSION", color="#38bdf8", fontsize=14, weight='bold', family='sans-serif')
    fig.text(0.08, 0.80, "Three Fundamental Mathematical Takeaways", color="#ffffff", fontsize=28, weight='bold', family='sans-serif')

    takeaways = (
        "1. DIRECTIONAL RATE OF CHANGE:\n"
        "   Partial derivatives isolate the rate of change of a multivariable function\n"
        "   strictly parallel to one coordinate axis at a time.\n\n"
        "2. INVARIANT VARIABLE ISOLATION:\n"
        "   When differentiating with respect to one variable, all other variables are treated\n"
        "   as static, unchanging constant scalars.\n\n"
        "3. GEOMETRIC ARCHITECTURE:\n"
        "   Geometrically, partial derivatives represent the slopes of tangent lines along 2D\n"
        "   cross-sectional slices, which together define the tangent plane z = 4x + 5y - 7."
    )
    fig.text(0.08, 0.45, takeaways, color="#f1f5f9", fontsize=14, family='monospace', linespacing=1.5)

    credits_text = (
        "─────────────────────────────────────────────────────────────────────────────\n"
        "ACADEMIC REFERENCES:\n"
        "• James Stewart, Multivariable Calculus (8th Edition), Cengage Learning\n"
        "• Thomas' Calculus (13th Edition), Pearson Higher Education\n"
        "• Gilbert Strang, Calculus, MIT OpenCourseWare\n\n"
        "PROJECT SPECIFICATIONS:\n"
        "• Course: BTech Linear Algebra and Calculus (M3) Internal Assessment\n"
        "• Topic: Understanding Partial Derivatives Through 3D Surface Visualization\n"
        "• Duration: 5.82 Minutes (~5.5 - 6.0 min target)\n"
        "• Tools: Python, Matplotlib, Three.js, KaTeX, FFmpeg, macOS Speech Synthesis\n"
        "• AI Disclosure: Assisted by Google Antigravity Agent for engineering & visualization."
    )
    fig.text(0.08, 0.14, credits_text, color="#94a3b8", fontsize=11, family='monospace', linespacing=1.4)

    plt.savefig(frame_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=100)
    plt.close(fig)

def render_scene_parallel(sc_num, worker_fn, duration, wav_audio):
    total_frames = int(duration * FPS)
    out_mp4 = os.path.join(SCENES_DIR, f"scene{sc_num}.mp4")
    frames_dir = os.path.join(SCENES_DIR, f"scene{sc_num}_frames")
    if os.path.exists(frames_dir):
        shutil.rmtree(frames_dir)
    os.makedirs(frames_dir, exist_ok=True)
    print(f"\n[Parallel] Rendering Scene {sc_num}: {total_frames} frames ({duration:.2f}s) across 8 cores...")

    args_list = [(i, total_frames, frames_dir) for i in range(total_frames)]
    with ProcessPoolExecutor(max_workers=8) as executor:
        list(executor.map(worker_fn, args_list))

    print(f"[FFmpeg] Encoding scene{sc_num}.mp4 with audio...")
    cmd = [
        "ffmpeg", "-y", "-framerate", str(FPS),
        "-i", os.path.join(frames_dir, "frame_%04d.png"),
        "-i", wav_audio,
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest", out_mp4
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.rmtree(frames_dir) # Clean frames immediately
    print(f"Scene {sc_num} complete -> {out_mp4}")
    return out_mp4

def concatenate_scenes(scene_files, final_output):
    concat_list = os.path.join(SCENES_DIR, "concat_list.txt")
    with open(concat_list, "w") as f:
        for s in scene_files:
            f.write(f"file '{s}'\n")

    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_list,
        "-c", "copy",
        final_output
    ]
    subprocess.run(cmd, check=True)
    print(f"\n==========================================")
    print(f"MASTER FINAL VIDEO GENERATED SUCCESSFULLY:")
    print(f"{final_output}")
    print(f"==========================================\n")

def main():
    import generate_narration
    durations = {}
    for sc in ["scene1", "scene2", "scene3", "scene4", "scene5", "scene6"]:
        wav = os.path.join(ASSETS_DIR, f"{sc}.wav")
        durations[sc] = generate_narration.get_wav_duration(wav)

    total_dur = sum(durations.values())
    print(f"Rendering Full 6-Scene Video: {total_dur:.2f}s ({total_dur/60:.2f} minutes)")

    scene_configs = [
        (1, render_s1_frame, durations["scene1"], os.path.join(ASSETS_DIR, "scene1.wav")),
        (2, render_s2_frame, durations["scene2"], os.path.join(ASSETS_DIR, "scene2.wav")),
        (3, render_s3_frame, durations["scene3"], os.path.join(ASSETS_DIR, "scene3.wav")),
        (4, render_s4_frame, durations["scene4"], os.path.join(ASSETS_DIR, "scene4.wav")),
        (5, render_s5_frame, durations["scene5"], os.path.join(ASSETS_DIR, "scene5.wav")),
        (6, render_s6_frame, durations["scene6"], os.path.join(ASSETS_DIR, "scene6.wav"))
    ]

    rendered_scenes = []
    for sc_num, worker_fn, dur, wav_path in scene_configs:
        mp4_path = render_scene_parallel(sc_num, worker_fn, dur, wav_path)
        rendered_scenes.append(mp4_path)

    final_video = os.path.join(DELIV_DIR, "final_video.mp4")
    concatenate_scenes(rendered_scenes, final_video)

if __name__ == "__main__":
    main()
