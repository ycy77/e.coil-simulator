---
entity_id: "protein.P37751"
entity_type: "protein"
name: "wbbK"
source_database: "UniProt"
source_id: "P37751"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wbbK yefI b2032 JW2017"
---

# wbbK

`protein.P37751`

## Static

- Type: `protein`
- Source: `UniProt:P37751`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: May be a glycosyltransferase involved in the transfer of UDP-GalF and UDP-glucose. wbbK is predicted to encode a glycosyltransferase involved in the biosynthesis of O-antigen repeat units (see ). E. coli K-12 is phenotypically rough and does not express O-antigen due to mutations in the rfb region; E. coli K-12 MG1655 contains the rfb-50 mutation - an IS5 element which disrupts EG11986 wbbL encoding rhamnose transferase; an engineered strain of E. coli K-12 with all rfb genes intact synthesizes CPD0-2249 O16 antigen . For information on bacterial polysaccharide gene nomenclature see .

## Enriched Pathways

- `eco00542` O-Antigen repeat unit biosynthesis (KEGG)

## Annotation

FUNCTION: May be a glycosyltransferase involved in the transfer of UDP-GalF and UDP-glucose.

## Pathways

- `eco00542` O-Antigen repeat unit biosynthesis (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b2032|gene.b2032]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37751`
- `KEGG:ecj:JW2017;eco:b2032;ecoc:C3026_11450;`
- `GeneID:946555;`
- `GO:GO:0005886; GO:0009103; GO:0016757`

## Notes

Putative glycosyltransferase WbbK
