---
entity_id: "gene.b0832"
entity_type: "gene"
name: "gsiD"
source_database: "NCBI RefSeq"
source_id: "gene-b0832"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0832"
  - "gsiD"
---

# gsiD

`gene.b0832`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0832`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gsiD (gene.b0832) is a gene entity. It encodes gsiD (protein.P75799). Encoded protein function: FUNCTION: Part of the ABC transporter complex GsiABCD involved in glutathione import. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000305|PubMed:16109926}. EcoCyc product frame: YLID-MONOMER. EcoCyc synonyms: yliD. Genomic coordinates: 871890-872801. EcoCyc protein note: gsiD encodes one of two predicted integral membrane subunits of a glutathione ABC importer

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75799|protein.P75799]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002836,ECOCYC:G6432,GeneID:945461`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:871890-872801:+; feature_type=gene
