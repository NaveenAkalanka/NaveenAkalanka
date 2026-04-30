from PIL import Image, ImageDraw, ImageFont
import os

WIDTH         = 460
LINE_HEIGHT   = 22
PADDING_X     = 16
PADDING_Y     = 12
HEADER_HEIGHT = 32
FONT_SIZE     = 13

BG_COLOR     = (13,  17,  23)
HEADER_COLOR = (22,  27,  34)
BORDER_COLOR = (0,  180, 216)
CMD_COLOR    = (39, 201,  63)
OUT_COLOR    = (0,  180, 216)
SEP_COLOR    = (40,  50,  65)
STATUS_COLOR = (255, 255, 255)
PROMPT_COLOR = (139, 148, 158)
CURSOR_COLOR = (0,  180, 216)

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
        font = font_bold = ImageFont.load_default()
        print("Using default font")

SEP = ("─" * 58, "sep")

PROJECTS = [
    (
        "scaneye_terminal.gif",
        "ScanEye — naveen@projects",
        [
            ("> cat project.info",                                    "cmd"),
            ("Name    : ScanEye",                                     "out"),
            ("Type    : Advanced Network Scanning & Monitoring Tool", "out"),
            SEP,
            ("> describe --detail",                                   "cmd"),
            ("Web browsers can't touch your local network.",          "out"),
            ("So I built a bridge: ScanEye runs as a privileged",     "out"),
            ("Docker container (network_mode: host), uses Nmap for",  "out"),
            ("deep device discovery, streams live results to a",       "out"),
            ("React dashboard via WebSockets.",                        "out"),
            ("Rate-limited | Helmet-hardened | Injection-resistant.", "out"),
            SEP,
            ("> ls /stack",                                           "cmd"),
            ("Docker  Node.js  React  Nmap  WebSockets  Express",     "status"),
        ]
    ),
    (
        "nuxview_terminal.gif",
        "NuxView — naveen@projects",
        [
            ("> cat project.info",                                    "cmd"),
            ("Name    : NuxView",                                     "out"),
            ("Type    : Interactive Linux Directory Visualization",   "out"),
            SEP,
            ("> describe --detail",                                   "cmd"),
            ("ls -la shows you names. NuxView shows you meaning.",    "out"),
            ("Scans local filesystems and renders an interactive,",   "out"),
            ("node-based web UI where you can explore directory",      "out"),
            ("roles — not just paths. Built for learning",            "out"),
            ("environments and complex lab setups alike.",            "out"),
            SEP,
            ("> ls /stack",                                           "cmd"),
            ("TypeScript  Node.js  React  Linux  File System API",    "status"),
        ]
    ),
    (
        "clustereye_terminal.gif",
        "ClusterEye — naveen@projects",
        [
            ("> cat project.info",                                    "cmd"),
            ("Name    : ClusterEye",                                  "out"),
            ("Type    : Cluster Monitoring & Management Dashboard",   "out"),
            SEP,
            ("> describe --detail",                                   "cmd"),
            ("Real-time monitoring for cluster environments.",        "out"),
            ("The architectural predecessor to ScanEye — and the",   "out"),
            ("project that exposed the browser sandboxing problem",   "out"),
            ("I later solved with a containerized split-arch",        "out"),
            ("approach.",                                             "out"),
            SEP,
            ("> ls /stack",                                           "cmd"),
            ("JavaScript  Node.js  Docker",                           "status"),
        ]
    ),
    (
        "posefit_terminal.gif",
        "PoseFit V2 — naveen@projects",
        [
            ("> cat project.info",                                    "cmd"),
            ("Name    : PoseFit V2",                                  "out"),
            ("Type    : Body-Orientation-Invariant 3D Joint-Angle",  "out"),
            SEP,
            ("> describe --detail",                                   "cmd"),
            ("Biomechanical angle estimation that stays accurate",    "out"),
            ("regardless of camera viewpoint, distance, or body",     "out"),
            ("rotation. Goes well beyond standard pose detection",    "out"),
            ("— maintains constant angle values even as the user",    "out"),
            ("moves freely.",                                         "out"),
            SEP,
            ("> ls /stack",                                           "cmd"),
            ("JavaScript  Machine Learning  Computer Vision",         "status"),
        ]
    ),
    (
        "scrollsync_terminal.gif",
        "ScrollSync — naveen@projects",
        [
            ("> cat project.info",                                    "cmd"),
            ("Name    : ScrollSync",                                  "out"),
            ("Type    : Hands-Free Chrome Browsing Extension",       "out"),
            SEP,
            ("> describe --detail",                                   "cmd"),
            ("Auto-scroll, smart click navigation, and gamepad",      "out"),
            ("controller support for Chrome. Built to solve a real",  "out"),
            ("accessibility and workflow convenience problem --",      "out"),
            ("because sometimes your hands should be free.",          "out"),
            SEP,
            ("> ls /stack",                                           "cmd"),
            ("JavaScript  Chrome Extension API",                      "status"),
        ]
    ),
    (
        "serenityecho_terminal.gif",
        "SerenityEcho — naveen@projects",
        [
            ("> cat project.info",                                    "cmd"),
            ("Name    : SerenityEcho",                                "out"),
            ("Type    : Privacy-First Offline Ambient Sound Mixer",  "out"),
            SEP,
            ("> describe --detail",                                   "cmd"),
            ("No signups. No paywalls. No cloud.",                    "out"),
            ("A fully offline-capable ambient sound mixer --",        "out"),
            ("because not every tool needs to phone home.",           "out"),
            ("Works entirely in the browser; no data ever leaves",    "out"),
            ("your device.",                                          "out"),
            SEP,
            ("> ls /stack",                                           "cmd"),
            ("TypeScript  PWA  Web Audio API",                        "status"),
        ]
    ),
]

def get_color(lt):
    return {"cmd": CMD_COLOR, "out": OUT_COLOR, "sep": SEP_COLOR, "status": STATUS_COLOR}.get(lt, OUT_COLOR)

def draw_frame(lines_data, visible_count, header_title, height, show_cursor=True):
    """Returns a plain RGB Image — no palette conversion yet."""
    img  = Image.new("RGB", (WIDTH, height), BG_COLOR)
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([0, 0, WIDTH-1, height-1], radius=8, outline=BORDER_COLOR, width=1)
    draw.rounded_rectangle([0, 0, WIDTH-1, HEADER_HEIGHT], radius=8, fill=HEADER_COLOR)
    draw.rectangle([0, HEADER_HEIGHT-8, WIDTH, HEADER_HEIGHT], fill=HEADER_COLOR)
    draw.line([0, HEADER_HEIGHT, WIDTH, HEADER_HEIGHT], fill=BORDER_COLOR, width=1)

    draw.ellipse([12, 10, 22, 20], fill=(255, 95,  86))
    draw.ellipse([29, 10, 39, 20], fill=(255, 189, 46))
    draw.ellipse([46, 10, 56, 20], fill=(39,  201, 63))

    draw.text((WIDTH // 2, HEADER_HEIGHT // 2), header_title,
              fill=PROMPT_COLOR, font=font, anchor="mm")

    y = HEADER_HEIGHT + PADDING_Y
    for i in range(visible_count):
        text, lt = lines_data[i]
        f = font_bold if lt == "status" else font
        draw.text((PADDING_X, y), text, fill=get_color(lt), font=f)
        y += LINE_HEIGHT

    if show_cursor and visible_count > 0:
        last_text = lines_data[visible_count - 1][0]
        try:
            bbox = draw.textbbox((0, 0), last_text, font=font)
            cx = PADDING_X + bbox[2] + 3
        except:
            cx = PADDING_X
        cy = HEADER_HEIGHT + PADDING_Y + (visible_count - 1) * LINE_HEIGHT
        draw.rectangle([cx, cy + 2, cx + 7, cy + LINE_HEIGHT - 3], fill=CURSOR_COLOR)

    return img

output_dir = r"i:\CODE CAMP\Antigravity\GIT Readme\Assets"
os.makedirs(output_dir, exist_ok=True)

for filename, header_title, lines_data in PROJECTS:
    total  = len(lines_data)
    height = HEADER_HEIGHT + PADDING_Y * 2 + total * LINE_HEIGHT + 10

    rgb_frames = []
    durations  = []

    rgb_frames.append(draw_frame(lines_data, 0, header_title, height, show_cursor=False))
    durations.append(500)

    for i in range(1, total + 1):
        rgb_frames.append(draw_frame(lines_data, i, header_title, height, show_cursor=True))
        lt = lines_data[i - 1][1]
        durations.append(700 if lt == "cmd" else 300 if lt == "sep" else 450)

    for blink in range(6):
        rgb_frames.append(draw_frame(lines_data, total, header_title, height, show_cursor=(blink % 2 == 0)))
        durations.append(400)

    rgb_frames.append(draw_frame(lines_data, total, header_title, height, show_cursor=False))
    durations.append(3000)

    # Build ONE shared palette from the fully-populated frame, quantize all frames to it
    palette_source = rgb_frames[-2].quantize(colors=256, dither=0)
    p_frames = [f.quantize(palette=palette_source, dither=0) for f in rgb_frames]

    out_path = os.path.join(output_dir, filename)
    p_frames[0].save(
        out_path,
        save_all=True,
        append_images=p_frames[1:],
        optimize=False,
        duration=durations,
        loop=0,
    )
    print(f"Generated: {filename}  ({os.path.getsize(out_path) // 1024} KB, {len(p_frames)} frames)")

print("\nAll project GIFs generated!")
