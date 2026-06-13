---
entity_id: "protein.P0AC30"
entity_type: "protein"
name: "ftsX"
source_database: "UniProt"
source_id: "P0AC30"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:10048040, ECO:0000269|PubMed:14729705, ECO:0000269|PubMed:3323846}; Multi-pass membrane protein {ECO:0000269|PubMed:10048040, ECO:0000269|PubMed:14729705, ECO:0000269|PubMed:3323846}. Note=Localizes to the septal ring at the later stages of cell growth and remains there until division is complete. This localization is dependent on localization of FtsZ, FtsA and ZipA, but not on the downstream division proteins FtsK, FtsQ or FtsI."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ftsX ftsS b3462 JW3427"
---

# ftsX

`protein.P0AC30`

## Static

- Type: `protein`
- Source: `UniProt:P0AC30`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:10048040, ECO:0000269|PubMed:14729705, ECO:0000269|PubMed:3323846}; Multi-pass membrane protein {ECO:0000269|PubMed:10048040, ECO:0000269|PubMed:14729705, ECO:0000269|PubMed:3323846}. Note=Localizes to the septal ring at the later stages of cell growth and remains there until division is complete. This localization is dependent on localization of FtsZ, FtsA and ZipA, but not on the downstream division proteins FtsK, FtsQ or FtsI.

## Enriched Summary

FUNCTION: Part of the ABC transporter FtsEX involved in cellular division. Important for assembly or stability of the septal ring. Encoded in an operon consisting of genes ftsY, ftsE and ftsX. {ECO:0000269|PubMed:10048040, ECO:0000269|PubMed:14729705}. FtsE and FtsX localize to the cell division site; localization is dependent on FtsZ, FtsA and ZipA, but not FtsK, FtsQ, FtsL and FtsI . FtsEX is important for assembly or stability of the septal ring under low-salt growth conditions . FtsX contains 4 transmembrane region with the C and N terminus located in the cytoplasm; a large periplasmic loop is located between the first and second transmembrane region . FtsX-GFP localizes to the septal ring in a ftsEX null mutant . FtsS: FtsX: "filamentous temperature sensitive X" Review:

## Biological Role

Component of divisome protein complex FtsEX (complex.ecocyc.ABC-54-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter FtsEX involved in cellular division. Important for assembly or stability of the septal ring. Encoded in an operon consisting of genes ftsY, ftsE and ftsX. {ECO:0000269|PubMed:10048040, ECO:0000269|PubMed:14729705}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-54-CPLX|complex.ecocyc.ABC-54-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3462|gene.b3462]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC30`
- `KEGG:ecj:JW3427;eco:b3462;ecoc:C3026_18755;`
- `GeneID:93778529;947969;`
- `GO:GO:0000917; GO:0000935; GO:0005886; GO:0009254; GO:0009276; GO:0016020; GO:0032153; GO:0043093; GO:0051301; GO:0051781; GO:0098797; GO:1904949; GO:1990586`

## Notes

Cell division protein FtsX
