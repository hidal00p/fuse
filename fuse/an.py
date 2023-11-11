import pypdf
from pypdf.annotations import Text

from .utils import verify_file


def an(file_name: str, annotations_meta: list[str], output_filename: str):
    pdf_file = verify_file(file_name)
    pdf_annotator = pypdf.PdfWriter()

    try:
        pdf_annotator.append(pdf_file)

        for anotation_meta in annotations_meta:
            page, title = anotation_meta.split(":")
            annotation = Text(
                text=title,
                rect=(0, 0, 0, 0),
            )
            pdf_annotator.add_annotation(page_number=int(page), annotation=annotation)

        pdf_annotator.write(output_filename)

    except BaseException as exc:
        print(f"Failed with {exc}")
    finally:
        pdf_annotator.close()
        pass
