# SRT to PDF Converter

This project converts SRT subtitle files into PDF documents, ensuring that each subtitle file creates a new page with its name at the top.

## Requirements

- Python 3.x
- ReportLab library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/str_to_pdf.git
    cd str_to_pdf
    ```

2. Install the required dependencies:
    ```sh
    pip install reportlab
    ```

## Usage

1. Place your SRT files in the `subtitles` directory.

2. Run the script:
    ```sh
    python str_to_pdf.py
    ```

3. The output PDF will be created in the same directory with the name `output.pdf`.

## Example

Given an SRT file `example.srt` in the `subtitles` directory, the script will generate a PDF with the following structure:

- A new page with the title `example.srt` at the top.
- Subsequent pages containing the subtitles with their respective timestamps.

## License

This project is licensed under the MIT License.