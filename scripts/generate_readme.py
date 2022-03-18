from pathlib import Path


def generate_img_tag(file):
    return f'<img src="icons/{file.name}" alt="{file.stem}" width="50">'


if __name__ == "__main__":
    imgs = sorted(Path("./icons").glob("*.png"))
    img_tags = [generate_img_tag(x) for x in imgs]

    with open("README.md", "wt", encoding="UTF-8") as f:
        f.write("# Schmökerei Icons\n\n")
        f.write(" ".join(img_tags))