---
entity_id: "protein.P0A9R7"
entity_type: "protein"
name: "ftsE"
source_database: "UniProt"
source_id: "P0A9R7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:10048040, ECO:0000269|PubMed:3323846}; Peripheral membrane protein {ECO:0000269|PubMed:10048040}; Cytoplasmic side {ECO:0000305}. Note=Associated with the membrane through an interaction with FtsX (PubMed:10048040). Localizes to the septal ring at the later stages of cell growth and remains there until division is complete (PubMed:14729705). This localization is dependent on localization of FtsZ, FtsA and ZipA, but not on the downstream division proteins FtsK, FtsQ or FtsI (PubMed:14729705). {ECO:0000269|PubMed:10048040, ECO:0000269|PubMed:14729705}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ftsE b3463 JW3428"
---

# ftsE

`protein.P0A9R7`

## Static

- Type: `protein`
- Source: `UniProt:P0A9R7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:10048040, ECO:0000269|PubMed:3323846}; Peripheral membrane protein {ECO:0000269|PubMed:10048040}; Cytoplasmic side {ECO:0000305}. Note=Associated with the membrane through an interaction with FtsX (PubMed:10048040). Localizes to the septal ring at the later stages of cell growth and remains there until division is complete (PubMed:14729705). This localization is dependent on localization of FtsZ, FtsA and ZipA, but not on the downstream division proteins FtsK, FtsQ or FtsI (PubMed:14729705). {ECO:0000269|PubMed:10048040, ECO:0000269|PubMed:14729705}.

## Enriched Summary

FUNCTION: Part of the ABC transporter FtsEX involved in cellular division. Important for assembly or stability of the septal ring. {ECO:0000269|PubMed:14729705}. FtsE dimerizes and associates with the inner membrane via interaction with FtsX, an integral membrane protein . FtsE and FtsX localize to the cell division site; localization is dependent on FtsZ, FtsA and ZipA, but not on FtsK, FtsQ, FtsL(W) nor FtsI; FtsEX is important for assembly or stability of the septal ring under low-salt growth conditions and under low osmolarity conditions . Depletion of FtsEX does not affect the abundance of FtsK, FtsQ, FtsI nor FtsN in the cytoplasmic membrane . The ATP-binding site mutant, FtsE(D162A) localizes to the septal ring and supports septal ring assembly but impairs septal ring constriction; FtsE may use ATP to promote septal ring constriction . FtsE requires FtsZ for localization to the septal ring . ftsE is non-essential when grown at high salt concentration (>0.5% NaCl); inactivation of ftsE (ftsE::kan) results in a filamented cellular morphology . ftsE and ftsX are located in an operon with ftsY - the latter encoding the SRP receptor . Overexpression of FtsEX does not interfere with SRP-mediated protein targeting; deletion of ftsE does not interfere with SRP-mediated protein targeting...

## Biological Role

Component of divisome protein complex FtsEX (complex.ecocyc.ABC-54-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter FtsEX involved in cellular division. Important for assembly or stability of the septal ring. {ECO:0000269|PubMed:14729705}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-54-CPLX|complex.ecocyc.ABC-54-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3463|gene.b3463]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9R7`
- `KEGG:ecj:JW3428;eco:b3463;ecoc:C3026_18760;`
- `GeneID:86862141;947968;`
- `GO:GO:0000917; GO:0000935; GO:0005524; GO:0005737; GO:0005886; GO:0009254; GO:0016887; GO:0019898; GO:0022857; GO:0032153; GO:0043093; GO:0046677; GO:0051301; GO:0051781; GO:0055085; GO:0098797; GO:1904949; GO:1990586`

## Notes

Cell division ATP-binding protein FtsE
