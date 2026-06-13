---
entity_id: "gene.b3301"
entity_type: "gene"
name: "rplO"
source_database: "NCBI RefSeq"
source_id: "gene-b3301"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3301"
  - "rplO"
---

# rplO

`gene.b3301`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3301`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplO (gene.b3301) is a gene entity. It encodes rplO (protein.P02413). Encoded protein function: FUNCTION: This protein binds the 5S rRNA. It is required for the late stages of subunit assembly, and is essential for 5S rRNA assembly onto the ribosome. {ECO:0000269|PubMed:3298242}. EcoCyc product frame: EG10876-MONOMER. Genomic coordinates: 3444105-3444539. EcoCyc protein note: The L15 protein is a component of the 50S subunit of the ribosome. L15 is a late assembly protein that appears to be required for 5S rRNA incorporation . L15 interacts with domain II of 23S rRNA in a partially assembled ribosomal particle . L15 appears to be dispensible for protein synthesis and cell growth , and ribosomes lacking L15 are translationally active . L15 is a component of the binding site for erythromycin on the ribosome . L15 has RNA chaperone-like activity in an in vitro trans splicing assay .

## Biological Role

Repressed by rpsH (protein.P0A7W7).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02413|protein.P02413]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7W7|protein.P0A7W7]] `RegulonDB` `S` - regulator=RpsH; target=rplO; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010819,ECOCYC:EG10876,GeneID:947798`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3444105-3444539:-; feature_type=gene
