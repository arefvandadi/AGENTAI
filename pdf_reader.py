import os
from llama_index.core import SimpleDirectoryReader, load_index_from_storage, VectorStoreIndex, StorageContext, Settings
from llama_index.readers.file import PDFReader
from pathlib import Path

# API Key
import os
import openai
openai.api_key = os.getenv('OPENAI_API_KEY_1')

pdf_file_path = os.path.join('data', 'Canada.pdf')
# Option 1
# reader = SimpleDirectoryReader(input_files=[pdf_file_path])
# document = reader.load_data()

# Option 2
loader = PDFReader()
Canada_pdf_doc = loader.load_data(file=Path(pdf_file_path))

def get_index(data, index_folder_name):
    index = None
    if not os.path.exists(index_folder_name):
        print("building index from imported data and saving in", index_folder_name, 'folder')
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_folder_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_folder_name)
        )

    return index

canada_index = get_index(Canada_pdf_doc, "canada")
canada_engine = canada_index.as_query_engine()