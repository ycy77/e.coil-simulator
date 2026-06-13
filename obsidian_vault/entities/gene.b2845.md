---
entity_id: "gene.b2845"
entity_type: "gene"
name: "yqeG"
source_database: "NCBI RefSeq"
source_id: "gene-b2845"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2845"
  - "yqeG"
---

# yqeG

`gene.b2845`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2845`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yqeG (gene.b2845) is a gene entity. It encodes yqeG (protein.P63340). Encoded protein function: Inner membrane transport protein YqeG EcoCyc product frame: B2845-MONOMER. Genomic coordinates: 2985847-2987076. EcoCyc protein note: The YqeG protein is an uncharacterised member of the Hydroxy/Aromatic Amino Acid Permease (HAAAP) Family of transporters . yqeG is induced by E. coli stationary-phase supernatant perhaps due to quorum-sensing signals . Mutation of the three PhoB binding sites in the yqeF-yqeG intergenic region results in increased expression of yqeG .

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P63340|protein.P63340]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009345,ECOCYC:G7465,GeneID:945028`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2985847-2987076:+; feature_type=gene
