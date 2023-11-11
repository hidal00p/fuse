import argparse

from .cat import cat
from .an import an


def config_app():
    parser = argparse.ArgumentParser(
        prog="fuse", description="A tiny tool to merge and annotate PDF files."
    )
    subparsers = parser.add_subparsers(required=True)

    # Subargs for annotations
    parser_an = subparsers.add_parser("an", help="Add annotations.")
    parser_an.add_argument(
        "--f",
        dest="file_name",
        required=True,
        type=str,
        help="File to which annotations will be added.",
    )
    parser_an.add_argument(
        "--a",
        dest="annotations_meta",
        required=True,
        nargs="+",
        type=str,
        help="Pairs of pages and annotations in the format `page:annotation`",
    )
    parser_an.add_argument(
        "--o",
        dest="output_filename",
        default="out.pdf",
        type=str,
        help="Output file name.",
    )
    parser_an.set_defaults(func=an)

    # Subargs for concatenation
    parser_cat = subparsers.add_parser("cat", help="Concatenate files.")
    parser_cat.add_argument(
        "--f",
        dest="file_names",
        required=True,
        nargs="+",
        type=str,
        help="File names to be merged into one single file.",
    )
    parser_cat.add_argument(
        "--o",
        dest="output_filename",
        default="out.pdf",
        type=str,
        help="Output file name.",
    )
    parser_cat.set_defaults(func=cat)

    return parser.parse_args()
