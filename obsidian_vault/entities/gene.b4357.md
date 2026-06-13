---
entity_id: "gene.b4357"
entity_type: "gene"
name: "lgoR"
source_database: "NCBI RefSeq"
source_id: "gene-b4357"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4357"
  - "lgoR"
---

# lgoR

`gene.b4357`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4357`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lgoR (gene.b4357) is a gene entity. It encodes lgoR (protein.P39399). Encoded protein function: FUNCTION: May be a positive transcriptional regulator for lgoD and/or lgoT. Is essential for growth on L-galactonate as the sole carbon source. {ECO:0000269|PubMed:17088549}. EcoCyc product frame: G7944-MONOMER. EcoCyc synonyms: yjjM. Genomic coordinates: 4594937-4595851. EcoCyc protein note: YjjM is a predicted transcriptional regulator that is essential for growth on L-galactonate as the sole carbon source . Expression of yjjM is upregulated during growth on L-galactonate compared to growth on L-lactate . UxuR appears to regulate yjjM expression .

## Biological Role

Repressed by exuR (protein.P0ACL2), uxuR (protein.P39161).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39399|protein.P39399]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACL2|protein.P0ACL2]] `RegulonDB` `S` - regulator=ExuR; target=lgoR; function=-
- `represses` <-- [[protein.P39161|protein.P39161]] `RegulonDB` `S` - regulator=UxuR; target=lgoR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014287,ECOCYC:G7944,GeneID:948881`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4594937-4595851:-; feature_type=gene
