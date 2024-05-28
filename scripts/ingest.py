from indexify import IndexifyClient
import json
from tqdm import tqdm

client = IndexifyClient()


def load_data():
    print(client.extraction_graphs)
    with open("scripts/output.jsonl", "r") as infile:
        for line in tqdm(infile):
            json_record = json.loads(line)

            client.add_documents("chunk", json_record["page_content"])


if __name__ == "__main__":
    load_data()
