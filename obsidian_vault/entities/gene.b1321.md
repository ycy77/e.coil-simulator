---
entity_id: "gene.b1321"
entity_type: "gene"
name: "ycjX"
source_database: "NCBI RefSeq"
source_id: "gene-b1321"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1321"
  - "ycjX"
---

# ycjX

`gene.b1321`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1321`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycjX (gene.b1321) is a gene entity. It encodes ycjX (protein.P76046). Encoded protein function: FUNCTION: Binds GTP and GDP. Has intrinsic GTPase activity. Does not hydrolyze ATP. May act as a transducer of stress responses. {ECO:0000250|UniProtKB:Q8EG04}. EcoCyc product frame: G6659-MONOMER. Genomic coordinates: 1384117-1385514. EcoCyc protein note: An electrophoretic mobility shift assay (EMSA) showed that PgrR is capable of interacting with the ycjX promoter region; in addition, the expression of ycjX was increased in a pgrR mutant strain . ycjX expression was increased during growth under nitrogen starvation conditions .

## Biological Role

Repressed by pgrR (protein.P77333). Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76046|protein.P76046]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=ycjX; function=+
- `represses` <-- [[protein.P77333|protein.P77333]] `RegulonDB` `S` - regulator=PgrR; target=ycjX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004433,ECOCYC:G6659,GeneID:945872`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1384117-1385514:+; feature_type=gene
