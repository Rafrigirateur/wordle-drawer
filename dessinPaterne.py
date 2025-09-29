from PIL import Image, ImageDraw, ImageFont
import os

def rectangle(output_path):
    image = Image.new("RGB", (1130, 1350), "#121212")
    draw = ImageDraw.Draw(image)
    # Draw a regular rectangle
    for k in range (6):
        for n in range (5):
            draw.rectangle((n*220+30, k*220+30, n*220+225, k*220+225), fill="#3a3a3c")
    
    image.save(output_path)

def drawPatern(paterne, nomPaterne):
    image = Image.new("RGB", (1130, 1350), "#121212")
    draw = ImageDraw.Draw(image)

    for k in range (6):
        for n in range (5):
            x0 = n*220 + 30
            y0 = k*220 + 30
            x1 = n*220 + 225
            y1 = k*220 + 225

            if (paterne[k][n] == "V"):
                draw.rectangle((x0, y0, x1, y1), fill="#538d4e")
            elif (paterne[k][n] == "J"):
                draw.rectangle((x0, y0, x1, y1), fill="#b59f3b")
            else :
                draw.rectangle((x0, y0, x1, y1), fill="#3a3a3c")
    
    output_dir = "images"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, nomPaterne + ".png")
    image.save(output_path)


def drawPaternWords(paterne, listeMots, nomPaterne):
    image = Image.new("RGB", (1130, 1350), "#121212")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("ClearSans-Bold.ttf", 130)

    for k in range(6):
        for n in range(5):
            x0 = n*220 + 30
            y0 = k*220 + 30
            x1 = n*220 + 225
            y1 = k*220 + 225

            if paterne[k][n] == "V":
                draw.rectangle((x0, y0, x1, y1), fill="#538d4e")
            elif paterne[k][n] == "J":
                draw.rectangle((x0, y0, x1, y1), fill="#b59f3b")
            else:
                draw.rectangle((x0, y0, x1, y1), fill="#3a3a3c")

            if listeMots[k] is not None:
                lettre = listeMots[k][n]
                center_x = (x0 + x1) // 2
                center_y = y0 + 45

                bbox = font.getbbox(lettre)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]

                text_x = center_x - text_width // 2
                text_y = center_y - text_height // 2

                draw.text((text_x, text_y), lettre, fill="white", font=font)

    output_dir = "images"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, nomPaterne + ".png")
    image.save(output_path)


    
if __name__ == "__main__":
    coeur = [
        ["G", "J", "G", "J", "G"],
        ["J", "G", "J", "G", "J"],
        ["J", "G", "G", "G", "J"],
        ["G", "J", "G", "J", "G"],
        ["G", "G", "J", "G", "G"],
        ["V", "V", "V", "V", "V"]
    ]

    listeMo = [
        "LINUM",
        "UMIAC",
        "INKER",
        "LINUM",
        "WAIST",
        "CURIO"
    ]

    rectangle("rounded_rectangle.jpg")
    #drawPatern(croix, "croix")
    drawPaternWords(coeur, listeMo, "coeur")