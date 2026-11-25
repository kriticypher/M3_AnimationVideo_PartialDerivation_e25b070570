import os
import subprocess
import wave
import contextlib

def get_wav_duration(path):
    with contextlib.closing(wave.open(path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        return frames / float(rate)

def main():
    assets_dir = "/Users/kritimaurya/PARTIAL_DERIVATION/M3_Partial_Derivatives/animation/assets"
    os.makedirs(assets_dir, exist_ok=True)

    # Rate 168 wpm precisely targets 340-350 seconds (5.67 - 5.8 minutes)
    scenes_text = {
        "scene1": (
            "What happens when a mathematical function depends on two independent variables, but we want to understand how changing just one variable at a time affects its total output? "
            "In single-variable calculus, finding a derivative is straightforward: because the input resides on a one-dimensional line, there is only one direction along the curve to move. "
            "But on a continuous three-dimensional landscape, you have infinite degrees of freedom and can move in infinitely many directions. "
            "How do we make sense of rates of change in multidimensional space? "
            "Welcome to Understanding Partial Derivatives Through Three-Dimensional Surface Visualization."
        ),
        "scene2": (
            "Let us introduce a multivariable function: z equals f of x and y. "
            "Here, two independent real numbers, x and y, act as coordinate inputs that determine a single scalar output, the vertical height z. "
            "Plotted across a continuous two-dimensional domain, this mapping generates a smooth, curved three-dimensional surface in Euclidean space. "
            "A partial derivative is fundamentally about answering a very specific question: "
            "if we freeze one of our input coordinates and nudge only the other, at what instantaneous rate does our elevation z respond? "
            "We denote these fundamental directional rates of change as partial f with respect to x, and partial f with respect to y. "
            "Notice the special stylized symbol, known as Jacobi's curly d, which distinguishes partial differentiation from ordinary single-variable derivatives."
        ),
        "scene3": (
            "Consider our central mathematical model: f of x and y equals x squared plus x times y plus y squared. "
            "Let us focus on the specific point where x equals 1 and y equals 2. "
            "Evaluating the function gives 1 squared plus 1 times 2 plus 2 squared, which equals 7. "
            "This locates point P at coordinates (1, 2, 7) on the surface. "
            "Now, how do we observe the partial derivative with respect to x visually? "
            "We hold y constant at 2. "
            "Visually, this corresponds to slicing cleanly through our three-dimensional surface with a vertical cutting plane at y equals 2. "
            "Look closely at the intersection: it is an exact, two-dimensional parabola! "
            "Next, to observe the partial derivative with respect to y, we hold x constant at 1. "
            "A vertical plane at x equals 1 cuts through the surface, producing an orthogonal cross-sectional trace. "
            "By freezing one coordinate, multivariable calculus eliminates the multidirectional ambiguity and simplifies directly back into elementary single-variable calculus along a single planar curve."
        ),
        "scene4": (
            "Now let us compute both partial derivatives analytically. "
            "Our function is f of x and y equals x squared plus x times y plus y squared. "
            "First, let us find the partial derivative with respect to x. "
            "When differentiating with respect to x, variable y is treated as an unchanging constant scalar. "
            "Let us examine each term carefully: "
            "Term one: the derivative of x squared with respect to x is 2x, following the standard single-variable power rule. "
            "Term two: for x times y, because y is treated as a constant scalar multiplier, the derivative with respect to x is simply y. "
            "Term three: for y squared, because y does not depend on x, y squared is an absolute constant scalar. And the derivative of any constant is zero! "
            "Combining these terms gives: partial f with respect to x equals 2x plus y. "
            "Evaluating this rate at point (1, 2), we substitute x equals 1 and y equals 2: 2 times 1 plus 2 equals 4. "
            "This means for every unit step in the positive x direction, z rises at an instantaneous rate of 4. "
            "Next, let us differentiate with respect to y. Here, x is treated as an unchanging constant. "
            "The derivative of x squared with respect to y is 0, because x is constant. "
            "The derivative of x times y with respect to y is x, because x is the constant coefficient. "
            "The derivative of y squared with respect to y is 2y, by the power rule. "
            "Thus, partial f with respect to y equals x plus 2y. "
            "Evaluating at (1, 2), we substitute x equals 1 and y equals 2: 1 plus 2 times 2 equals 5. "
            "Analytically, our directional slopes are exactly 4 in the x direction, and 5 in the y direction."
        ),
        "scene5": (
            "Let us return to the three-dimensional surface to witness what these numerical values truly represent in space. "
            "Along the cross-sectional trace where y equals 2, the cyan tangent line touches the curve at (1, 2, 7). "
            "Its slope is exactly 4. "
            "That means the instantaneous rate of elevation change parallel to the x-axis is 4 units of rise per unit of run. "
            "Along the cross-sectional trace where x equals 1, the purple tangent line touches the curve. "
            "Its slope is 5, meaning a step forward along the positive y-axis yields an elevation increase of 5 units. "
            "Together, these two orthogonal tangent lines span a unique, flat plane: the tangent plane at (1, 2, 7). "
            "Its mathematical formula is z minus z naught equals f sub x times (x minus x naught) plus f sub y times (y minus y naught), which becomes z minus 7 equals 4 times (x minus 1) plus 5 times (y minus 2), or z equals 4x plus 5y minus 7. "
            "The partial derivatives provide the exact directional slopes that establish the orientation of this tangent plane in three-dimensional space."
        ),
        "scene6": (
            "To summarize our multivariable insights: "
            "First, partial derivatives measure the rate of change of a multivariable function with respect to one variable at a time. "
            "Second, to evaluate a partial derivative, all other independent variables are held strictly constant. "
            "Third, geometrically, partial derivatives represent the slopes of tangent lines along two-dimensional cross-sectional slices, which together construct the unique local tangent plane. "
            "Thank you for exploring the geometry of multivariable calculus."
        )
    }

    durations = {}
    for scene_id, text in scenes_text.items():
        aiff_path = os.path.join(assets_dir, f"{scene_id}.aiff")
        wav_path = os.path.join(assets_dir, f"{scene_id}.wav")
        cmd_say = ["say", "-v", "Samantha", "-r", "168", "-o", aiff_path, text]
        subprocess.run(cmd_say, check=True)
        cmd_conv = ["ffmpeg", "-y", "-i", aiff_path, "-ar", "44100", "-ac", "2", wav_path]
        subprocess.run(cmd_conv, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        dur = get_wav_duration(wav_path)
        durations[scene_id] = dur
        print(f"Generated {scene_id}.wav: {dur:.2f} seconds")

    total_dur = sum(durations.values())
    print(f"\n==========================================")
    print(f"Total Narration Duration: {total_dur:.2f} seconds ({total_dur/60:.2f} minutes)")
    print(f"Target Window: 5.5 to 6.0 minutes")
    print(f"==========================================\n")

if __name__ == "__main__":
    main()
