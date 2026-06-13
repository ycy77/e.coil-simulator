---
entity_id: "gene.b4222"
entity_type: "gene"
name: "ytfP"
source_database: "NCBI RefSeq"
source_id: "gene-b4222"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4222"
  - "ytfP"
---

# ytfP

`gene.b4222`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4222`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ytfP (gene.b4222) is a gene entity. It encodes ytfP (protein.P0AE48). Encoded protein function: FUNCTION: May play a role in antibiotic biosynthesis. {ECO:0000305}. EcoCyc product frame: G7876-MONOMER. Genomic coordinates: 4447894-4448235. EcoCyc protein note: Overexpression of ytfP is toxic to the cell (see ASKA clone resource information at GenoBase) . YtfP is a member of the UPF0131 protein domain family. A solution structure is available .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE48|protein.P0AE48]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ytfP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013814,ECOCYC:G7876,GeneID:948741`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4447894-4448235:+; feature_type=gene
