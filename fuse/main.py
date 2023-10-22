import argparse
import pathlib
import pypdf

def parse_raw_file_names(file_names: str) -> list[pathlib.Path]:
    ext = ".pdf"
    files = []
    for file_name in file_names:
        if ext not in file_name:
            raise RuntimeError(f"Provided file {file_name} does not have PDF extension explicitely specified.")
        file = pathlib.Path(file_name)

        if not file.exists():
            raise RuntimeError(f"Provided file {file} does not exist.")

        files.append(file)
    return files

def main(file_names: str, output_file_name: str):
    pdf_files = parse_raw_file_names(file_names)
    pdf_merger = pypdf.PdfWriter()

    try:
        for pdf in pdf_files:
            pdf_merger.append(pdf)
        pdf_merger.write(output_file_name)

    except BaseException as exc:
        print(f"Failed with {exc}")

    finally:
        pdf_merger.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Merge pdf files with ease."
    )
    parser.add_argument(
        "--f",
        required=True,
        nargs="+",
        type=str,
        help="File names to be merged into one single file.",
    )
    parser.add_argument(
        "--o",
        default="out.pdf",
        type=str,
        help="Output file name.",
    )

    args = parser.parse_args()
    file_names, output_file_name = args.f, args.o

    main(file_names, output_file_name)
