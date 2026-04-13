import os
import fitz  # PyMuPDF
import subprocess
from PIL import Image
import io

def find_ghostscript():
    """
    Automatically find Ghostscript executable.
    1. Check GHOSTSCRIPT_HOME environment variable.
    2. Check default Windows installation path.
    3. Fallback to 'gs' (if it's in PATH).
    """
    env_path = os.environ.get("GHOSTSCRIPT_HOME")
    if env_path:
        exe_path = os.path.join(env_path, "bin", "gswin64c.exe")
        if os.path.exists(exe_path):
            return exe_path

    default_path = r"C:\Program Files\gs"
    if os.path.exists(default_path):
        for folder in os.listdir(default_path):
            candidate = os.path.join(default_path, folder, "bin", "gswin64c.exe")
            if os.path.exists(candidate):
                return candidate

    return "gs"  # fallback if in PATH


def is_scanned_pdf(pdf_path, threshold=0.8):
    """Detect if PDF is mostly images (>80% of pages)."""
    doc = fitz.open(pdf_path)
    image_pages = sum(1 for p in doc if p.get_images(full=True))
    ratio = image_pages / len(doc)
    doc.close()
    return ratio >= threshold


def compress_with_pymupdf(input_path, output_path, image_quality=75, image_scale=0.85):
    """Compress text/image-based PDFs using PyMuPDF."""
    print("📘 Using PyMuPDF compression (text-based PDF)...")
    doc = fitz.open(input_path)
    doc.set_metadata({})
    original_size = os.path.getsize(input_path)

    for page_index in range(len(doc)):
        page = doc[page_index]
        image_list = page.get_images(full=True)
        if not image_list:
            continue

        for img in image_list:
            xref = img[0]
            base_image = doc.extract_image(xref)
            ext = base_image["ext"].lower()
            if ext in ["jpg", "jpeg", "jbig2", "ccitt"]:
                continue  # already efficiently compressed

            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            new_size = (int(image.width * image_scale), int(image.height * image_scale))
            image = image.resize(new_size, Image.LANCZOS)

            buffer = io.BytesIO()
            image.save(buffer, format="JPEG", quality=image_quality)
            rect = page.get_image_bbox(img)
            page.insert_image(rect, stream=buffer.getvalue())

    doc.save(output_path, garbage=4, deflate=True, clean=True)
    doc.close()

    compressed_size = os.path.getsize(output_path)
    print(f"✅ PyMuPDF compression complete.")
    print(f"Original: {original_size/1024:.2f} KB | Compressed: {compressed_size/1024:.2f} KB | Reduction: {(1 - compressed_size/original_size)*100:.2f}%")


def compress_with_ghostscript(input_path, output_path, quality="/ebook"):
    """Compress scanned/image PDFs using Ghostscript."""
    gs_exe = find_ghostscript()
    print(f"🖨️ Using Ghostscript compression (scanned PDF)...")
    print(f"🔎 Ghostscript path: {gs_exe}")

    gs_command = [
        gs_exe, "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS={quality}",
        "-dNOPAUSE", "-dQUIET", "-dBATCH",
        f"-sOutputFile={output_path}",
        input_path
    ]

    try:
        subprocess.run(gs_command, check=True)
        original_size = os.path.getsize(input_path)
        compressed_size = os.path.getsize(output_path)
        print(f"✅ Ghostscript compression complete.")
        print(f"Original: {original_size/1024:.2f} KB | Compressed: {compressed_size/1024:.2f} KB | Reduction: {(1 - compressed_size/original_size)*100:.2f}%")
    except Exception as e:
        print(f"❌ Ghostscript compression failed: {e}")


def compress_pdf_auto(input_path, output_path):
    """Automatically choose compression method."""
    print("🔍 Checking PDF type...")
    if is_scanned_pdf(input_path):
        print("Detected: 📄 Scanned or image-heavy PDF")
        compress_with_ghostscript(input_path, output_path, quality="/ebook")
    else:
        print("Detected: 📝 Text-based PDF")
        compress_with_pymupdf(input_path, output_path)


# --- Your file paths ---
input_pdf = r"C:\Users\Lenovo\OneDrive\Backup_23102024\d_drive\OFFICIAL\Aufhebungsvertrag\Aufhebungsvertrag_signed.pdf"
output_pdf = r"C:\Users\Lenovo\OneDrive\Backup_23102024\d_drive\OFFICIAL\Aufhebungsvertrag\compressed.pdf"

compress_pdf_auto(input_pdf, output_pdf)
