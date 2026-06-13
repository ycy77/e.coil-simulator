---
entity_id: "gene.b2427"
entity_type: "gene"
name: "murR"
source_database: "NCBI RefSeq"
source_id: "gene-b2427"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2427"
  - "murR"
---

# murR

`gene.b2427`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2427`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

murR (gene.b2427) is a gene entity. It encodes murR (protein.P77245). Encoded protein function: FUNCTION: Represses the expression of the murPQ operon involved in the uptake and degradation of N-acetylmuramic acid (MurNAc). Binds to two adjacent inverted repeats within the operator region. MurNAc 6-phosphate, the substrate of MurQ, is the specific inducer that weakens binding of MurR to the operator. Also represses its own transcription. {ECO:0000269|PubMed:18723630}. EcoCyc product frame: G7262-MONOMER. EcoCyc synonyms: yfeT. Genomic coordinates: 2544752-2545609.

## Biological Role

Repressed by murR (protein.P77245). Activated by rpoD (protein.P00579), rpoS (protein.P13445), murR (protein.P77245).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77245|protein.P77245]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=murR; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=murR; function=+
- `activates` <-- [[protein.P77245|protein.P77245]] `RegulonDB` `S` - regulator=MurR; target=murR; function=-+
- `represses` <-- [[protein.P77245|protein.P77245]] `RegulonDB` `S` - regulator=MurR; target=murR; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0008000,ECOCYC:G7262,GeneID:946568`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2544752-2545609:-; feature_type=gene
