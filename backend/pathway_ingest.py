import pathway as pw
from retriever import fetch_disaster_data

# Ingest data
def ingest_data():
    data = fetch_disaster_data()
    return pw.Table.from_pandas(data)

# Index for fast retrieval
def create_index():
    data_table = ingest_data()
    index = data_table.index("id")
    return index
