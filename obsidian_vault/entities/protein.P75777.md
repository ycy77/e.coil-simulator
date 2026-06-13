---
entity_id: "protein.P75777"
entity_type: "protein"
name: "ybhG"
source_database: "UniProt"
source_id: "P75777"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_01304, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybhG b0795 JW0779"
---

# ybhG

`protein.P75777`

## Static

- Type: `protein`
- Source: `UniProt:P75777`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_01304, ECO:0000305}.

## Enriched Summary

FUNCTION: Could be involved in the sensitivity control to chloramphenicol. {ECO:0000305|PubMed:27112147}. ΔybhG mutants show reduced growth in the presence of chloramphenicol and the third generation cephalosporin - cefoperazone . YbhG belongs to the HlyD_D23 family of proteins - defined in the Pfam database as 'the combined domains 2 and 3 of the membrane-fusion proteins CusB and HlyD, which forms a barrel-sandwich'. Transcription of the ybhG-containing operon (cecR-ybhGFSR) is negatively regulated by EG12406-MONOMER "CecR" . The mechanism by which YbhG contributes to drug resistance is not clear. Membrane fusion proteins typically function with RND family proteins plus an outer membrane factor to mediate export. The ybhF, ybhS and ybhR genes located in this operon encode the components of a putative ABC exporter implicated in the efflux of cefoperazone and tetracycline antibiotics . In the Transporter Classification Database YbhGFSR is annotated as a 4-component system within the ATP-binding Cassette (ABC) superfamily .

## Annotation

FUNCTION: Could be involved in the sensitivity control to chloramphenicol. {ECO:0000305|PubMed:27112147}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0795|gene.b0795]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75777`
- `KEGG:ecj:JW0779;eco:b0795;`
- `GeneID:945414;`
- `GO:GO:0005886; GO:0042597; GO:0046677`

## Notes

UPF0194 membrane protein YbhG
