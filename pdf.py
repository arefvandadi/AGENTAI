import os
from llama_index.core.readers import SimpleDirectoryReader
from llama_index.readers.file import PDFReader
from pathlib import Path

pdf_file_path = os.path.join('data', 'Canada.pdf')
# Option 1
# reader = SimpleDirectoryReader(input_files=[pdf_file_path])
# document1 = reader.load_data()
# # print(len(document))

# Option 2
loader = PDFReader()
document2 = loader.load_data(file=Path(pdf_file_path))
# print(len(document))
