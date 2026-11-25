"""
Professional Storyboard PDF Generator
Generates deliverables/storyboard.pdf detailing all 6 scenes according to the exact project guidelines.
"""

import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

BASE_DIR = "/Users/kritimaurya/PARTIAL_DERIVATION/M3_Partial_Derivatives"
OUTPUT_PDF = os.path.join(BASE_DIR, "deliverables", "storyboard.pdf")

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Header rule & title
        self.setStrokeColor(colors.HexColor("#334155"))
        self.setLineWidth(0.5)
        self.line(40, 575, 752, 575)
        self.drawString(40, 582, "M3 Mathematics Internal Assessment — 6-Scene Educational Video Storyboard")
        self.drawRightString(752, 582, "Topic: Partial Derivatives & 3D Visualization")

        # Footer rule & page
        self.line(40, 35, 752, 35)
        self.drawString(40, 24, "Academic Submission • BTech Linear Algebra and Calculus (M3)")
        self.drawRightString(752, 24, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=landscape(letter),
        leftMargin=40,
        rightMargin=40,
        topMargin=50,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#334155'),
        spaceAfter=15
    )

    scene_heading_style = ParagraphStyle(
        'SceneHead',
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#0284c7'),
        spaceBefore=10,
        spaceAfter=6
    )

    label_style = ParagraphStyle(
        'CellLabel',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#1e293b')
    )

    body_style = ParagraphStyle(
        'CellBody',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#334155')
    )

    math_style = ParagraphStyle(
        'CellMath',
        fontName='Courier-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#0f172a')
    )

    narration_style = ParagraphStyle(
        'CellNarration',
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#1e293b')
    )

    story = []

    # Title Banner
    story.append(Paragraph("Understanding Partial Derivatives Through 3D Surface Visualization", title_style))
    story.append(Paragraph("Complete Six-Scene Master Animation Storyboard & Academic Production Plan", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#0284c7"), spaceAfter=12))

    # Scene Data
    scenes = [
        {
            "num": "SCENE 1",
            "title": "Hook / Multivariable Context",
            "time": "0:00 – 0:30 (30s)",
            "purpose": "Engage student interest by contrasting 1D single-variable motion with unconstrained 3D motion, formulating the central question.",
            "visual": "Dynamic rotating 3D surface plot of z = x² + xy + y² rendered in high-contrast viridis colormap. Glowing coordinate axes, animated camera rotation, clear title typography overlays.",
            "math": "z = f(x,y)\nDomain: (x,y) in R²\nRange: z in R",
            "narration": "\"What happens when a function depends on two variables, but we want to understand how changing just one variable affects its output? In single-variable calculus, finding a derivative is simple: there is only one direction along the curve to move. But on a continuous 3D landscape, you can move in infinitely many directions. How do we make sense of rates of change in multidimensional space? Welcome to Understanding Partial Derivatives Through 3D Surface Visualization.\"",
            "transition": "Smooth orbital camera pan down into the xy-coordinate floor as Scene 2 begins."
        },
        {
            "num": "SCENE 2",
            "title": "Concept Introduction & Mapping",
            "time": "0:30 – 1:10 (40s)",
            "purpose": "Establish the rigorous definition of a two-variable scalar function, input-output coordinates, and the motivation for isolating directional rates of change.",
            "visual": "Split viewport: Left showcases the 3D surface with a highlighted domain coordinate (1,2) and its vertical projection up to height z=7. Right shows crisp typography defining inputs, outputs, and the partial symbols ∂f/∂x and ∂f/∂y.",
            "math": "z = f(x,y) = x² + xy + y²\nPoint: (x₀, y₀) = (1, 2) → z₀ = 7\nSymbols: ∂f/∂x,  ∂f/∂y",
            "narration": "\"Let us introduce a multivariable function: z equals f of x and y. Here, two independent real numbers, x and y, act as inputs that determine a single output, the height z. Plotted across a continuous grid, this generates a curved three-dimensional surface. A partial derivative is fundamentally about answering a focused question: if we freeze one of our input coordinates and nudge only the other, at what instantaneous rate does our elevation z respond? We denote these rates of change as ∂f/∂x and ∂f/∂y.\"",
            "transition": "Camera locks into an isometric viewing angle focused on target point P(1, 2, 7)."
        },
        {
            "num": "SCENE 3",
            "title": "Visual Intuition: Cross-Sections",
            "time": "1:10 – 2:10 (60s)",
            "purpose": "The core geometric breakthrough: demonstrating that holding one variable constant slices the 3D surface into single-variable 2D curves.",
            "visual": "Point P(1,2,7) highlighted with a pulsating red sphere. Experiment 1: Translucent blue vertical plane y=2 cuts the surface, tracing a bright cyan 2D parabola. Experiment 2: Translucent purple vertical plane x=1 cuts the surface, tracing a bright purple 2D parabola.",
            "math": "Experiment 1: y = 2 → z = x² + 2x + 4 (Cyan)\nExperiment 2: x = 1 → z = y² + y + 1 (Purple)\nPoint P = (1, 2, 7)",
            "narration": "\"Consider our central mathematical model: f(x,y) = x² + xy + y². Let us focus on the specific point (1, 2). Evaluating the function gives 1² + (1)(2) + 2² = 7, locating point P at coordinates (1, 2, 7) on the surface. Now, how do we observe the partial derivative with respect to x? We hold y constant at 2. Visually, this means slicing through our 3D surface with a vertical plane at y = 2. Look at the intersection: it is a pure two-dimensional curve! Next, to observe the partial derivative with respect to y, we hold x constant at 1. A vertical plane at x = 1 intersects the landscape, producing an orthogonal cross-sectional curve. By freezing one degree of freedom, multivariable calculus simplifies directly back into single-variable calculus.\"",
            "transition": "Cut smoothly to high-contrast pedagogical math derivation card."
        },
        {
            "num": "SCENE 4",
            "title": "Step-by-Step Analytical Derivation",
            "time": "2:10 – 3:40 (90s)",
            "purpose": "Provide absolute mathematical rigor. Walk through every term of x² + xy + y² for both ∂f/∂x and ∂f/∂y, verifying numerical values 4 and 5.",
            "visual": "Two-column analytical dashboard. Left column highlights ∂f/∂x in cyan, annotating terms x² → 2x, xy → y, and y² → 0. Right column highlights ∂f/∂y in purple, annotating x² → 0, xy → x, and y² → 2y. Substitution of (1,2) highlighted with glowing borders.",
            "math": "∂/∂x[x²] = 2x,  ∂/∂x[xy] = y,  ∂/∂x[y²] = 0\n∂f/∂x = 2x + y → 2(1) + 2 = 4\n\n∂/∂y[x²] = 0,  ∂/∂y[xy] = x,  ∂/∂y[y²] = 2y\n∂f/∂y = x + 2y → 1 + 2(2) = 5",
            "narration": "\"Now let us compute both partial derivatives analytically. Our function is f(x,y) = x² + xy + y². First, let us find the partial derivative with respect to x. When differentiating with respect to x, variable y is treated as an unchanging constant scalar. The derivative of x² with respect to x is 2x, by the standard power rule. For the term xy, because y is a constant multiplier, its derivative is simply y. For y², since y is an independent constant, y² is also constant; its derivative is zero! Combining gives: ∂f/∂x = 2x + y. Evaluating at (1, 2): 2(1) + 2 = 4. Next, differentiating with respect to y: x² becomes 0, xy becomes x, and y² becomes 2y. Thus ∂f/∂y = x + 2y. Evaluating at (1, 2): 1 + 2(2) = 5. Analytically, our slopes in the x and y directions are exactly 4 and 5.\"",
            "transition": "Return to the 3D surface view to connect the numerical values 4 and 5 directly to geometry."
        },
        {
            "num": "SCENE 5",
            "title": "Geometric Synthesis & Tangent Plane",
            "time": "3:40 – 4:30 (50s)",
            "purpose": "Showcase tangent vectors with slopes 4 and 5 touching the traces at P(1,2,7), and show how together they span the unique tangent plane.",
            "visual": "Point P(1,2,7) on 3D surface. Solid cyan tangent line drawn along plane y=2 (slope=4). Solid purple tangent line drawn along plane x=1 (slope=5). Semi-transparent amber tangent plane z = 4x + 5y - 7 materializes, resting tangentially on the curved surface.",
            "math": "Tangent X: slope = 4 along y = 2\nTangent Y: slope = 5 along x = 1\nTangent Plane Equation:\nz - 7 = 4(x - 1) + 5(y - 2)\nz = 4x + 5y - 7",
            "narration": "\"Let us return to the 3D surface to witness what these numbers truly represent. Along the cross-section where y = 2, the cyan tangent line touches the curve at (1, 2, 7). Its slope is exactly 4. That means for every step forward along the positive x-axis, the surface rises by 4 units. Along the cross-section where x = 1, the purple tangent line touches the curve. Its slope is 5, meaning a step forward along the positive y-axis yields an elevation increase of 5 units. Together, these two perpendicular tangent lines span a unique, flat plane: the tangent plane at (1, 2, 7). Its equation is z - 7 = 4(x - 1) + 5(y - 2), or z = 4x + 5y - 7. The partial derivatives provide the exact directional slopes that define this local linear approximation.\"",
            "transition": "Gentle zoom out into the final academic summary screen."
        },
        {
            "num": "SCENE 6",
            "title": "Summary, Credits & AI Disclosure",
            "time": "4:30 – 5:00 (30s)",
            "purpose": "Reinforce the three foundational takeaways, present formal academic citations, project details, and mandatory AI disclosures.",
            "visual": "Clean academic summary layout with three core conclusion callout boxes, followed by academic references (Stewart, Thomas, Strang), student submission placeholders, and AI tooling disclosure.",
            "math": "1. Directional Rate along Coordinate Axes\n2. Hold Complementary Variables Constant\n3. Slopes of 2D Traces → Tangent Plane\nz = 4x + 5y - 7",
            "narration": "\"To summarize our multivariable insights: First, partial derivatives measure the rate of change of a multivariable function with respect to one variable at a time. Second, to evaluate a partial derivative, all other independent variables are held strictly constant. Third, geometrically, partial derivatives represent the slopes of tangent lines along cross-sectional slices, which together construct the local tangent plane. Thank you for exploring the geometry of multivariable calculus.\"",
            "transition": "Fade to black with academic course credits."
        }
    ]

    for s in scenes:
        table_data = [
            [
                Paragraph(f"<b>{s['num']}: {s['title']}</b>", scene_heading_style),
                Paragraph(f"<b>Duration:</b> {s['time']}", label_style)
            ],
            [
                Paragraph("<b>Pedagogical Purpose:</b>", label_style),
                Paragraph(s["purpose"], body_style)
            ],
            [
                Paragraph("<b>Visual Design & 3D Geometry:</b>", label_style),
                Paragraph(s["visual"], body_style)
            ],
            [
                Paragraph("<b>Mathematical Content & Equations:</b>", label_style),
                Paragraph(s["math"].replace("\n", "<br/>"), math_style)
            ],
            [
                Paragraph("<b>Voice-over Narration Script:</b>", label_style),
                Paragraph(s["narration"], narration_style)
            ],
            [
                Paragraph("<b>Scene Transition:</b>", label_style),
                Paragraph(s["transition"], body_style)
            ]
        ]

        t = Table(table_data, colWidths=[130, 582])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (1, 0), colors.HexColor('#f1f5f9')),
            ('LINEBELOW', (0, 0), (1, 0), 1, colors.HexColor('#0284c7')),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))

        story.append(t)
        story.append(Spacer(1, 10))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Storyboard PDF created successfully at: {OUTPUT_PDF}")

if __name__ == "__main__":
    build_pdf()
