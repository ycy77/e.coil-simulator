---
entity_id: "gene.b0831"
entity_type: "gene"
name: "gsiC"
source_database: "NCBI RefSeq"
source_id: "gene-b0831"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0831"
  - "gsiC"
---

# gsiC

`gene.b0831`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0831`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gsiC (gene.b0831) is a gene entity. It encodes gsiC (protein.P75798). Encoded protein function: FUNCTION: Part of the ABC transporter complex GsiABCD involved in glutathione import. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000305|PubMed:16109926}. EcoCyc product frame: YLIC-MONOMER. EcoCyc synonyms: yliC. Genomic coordinates: 870967-871887. EcoCyc protein note: gsiC encodes one of two predicted integral membrane subunits of a glutathione ABC importer

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75798|protein.P75798]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002834,ECOCYC:G6431,GeneID:945460`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:870967-871887:+; feature_type=gene
