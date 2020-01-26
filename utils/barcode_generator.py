"""Barcode generator."""
import code128


def generate(data):
    """Generates barcode from parsed data."""
    return code128.image(data).save("utils/temp/barcode.png")
