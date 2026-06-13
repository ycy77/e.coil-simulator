---
entity_id: "gene.b4230"
entity_type: "gene"
name: "ytfT"
source_database: "NCBI RefSeq"
source_id: "gene-b4230"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4230"
  - "ytfT"
---

# ytfT

`gene.b4230`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4230`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ytfT (gene.b4230) is a gene entity. It encodes ytfT (protein.P39328). Encoded protein function: FUNCTION: Part of the ABC transporter complex YtfQRT-YjfF involved in galactofuranose transport (Probable). Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000305, ECO:0000305|PubMed:19744923}. EcoCyc product frame: YTFT-MONOMER. Genomic coordinates: 4452571-4453596. EcoCyc protein note: Sequence analysis suggests that YtfT is the integral membrane protein of an ATP-binding cassette (ABC) transporter .

## Biological Role

Repressed by araC (protein.P0A9E0).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39328|protein.P39328]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `S` - regulator=AraC; target=ytfT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013838,ECOCYC:EG12520,GeneID:948743`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4452571-4453596:+; feature_type=gene
