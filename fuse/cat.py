import pypdf

from .utils import verify_file


def cat(file_names: str, output_filename: str):
    pdf_files = [verify_file(file_name) for file_name in file_names]
    pdf_merger = pypdf.PdfWriter()

    try:
        for pdf in pdf_files:
            pdf_merger.append(pdf)
        pdf_merger.write(output_filename)

    except BaseException as exc:
        print(f"Failed with {exc}")

    finally:
        pdf_merger.close()
