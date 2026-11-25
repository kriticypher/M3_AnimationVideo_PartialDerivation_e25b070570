"""
M3 Mathematics Educational Video Renderer
Title: Understanding Partial Derivatives Through 3D Surface Visualization
Function: f(x,y) = x^2 + xy + y^2 evaluated at (1,2)

Produces a genuine 1080p 60fps/24fps video across the strict six scenes,
combining dynamic 3D surface rotations, cross-sectional cutting planes,
secant-to-tangent limits, analytical step-by-step math cards,
and synchronizing with high-quality generated voice narration.
"""

import os
import sys
import subprocess
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from PIL import Image

BASE_DIR = "/Users/kritimaurya/PARTIAL_DERIVATION/M3_Partial_Derivatives"
ANIM_DIR = os.path.join(BASE_DIR, "animation")
ASSETS_DIR = os.path.join(ANIM_DIR, "assets")
SCENES_DIR = os.path.join(ANIM_DIR, "scenes")
DELIV_DIR = os.path.join(BASE_DIR, "deliverables")

os.makedirs(SCENES_DIR, exist_ok=True)
os.makedirs(DELIV_DIR, exist_ok=True)

# Math model
def f(x, y):
    return x**2 + x*y + y**2

def df_dx(x, y):
    return 2*x + y

def df_dy(x, y):
    return x + 2*y

FPS = 24  # High quality, fluid 24 fps

def setup_canvas():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100) # 1920 x 1080
    fig.patch.set_facecolor('#030712') # Deep slate navy
    return fig

def render_scene1(duration, out_mp4, wav_audio):
    """
    SCENE 1 — HOOK / CONTEXT (0:00 - 0:30)
    Rotating 3D surface, title overlays, presenting the core question.
    """
    total_frames = int(duration * FPS)
    print(f"Rendering Scene 1: {total_frames} frames...")
    frames_dir = os.path.join(SCENES_DIR, "scene1_frames")
    os.makedirs(frames_dir, exist_ok=True)

    X = np.linspace(-3, 3, 50)
    Y = np.linspace(-3, 3, 50)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)

    for i in range(total_frames):
        t = i / float(total_frames)
        fig = setup_canvas()
        
        # 3D plot on left/center
        ax = fig.add_axes([0.05, 0.1, 0.58, 0.8], projection='3d')
        ax.set_facecolor('#030712')
        ax.xaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
        ax.yaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
        ax.zaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
        ax.grid(True, color='#1e293b', linestyle='--', linewidth=0.5)

        azim = -60 + t * 45
        elev = 25 + np.sin(t * np.pi) * 8
        ax.view_init(elev=elev, azim=azim)

        # Surface
        surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.82, edgecolor='#334155', linewidth=0.2)
        ax.set_xlabel('X axis', color='#38bdf8', fontsize=12, labelpad=8)
        ax.set_ylabel('Y axis', color='#c084fc', fontsize=12, labelpad=8)
        ax.set_zlabel('Z = f(x,y)', color='#f59e0b', fontsize=12, labelpad=8)
        ax.tick_params(colors='#94a3b8', labelsize=9)

        # Right side text typography
        # Header banner
        fig.text(0.67, 0.84, "M3 MATHEMATICS ASSESSMENT", color="#38bdf8", fontsize=14, weight='bold', family='sans-serif')
        fig.text(0.67, 0.77, "Understanding Partial Derivatives", color="#ffffff", fontsize=28, weight='bold', family='sans-serif')
        fig.text(0.67, 0.72, "Through 3D Surface Visualization", color="#38bdf8", fontsize=24, weight='bold', family='sans-serif')
        fig.text(0.67, 0.65, "How changing one variable at a time reveals the behaviour\nof a multivariable function.", color="#cbd5e1", fontsize=14, style='italic', family='sans-serif')

        # Hook box
        fig.text(0.67, 0.52, "THE CENTRAL QUESTION:", color="#f59e0b", fontsize=16, weight='bold', family='sans-serif')
        hook_text = (
            "In single-variable calculus, y = f(x) has only ONE\n"
            "direction to change: moving along the 1D x-axis.\n\n"
            "On a continuous 3D landscape z = f(x,y), you can\n"
            "step in INFINITELY many directions.\n\n"
            "How do we quantify rates of change in multidimensions?"
        )
        fig.text(0.67, 0.36, hook_text, color="#f8fafc", fontsize=13, family='monospace', linespacing=1.6)

        # Meta footer
        fig.text(0.67, 0.16, "Candidate: Individual Student Submission\nTarget Model: z = x² + xy + y² at (1,2)", color="#64748b", fontsize=11, family='monospace')

        # Save frame
        frame_path = os.path.join(frames_dir, f"frame_{i:04d}.png")
        plt.savefig(frame_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=100)
        plt.close(fig)

    # Encode with audio
    cmd = [
        "ffmpeg", "-y", "-framerate", str(FPS),
        "-i", os.path.join(frames_dir, "frame_%04d.png"),
        "-i", wav_audio,
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest", out_mp4
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Scene 1 generated: {out_mp4}")


def render_scene2(duration, out_mp4, wav_audio):
    """
    SCENE 2 — CONCEPT INTRODUCTION (0:30 - 1:10)
    Two inputs (x,y) -> One output z. Definition of partial derivative.
    """
    total_frames = int(duration * FPS)
    print(f"Rendering Scene 2: {total_frames} frames...")
    frames_dir = os.path.join(SCENES_DIR, "scene2_frames")
    os.makedirs(frames_dir, exist_ok=True)

    X = np.linspace(-3, 3, 40)
    Y = np.linspace(-3, 3, 40)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)

    for i in range(total_frames):
        t = i / float(total_frames)
        fig = setup_canvas()

        # Left 3D plot
        ax = fig.add_axes([0.05, 0.1, 0.52, 0.8], projection='3d')
        ax.set_facecolor('#030712')
        ax.xaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
        ax.yaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
        ax.zaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
        ax.grid(True, color='#1e293b', linestyle='--', linewidth=0.5)

        azim = -40 + t * 25
        elev = 28
        ax.view_init(elev=elev, azim=azim)

        ax.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.75, edgecolor='#334155', linewidth=0.2)
        
        # Highlight grid point on ground plane
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

        # Right explanatory pedagogical panel
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
            "   • ∂f/∂y: Rate of change along y (holding x constant)"
        )
        fig.text(0.61, 0.42, panel_text, color="#f1f5f9", fontsize=13, family='monospace', linespacing=1.6)

        # Highlight callout box
        fig.text(0.61, 0.22, "CORE INSIGHT:", color="#10b981", fontsize=14, weight='bold', family='sans-serif')
        fig.text(0.61, 0.15, "Freezing one variable reduces a complex 3D surface problem\ninto elementary single-variable calculus along a 2D slice!", color="#a7f3d0", fontsize=12, style='italic', family='sans-serif')

        frame_path = os.path.join(frames_dir, f"frame_{i:04d}.png")
        plt.savefig(frame_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=100)
        plt.close(fig)

    cmd = [
        "ffmpeg", "-y", "-framerate", str(FPS),
        "-i", os.path.join(frames_dir, "frame_%04d.png"),
        "-i", wav_audio,
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest", out_mp4
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Scene 2 generated: {out_mp4}")


def render_scene3(duration, out_mp4, wav_audio):
    """
    SCENE 3 — VISUAL INTUITION: CROSS-SECTIONS (1:10 - 2:10)
    Point P(1,2,7). Animates Plane y=2 (Cyan curve) then Plane x=1 (Purple curve).
    """
    total_frames = int(duration * FPS)
    print(f"Rendering Scene 3: {total_frames} frames...")
    frames_dir = os.path.join(SCENES_DIR, "scene3_frames")
    os.makedirs(frames_dir, exist_ok=True)

    X = np.linspace(-3, 3, 40)
    Y = np.linspace(-3, 3, 40)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)

    # Cross section curves
    u_vals = np.linspace(-3, 3, 60)
    # y = 2
    curve_x_X = u_vals
    curve_x_Y = np.full_like(u_vals, 2.0)
    curve_x_Z = f(curve_x_X, curve_x_Y)
    # x = 1
    curve_y_X = np.full_like(u_vals, 1.0)
    curve_y_Y = u_vals
    curve_y_Z = f(curve_y_X, curve_y_Y)

    for i in range(total_frames):
        t = i / float(total_frames)
        fig = setup_canvas()

        ax = fig.add_axes([0.05, 0.1, 0.55, 0.8], projection='3d')
        ax.set_facecolor('#030712')
        ax.xaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
        ax.yaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
        ax.zaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
        ax.grid(True, color='#1e293b', linestyle='--', linewidth=0.5)

        ax.view_init(elev=24, azim=-55 + t * 30)

        # Base Surface (semi-transparent)
        ax.plot_surface(X, Y, Z, cmap='gist_earth', alpha=0.35, edgecolor='#334155', linewidth=0.1)

        # Highlight Point P(1,2,7)
        ax.scatter([1.0], [2.0], [7.0], color='#ef4444', s=140, zorder=10)
        ax.text(1.1, 2.1, 7.8, "P(1, 2, 7)", color='#fca5a5', fontsize=12, weight='bold')

        # Phase 1: show y=2 plane and x-curve (t < 0.5)
        # Phase 2: also show x=1 plane and y-curve (t >= 0.5)
        show_y_slice = t >= 0.45

        # Cutting Plane y = 2
        px = np.array([[-3, 3], [-3, 3]])
        py = np.array([[2, 2], [2, 2]])
        pz = np.array([[0, 0], [18, 18]])
        ax.plot_surface(px, py, pz, color='#0284c7', alpha=0.25)
        # 2D cross section curve in x
        ax.plot(curve_x_X, curve_x_Y, curve_x_Z, color='#38bdf8', linewidth=4, label='Trace at y = 2 (X-curve)')

        if show_y_slice:
            # Cutting Plane x = 1
            qx = np.array([[1, 1], [1, 1]])
            qy = np.array([[-3, 3], [-3, 3]])
            qz = np.array([[0, 0], [18, 18]])
            ax.plot_surface(qx, qy, qz, color='#7c3aed', alpha=0.25)
            # 2D cross section curve in y
            ax.plot(curve_y_X, curve_y_Y, curve_y_Z, color='#c084fc', linewidth=4, label='Trace at x = 1 (Y-curve)')

        ax.legend(loc='upper left', facecolor='#0f172a', edgecolor='#334155', labelcolor='#ffffff', fontsize=10)
        ax.set_xlabel('X axis', color='#38bdf8', fontsize=11)
        ax.set_ylabel('Y axis', color='#c084fc', fontsize=11)
        ax.set_zlabel('Z axis', color='#f59e0b', fontsize=11)
        ax.tick_params(colors='#94a3b8', labelsize=8)

        # Right descriptive text
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

        frame_path = os.path.join(frames_dir, f"frame_{i:04d}.png")
        plt.savefig(frame_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=100)
        plt.close(fig)

    cmd = [
        "ffmpeg", "-y", "-framerate", str(FPS),
        "-i", os.path.join(frames_dir, "frame_%04d.png"),
        "-i", wav_audio,
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest", out_mp4
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Scene 3 generated: {out_mp4}")


def render_scene4(duration, out_mp4, wav_audio):
    """
    SCENE 4 — STEP-BY-STEP WORKED EXAMPLE (2:10 - 3:40)
    Derive ∂f/∂x = 2x+y = 4 and ∂f/∂y = x+2y = 5 with term-by-term breakdown.
    """
    total_frames = int(duration * FPS)
    print(f"Rendering Scene 4: {total_frames} frames...")
    frames_dir = os.path.join(SCENES_DIR, "scene4_frames")
    os.makedirs(frames_dir, exist_ok=True)

    for i in range(total_frames):
        t = i / float(total_frames)
        fig = setup_canvas()

        # Title
        fig.text(0.08, 0.88, "ANALYTICAL DERIVATION", color="#38bdf8", fontsize=14, weight='bold', family='sans-serif')
        fig.text(0.08, 0.81, "Step-by-Step Evaluation at Point (1, 2)", color="#ffffff", fontsize=28, weight='bold', family='sans-serif')
        fig.text(0.08, 0.74, "Original Function:  f(x, y) = x² + xy + y²", color="#f59e0b", fontsize=20, weight='bold', family='monospace')

        # Left Column: ∂f/∂x (Blue)
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

        # Right Column: ∂f/∂y (Purple) - Animated appearance based on t
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

        # Bottom verification bar
        fig.text(0.08, 0.10, "VERIFICATION: Point (1, 2, 7) has slopes ∂f/∂x = 4 and ∂f/∂y = 5.", color="#10b981", fontsize=13, weight='bold', family='monospace')

        frame_path = os.path.join(frames_dir, f"frame_{i:04d}.png")
        plt.savefig(frame_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=100)
        plt.close(fig)

    cmd = [
        "ffmpeg", "-y", "-framerate", str(FPS),
        "-i", os.path.join(frames_dir, "frame_%04d.png"),
        "-i", wav_audio,
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest", out_mp4
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Scene 4 generated: {out_mp4}")


def render_scene5(duration, out_mp4, wav_audio):
    """
    SCENE 5 — GEOMETRIC INTERPRETATION & TANGENT PLANE (3:40 - 4:30)
    3D visualization showing tangent lines slope 4 & 5, and tangent plane z-7 = 4(x-1)+5(y-2).
    """
    total_frames = int(duration * FPS)
    print(f"Rendering Scene 5: {total_frames} frames...")
    frames_dir = os.path.join(SCENES_DIR, "scene5_frames")
    os.makedirs(frames_dir, exist_ok=True)

    X = np.linspace(-1, 3, 40)
    Y = np.linspace(0, 4, 40)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)

    # Tangent plane grid around (1,2)
    tx = np.linspace(0, 2, 20)
    ty = np.linspace(1, 3, 20)
    TX, TY = np.meshgrid(tx, ty)
    # z - 7 = 4(x - 1) + 5(y - 2) => z = 7 + 4(x - 1) + 5(y - 2)
    TZ = 7 + 4*(TX - 1) + 5*(TY - 2)

    # Tangent lines
    t_vals = np.linspace(-1.2, 1.2, 30)
    # X tangent: x = 1 + t, y = 2, z = 7 + 4*t
    tan_x_X = 1 + t_vals
    tan_x_Y = np.full_like(t_vals, 2.0)
    tan_x_Z = 7 + 4 * t_vals

    # Y tangent: x = 1, y = 2 + t, z = 7 + 5*t
    tan_y_X = np.full_like(t_vals, 1.0)
    tan_y_Y = 2 + t_vals
    tan_y_Z = 7 + 5 * t_vals

    for i in range(total_frames):
        t = i / float(total_frames)
        fig = setup_canvas()

        ax = fig.add_axes([0.05, 0.1, 0.55, 0.8], projection='3d')
        ax.set_facecolor('#030712')
        ax.xaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
        ax.yaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
        ax.zaxis.set_pane_color((0.02, 0.04, 0.08, 0.8))
        ax.grid(True, color='#1e293b', linestyle='--', linewidth=0.5)

        ax.view_init(elev=22 + np.sin(t*np.pi)*5, azim=-50 + t * 35)

        # Surface
        ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.45, edgecolor='#334155', linewidth=0.1)

        # Highlight point P
        ax.scatter([1.0], [2.0], [7.0], color='#ef4444', s=160, zorder=12)

        # Tangent line X (Cyan)
        ax.plot(tan_x_X, tan_x_Y, tan_x_Z, color='#38bdf8', linewidth=4.5, label='Tangent in X (Slope = 4)')

        # Tangent line Y (Purple)
        ax.plot(tan_y_X, tan_y_Y, tan_y_Z, color='#c084fc', linewidth=4.5, label='Tangent in Y (Slope = 5)')

        # Tangent Plane appears at t > 0.35
        if t >= 0.35:
            ax.plot_surface(TX, TY, TZ, color='#f59e0b', alpha=0.45)

        ax.legend(loc='upper left', facecolor='#0f172a', edgecolor='#334155', labelcolor='#ffffff', fontsize=10)
        ax.set_xlabel('X axis', color='#38bdf8', fontsize=11)
        ax.set_ylabel('Y axis', color='#c084fc', fontsize=11)
        ax.set_zlabel('Z axis', color='#f59e0b', fontsize=11)

        # Right descriptive text
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

        frame_path = os.path.join(frames_dir, f"frame_{i:04d}.png")
        plt.savefig(frame_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=100)
        plt.close(fig)

    cmd = [
        "ffmpeg", "-y", "-framerate", str(FPS),
        "-i", os.path.join(frames_dir, "frame_%04d.png"),
        "-i", wav_audio,
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest", out_mp4
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Scene 5 generated: {out_mp4}")


def render_scene6(duration, out_mp4, wav_audio):
    """
    SCENE 6 — SUMMARY & CREDITS (4:30 - 5:00)
    Core takeaways, references, academic submission credits, AI disclosure.
    """
    total_frames = int(duration * FPS)
    print(f"Rendering Scene 6: {total_frames} frames...")
    frames_dir = os.path.join(SCENES_DIR, "scene6_frames")
    os.makedirs(frames_dir, exist_ok=True)

    for i in range(total_frames):
        fig = setup_canvas()

        # Header
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

        # Credits & References Box
        credits_text = (
            "─────────────────────────────────────────────────────────────────────────────\n"
            "ACADEMIC REFERENCES:\n"
            "• James Stewart, Multivariable Calculus (8th Edition), Cengage Learning\n"
            "• Thomas' Calculus (13th Edition), Pearson Higher Education\n"
            "• Gilbert Strang, Calculus, MIT OpenCourseWare\n\n"
            "PROJECT SPECIFICATIONS:\n"
            "• Course: BTech Linear Algebra and Calculus (M3) Internal Assessment\n"
            "• Topic: Understanding Partial Derivatives Through 3D Surface Visualization\n"
            "• Tools: Python, Matplotlib, Three.js, KaTeX, FFmpeg, macOS Speech Synthesis\n"
            "• AI Disclosure: Assisted by Google Antigravity Agent for engineering & visualization."
        )
        fig.text(0.08, 0.14, credits_text, color="#94a3b8", fontsize=11, family='monospace', linespacing=1.4)

        frame_path = os.path.join(frames_dir, f"frame_{i:04d}.png")
        plt.savefig(frame_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=100)
        plt.close(fig)

    cmd = [
        "ffmpeg", "-y", "-framerate", str(FPS),
        "-i", os.path.join(frames_dir, "frame_%04d.png"),
        "-i", wav_audio,
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest", out_mp4
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Scene 6 generated: {out_mp4}")


def concatenate_scenes(scene_files, final_output):
    """
    Concatenate all 6 scene mp4 files into final_video.mp4 using ffmpeg concat demuxer.
    """
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
    print(f"\nSUCCESS: Generated Final Master Video -> {final_output}")


def main():
    import generate_narration

    # 1. Ensure narration audio files exist
    print("Checking narration audio...")
    durations = {}
    for sc in ["scene1", "scene2", "scene3", "scene4", "scene5", "scene6"]:
        wav = os.path.join(ASSETS_DIR, f"{sc}.wav")
        if not os.path.exists(wav):
            print(f"Generating narration audio for {sc}...")
            generate_narration.main()
            break
        durations[sc] = generate_narration.get_wav_duration(wav)

    print("Audio Durations:", durations)

    scene_renderers = [
        ("scene1", render_scene1),
        ("scene2", render_scene2),
        ("scene3", render_scene3),
        ("scene4", render_scene4),
        ("scene5", render_scene5),
        ("scene6", render_scene6)
    ]

    rendered_scenes = []
    for sc_name, renderer in scene_renderers:
        out_mp4 = os.path.join(SCENES_DIR, f"{sc_name}.mp4")
        wav_audio = os.path.join(ASSETS_DIR, f"{sc_name}.wav")
        dur = durations[sc_name]
        renderer(dur, out_mp4, wav_audio)
        rendered_scenes.append(out_mp4)

    # Concatenate to final video
    final_video = os.path.join(DELIV_DIR, "final_video.mp4")
    concatenate_scenes(rendered_scenes, final_video)

if __name__ == "__main__":
    main()
