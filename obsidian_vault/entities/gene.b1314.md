---
entity_id: "gene.b1314"
entity_type: "gene"
name: "ycjR"
source_database: "NCBI RefSeq"
source_id: "gene-b1314"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1314"
  - "ycjR"
---

# ycjR

`gene.b1314`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1314`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycjR (gene.b1314) is a gene entity. It encodes ycjR (protein.P76044). Encoded protein function: FUNCTION: Catalyzes the epimerization at C4 of 3-dehydro-D-gulosides leading to 3-dehydro-D-glucosides. Probably functions in a metabolic pathway that transforms D-gulosides to D-glucosides. Can use methyl alpha-3-dehydro-D-glucoside and methyl beta-3-dehydro-D-glucoside as substrates in vitro. However, the actual specific physiological substrates for this metabolic pathway are unknown. Cannot act on D-psicose, D-fructose, D-tagatose, D-sorbose, L-xylulose, or L-ribulose. {ECO:0000269|PubMed:30742415}. EcoCyc product frame: G6652-MONOMER. EcoCyc synonyms: dte. Genomic coordinates: 1376034-1376822.

## Biological Role

Repressed by ycjW (protein.P77615).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76044|protein.P76044]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77615|protein.P77615]] `RegulonDB` `S` - regulator=YcjW; target=ycjR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004414,ECOCYC:G6652,GeneID:947427`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1376034-1376822:+; feature_type=gene
