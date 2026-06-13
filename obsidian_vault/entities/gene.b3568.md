---
entity_id: "gene.b3568"
entity_type: "gene"
name: "xylH"
source_database: "NCBI RefSeq"
source_id: "gene-b3568"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3568"
  - "xylH"
---

# xylH

`gene.b3568`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3568`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xylH (gene.b3568) is a gene entity. It encodes xylH (protein.P0AGI4). Encoded protein function: FUNCTION: Part of the binding-protein-dependent transport system for D-xylose. Probably responsible for the translocation of the substrate across the membrane. EcoCyc product frame: XYLH-MONOMER. Genomic coordinates: 3733720-3734901. EcoCyc protein note: XylH is the predicted integral membrane subunit of a high-affinity, ATP dependent xylose uptake system .

## Biological Role

Activated by xylR (protein.P0ACI3).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGI4|protein.P0AGI4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACI3|protein.P0ACI3]] `RegulonDB` `S` - regulator=XylR; target=xylH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011650,ECOCYC:EG12276,GeneID:948083`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3733720-3734901:+; feature_type=gene
