# Data pipeline scripts

These scripts build the first public-data version of the E.coil knowledge graph.

## Current public sources

```bash
python3 scripts/fetch_uniprot.py
python3 scripts/fetch_kegg.py
python3 scripts/fetch_kegg_reactions.py
python3 scripts/fetch_ncbi_refseq.py
python3 scripts/build_ncbi_entities.py
python3 scripts/build_regulondb_edges.py
python3 scripts/build_entities.py
python3 scripts/build_edges.py
python3 scripts/build_pathways.py
```

Outputs:

```text
data/raw/uniprot/
data/raw/kegg/
data/raw/kegg/reaction_details/
data/raw/ncbi_refseq/
data/normalized/ncbi_entities.csv
data/normalized/entities.csv
data/normalized/edges.csv
data/normalized/pathways.csv
```

EcoCyc and RegulonDB are intentionally not downloaded here yet. Put licensed flat files under:
EcoCyc is now licensed for this project, but its confidential URL and credentials
must stay outside the repository. Export them in your shell before downloading:

```bash
export BIOCYC_FLATFILES_URL="..."
export BIOCYC_FLATFILES_USER="..."
export BIOCYC_FLATFILES_PASSWORD="..."
python3 scripts/fetch_ecocyc_flatfiles.py --dry-run
python3 scripts/fetch_ecocyc_flatfiles.py
```

The script writes files to:

```text
data/raw/ecocyc/
```

Do not paste the real URL, username, or password into tracked files.

RegulonDB files can remain under:

```text
data/raw/regulondb/
```

Then add parsers for EcoCyc complexes, transport reactions, transcription
units, curated reactions, and response-pattern annotations.
