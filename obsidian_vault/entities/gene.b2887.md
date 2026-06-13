---
entity_id: "gene.b2887"
entity_type: "gene"
name: "ygfT"
source_database: "NCBI RefSeq"
source_id: "gene-b2887"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2887"
  - "ygfT"
---

# ygfT

`gene.b2887`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2887`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygfT (gene.b2887) is a gene entity. It encodes uacF (protein.Q46820). Encoded protein function: FUNCTION: Involved in formate-dependent uric acid degradation under microaerobic and anaerobic conditions. May reduce the enzymes necessary for uric acid degradation. {ECO:0000269|PubMed:30885932}. EcoCyc product frame: G7506-MONOMER. Genomic coordinates: 3029012-3030931. EcoCyc protein note: Under anaerobic and microaerobic conditions, E. coli is able to utilize urate as its sole source of nitrogen. YgfT or AegA play a role in the formate-dependent catabolism of urate. Like AegA, YgfT contains an N-terminal Fe-S cluster domain and C-terminal pyridine nucleotide-disulfide oxidoreductase domain . An aegA ygfT double mutant lacks urate degradation activity . Expression of ygfT is induced under anaerobic and microaerobic conditions; expression is also increased in the presence of dimethyl sulfoxide, trimethylamine N-oxide, fumarate, hypoxanthine, xanthine, or urate and reduced in the presence of nitrate or nitrite under anaerobic conditions .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46820|protein.Q46820]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009473,ECOCYC:G7506,GeneID:949018`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3029012-3030931:-; feature_type=gene
