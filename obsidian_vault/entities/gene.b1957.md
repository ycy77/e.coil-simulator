---
entity_id: "gene.b1957"
entity_type: "gene"
name: "yodC"
source_database: "NCBI RefSeq"
source_id: "gene-b1957"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1957"
  - "yodC"
---

# yodC

`gene.b1957`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1957`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yodC (gene.b1957) is a gene entity. It encodes yodC (protein.P64517). Encoded protein function: Uncharacterized protein YodC EcoCyc product frame: G7050-MONOMER. Genomic coordinates: 2028188-2028370. EcoCyc protein note: This uncharacterized enzyme was found to interact with the PKII-MONOMER enzyme in glycolysis in a large assessment of protein-protein interactions (PPIs) .

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64517|protein.P64517]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006498,ECOCYC:G7050,GeneID:946466`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2028188-2028370:-; feature_type=gene
