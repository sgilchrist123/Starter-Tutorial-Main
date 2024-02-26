import nest_asyncio
nest_asyncio.apply()

from llama_parse import LlamaParse

parser = LlamaParse(
    api_key="llx-XXXXXXXX",  # can also be set in your env as LLAMA_CLOUD_API_KEY
    result_type="markdown",  # "markdown" and "text" are available
    num_workers=4, # if multiple files passed, split in `num_workers` API calls
    verbose=True
)

# sync
documents = parser.load_data("./my_file.pdf")

print(documents[0].text[6000:7000])