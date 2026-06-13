---
entity_id: "reaction.ecocyc.ACETYLGLUTKIN-RXN"
entity_type: "reaction"
name: "ACETYLGLUTKIN-RXN"
source_database: "EcoCyc"
source_id: "ACETYLGLUTKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACETYLGLUTKIN-RXN

`reaction.ecocyc.ACETYLGLUTKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACETYLGLUTKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second step in arginine biosynthesis. EcoCyc reaction equation: ACETYL-GLU + ATP -> N-ACETYL-GLUTAMYL-P + ADP; direction=LEFT-TO-RIGHT. This is the second step in arginine biosynthesis.

## Biological Role

Catalyzed by acetylglutamate kinase (complex.ecocyc.ACETYLGLUTKIN-CPLX). Substrates: ATP (molecule.C00002), N-Acetyl-L-glutamate (molecule.C00624). Products: ADP (molecule.C00008), N-Acetyl-L-glutamate 5-phosphate (molecule.C04133).

## Enriched Pathways

- `ecocyc.GLUTORN-PWY` L-ornithine biosynthesis I (EcoCyc)

## Annotation

This is the second step in arginine biosynthesis.

## Pathways

- `ecocyc.GLUTORN-PWY` L-ornithine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ACETYLGLUTKIN-CPLX|complex.ecocyc.ACETYLGLUTKIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04133|molecule.C04133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00624|molecule.C00624]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ACETYLGLUTKIN-RXN`

## Notes

ACETYL-GLU + ATP -> N-ACETYL-GLUTAMYL-P + ADP; direction=LEFT-TO-RIGHT
