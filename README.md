# Instructions

This is a simple repo that attempts to use Indexify and run it using a `docker-compose.yml` file locally.

> You'll need to have a .env file which looks like this
> AWS_ACCESS_KEY_ID=
> AWS_SECRET_ACCESS_KEY=

## Running Locally

1. Make sure you have docker installed and run the command below. This will boot up an indexify server and a single chunk extractor.

> Note that this currently works because they have a shared `/tmp` folder.

```bash
make start
```

Once you've started the two docker containers, make sure that the UI is working as intended by going to `http://localhost:8900/ui`. You should have a tensorlake/chunk-extractor registered.

2. Next, create a virtual environment and make sure to install all of the dependencies inside the `requirements.txt` file

```bash
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

3. Once you've installed all of the dependencies, you can then create an ExtractionGraph by running the `create_graph.py` script. This will in turn create a new Extraction Graph in the UI called `summarize_and_chunk`

```bash
python3 ./scripts/create_graph.py
```

4. Now, run the `ingest.py` script so that we're able to load in 20 chunks into the ingestion pipeline. This should in turn create around 6 children per chunk that we ingest.

```bash
python3 ./scripts/create_graph.py
```

## Deploying to Fly.io

I've configured two `fly.toml` files which deploy two working versions of the applications. There are two main issues which I need to resolve before they're usable. **Make sure to also update `fly.toml` with the relevant IPs of the server and the extractor so that it works for you**.

1. Fly.io automatically deploys two different versions of my orchestrator and I need to manually stop one of them in order for me to consistently be able to run through any tests.

2. The Orchestrator and the Chunk Extractor currently don't share a common volume, causing some problems to occur. This needs to be fixed before we can succesfully deploy the central server and the chunk extractor together

I'd love to know how we can fix this - potentially configuring a S3 bucket to be used?
