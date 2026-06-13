---
entity_id: "gene.b0050"
entity_type: "gene"
name: "apaG"
source_database: "NCBI RefSeq"
source_id: "gene-b0050"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0050"
  - "apaG"
---

# apaG

`gene.b0050`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0050`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

apaG (gene.b0050) is a gene entity. It encodes apaG (protein.P62672). Encoded protein function: Protein ApaG EcoCyc product frame: EG10047-MONOMER. Genomic coordinates: 51229-51606. EcoCyc protein note: An apaG frameshift mutation affects production of ApaH (diadenosine tetraphosphatase), indicating translational coregulation . Mutations have been generated . apaG belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 . Regulation has been described .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P62672|protein.P62672]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000169,ECOCYC:EG10047,GeneID:944772`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:51229-51606:-; feature_type=gene
