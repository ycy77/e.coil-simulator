---
entity_id: "reaction.ecocyc.RXN0-961"
entity_type: "reaction"
name: "RXN0-961"
source_database: "EcoCyc"
source_id: "RXN0-961"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-961

`reaction.ecocyc.RXN0-961`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-961`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-ALA-GAMMA-D-GLU-DAP + WATER -> CPD0-2190 + MESO-DIAMINOPIMELATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: L-ALA-GAMMA-D-GLU-DAP + WATER -> CPD0-2190 + MESO-DIAMINOPIMELATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by murein tripeptide amidase A (complex.ecocyc.CPLX0-7989). Substrates: H2O (molecule.C00001), L-alanyl-γ-D-glutamyl-meso-diaminopimelate (molecule.ecocyc.L-ALA-GAMMA-D-GLU-DAP). Products: meso-2,6-Diaminoheptanedioate (molecule.C00680), L-alanyl-D-glutamate (molecule.ecocyc.CPD0-2190).

## Enriched Pathways

- `ecocyc.PWY0-1546` muropeptide degradation (EcoCyc)

## Annotation

L-ALA-GAMMA-D-GLU-DAP + WATER -> CPD0-2190 + MESO-DIAMINOPIMELATE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1546` muropeptide degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7989|complex.ecocyc.CPLX0-7989]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00680|molecule.C00680]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2190|molecule.ecocyc.CPD0-2190]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.L-ALA-GAMMA-D-GLU-DAP|molecule.ecocyc.L-ALA-GAMMA-D-GLU-DAP]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-961`

## Notes

L-ALA-GAMMA-D-GLU-DAP + WATER -> CPD0-2190 + MESO-DIAMINOPIMELATE; direction=LEFT-TO-RIGHT
