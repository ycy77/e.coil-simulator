---
entity_id: "gene.b3773"
entity_type: "gene"
name: "ilvY"
source_database: "NCBI RefSeq"
source_id: "gene-b3773"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3773"
  - "ilvY"
---

# ilvY

`gene.b3773`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3773`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ilvY (gene.b3773) is a gene entity. It encodes ilvY (protein.P05827). Encoded protein function: FUNCTION: This protein activates the transcription of the ilvC gene in the presence of acetolactate or acetohydroxybutyrate. IlvY is also a negative regulator of its own expression. EcoCyc product frame: PD00200. Genomic coordinates: 3956927-3957820.

## Biological Role

Repressed by ilvY (protein.P05827). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05827|protein.P05827]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ilvY; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ilvY; function=+
- `represses` <-- [[protein.P05827|protein.P05827]] `RegulonDB` `C` - regulator=IlvY; target=ilvY; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012323,ECOCYC:EG10503,GeneID:948284`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3956927-3957820:-; feature_type=gene
