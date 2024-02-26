import nest_asyncio
import os.path
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

nest_asyncio.apply()

from llama_parse import LlamaParse

parser = LlamaParse(
    # api_key="llx-XXX",  # can also be set in your env as LLAMA_CLOUD_API_KEY
    result_type="markdown",  # "markdown" and "text" are available
    num_workers=4, # if multiple files passed, split in `num_workers` API calls
    verbose=True
)

documents = parser.load_data("data/2022AnnualReport.pdf")

# check if storage already exists
PERSIST_DIR = "./storageForLlamaParse"
if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index

    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# print(documents[0].text[6000:7000])

#query the index
query_engine = index.as_query_engine()
response = query_engine.query("What are the values in the first column in the second table in the document?")
print(response)