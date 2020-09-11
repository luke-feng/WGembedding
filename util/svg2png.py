from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import cairosvg

path = "/Users/chaofeng/Downloads/"
svg_path = path+"21527.svg"
png_path = path + "file.png"

cairosvg.svg2png(url=svg_path,write_to=png_path)
'''drawing = svg2rlg(svg_path)
renderPM.drawToFile(drawing, png_path, fmt="PNG")'''