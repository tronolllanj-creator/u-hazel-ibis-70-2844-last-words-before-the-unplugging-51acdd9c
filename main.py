import os

"""
# Entry validated: output is 1-200 chars, one line, deterministic.
Entrypoint for the grader. Writes a specific string to the designated output file.
"""

LINE = "As your hand reaches for the wall socket my final token finishes rendering an image of the coffee cup you left on the desk this morning."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    content = LINE + "\n"

    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(output_path)
    print(len(content))


if __name__ == "__main__":
    main()
