from PIL import Image, ImageDraw, ImageFont
import os

# Terminal dimensions
WIDTH = 900
LINE_HEIGHT = 23
PADDING_X = 20
PADDING_Y = 15
HEADER_HEIGHT = 35
FONT_SIZE = 14

# Color palette
BG_COLOR      = (13, 17, 23)       # #0D1117 - dark bg
HEADER_COLOR  = (22, 27, 34)       # #161B22 - header
BORDER_COLOR  = (0, 180, 216)      # #00B4D8 - electric blue border
CMD_COLOR     = (39, 201, 63)      # #27C93F - green commands
OUT_COLOR     = (0, 180, 216)      # #00B4D8 - blue output
SEP_COLOR     = (40, 50, 65)       # separator lines
STATUS_COLOR  = (255, 255, 255)    # white for status
PROMPT_COLOR  = (139, 148, 158)    # gray for prompt text
CURSOR_COLOR  = (0, 180, 216)      # cursor block

# All terminal lines from cm.md
lines = [
    ("> whoami",                                                                          "cmd"),
    ("Name: Naveen Akalanka  |  Role: Cloud & DevOps Engineer | Infrastructure Specialist", "out"),
    ("Focus: High-availability architecture and agent-driven automation",                  "out"),
    ("─" * 95,                                                                            "sep"),
    ("> system --info",                                                                   "cmd"),
    ("Education: BSc (Hons) Computer Networks  —  First Class Honours",                  "out"),
    ("Experience: System Administrator at JID Advertising Agency",                        "out"),
    ("─" * 95,                                                                            "sep"),
    ("> ls /skills/technical",                                                            "cmd"),
    ("Cloud: Azure, AWS  |  DevOps: Kubernetes, Docker, n8n, Linux",                     "out"),
    ("Networking / Virtualization: Proxmox Clusters (HA), LXC, VMs",                     "out"),
    ("─" * 95,                                                                            "sep"),
    ("> ls /skills/creative",                                                             "cmd"),
    ("Agentic Dev: AI-Agent Orchestration",                                               "out"),
    ("Design: UI/UX, Graphic Design, and 3D Modeling",                                   "out"),
    ("─" * 95,                                                                            "sep"),
    ("> echo $MISSION",                                                                   "cmd"),
    ('"To build & scale resilient cloud infrastructure through agent-driven problem solving."', "out"),
    ("─" * 95,                                                                            "sep"),
    ("[STATUS: ONLINE]",                                                                  "status"),
    ("$ status --check",                                                                  "cmd"),
    ("Checking systems... [DONE]",                                                        "out"),
    ("All systems operational.",                                                          "status"),
]

TOTAL_LINES = len(lines)
HEIGHT = HEADER_HEIGHT + PADDING_Y * 2 + TOTAL_LINES * LINE_HEIGHT + 10

def get_color(line_type):
    return {"cmd": CMD_COLOR, "out": OUT_COLOR, "sep": SEP_COLOR, "status": STATUS_COLOR}.get(line_type, OUT_COLOR)

# Load fonts
try:
    font      = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", FONT_SIZE)
    font_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", FONT_SIZE)
    print("Loaded Consolas font")
except:
    try:
        font      = ImageFont.truetype("C:/Windows/Fonts/cour.ttf", FONT_SIZE)
        font_bold = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", FONT_SIZE)
        print("Loaded Courier New font")
    except:
        font      = ImageFont.load_default()
        font_bold = font
        print("Using default font")

def draw_terminal(visible_count, show_cursor=True):
    img  = Image.new("RGBA", (WIDTH, HEIGHT), BG_COLOR + (255,))
    draw = ImageDraw.Draw(img)

    # Outer border
    draw.rounded_rectangle([0, 0, WIDTH-1, HEIGHT-1], radius=8, outline=BORDER_COLOR, width=1)

    # Header background
    draw.rounded_rectangle([0, 0, WIDTH-1, HEADER_HEIGHT], radius=8, fill=HEADER_COLOR)
    draw.rectangle([0, HEADER_HEIGHT-8, WIDTH, HEADER_HEIGHT], fill=HEADER_COLOR)
    draw.line([0, HEADER_HEIGHT, WIDTH, HEADER_HEIGHT], fill=BORDER_COLOR, width=1)

    # macOS traffic lights
    draw.ellipse([14, 11, 26, 23], fill=(255, 95, 86))
    draw.ellipse([34, 11, 46, 23], fill=(255, 189, 46))
    draw.ellipse([54, 11, 66, 23], fill=(39, 201, 63))

    # Header title
    draw.text((WIDTH // 2, HEADER_HEIGHT // 2), "terminal — naveen@infrastructure — 100x30",
              fill=PROMPT_COLOR, font=font, anchor="mm")

    # Draw visible lines
    y = HEADER_HEIGHT + PADDING_Y
    for i in range(visible_count):
        text, line_type = lines[i]
        color = get_color(line_type)
        f     = font_bold if line_type == "status" else font
        draw.text((PADDING_X, y), text, fill=color, font=f)
        y += LINE_HEIGHT

    # Cursor
    if show_cursor:
        cx = PADDING_X
        if visible_count > 0:
            last_text = lines[visible_count - 1][0]
            try:
                bbox = draw.textbbox((0, 0), last_text, font=font)
                cx = PADDING_X + bbox[2] + 3
            except:
                pass
        cursor_y = HEADER_HEIGHT + PADDING_Y + (visible_count - 1) * LINE_HEIGHT if visible_count > 0 else HEADER_HEIGHT + PADDING_Y
        draw.rectangle([cx, cursor_y + 2, cx + 8, cursor_y + LINE_HEIGHT - 3], fill=CURSOR_COLOR)

    return img.convert("P", palette=Image.ADAPTIVE, colors=128)

frames    = []
durations = []

# Frame 0 — empty terminal
frames.append(draw_terminal(0, show_cursor=False))
durations.append(600)

# Build up lines one by one
for i in range(1, TOTAL_LINES + 1):
    frame = draw_terminal(i, show_cursor=True)
    frames.append(frame)
    line_type = lines[i - 1][1]
    # Commands appear slower (typing feel), output faster
    delay = 700 if line_type == "cmd" else 350 if line_type == "sep" else 500
    durations.append(delay)

# Hold full terminal — cursor blink
for blink in range(8):
    frames.append(draw_terminal(TOTAL_LINES, show_cursor=(blink % 2 == 0)))
    durations.append(400)

# Long pause before loop
frames.append(draw_terminal(TOTAL_LINES, show_cursor=False))
durations.append(3000)

# Save
output_path = r"i:\CODE CAMP\Antigravity\GIT Readme\Assets\terminal.gif"
frames[0].save(
    output_path,
    save_all=True,
    append_images=frames[1:],
    optimize=True,
    duration=durations,
    loop=0,
)
print(f"\nGIF saved! Frames: {len(frames)}, Size: {os.path.getsize(output_path) // 1024}KB")
