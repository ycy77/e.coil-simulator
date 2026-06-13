---
entity_id: "reaction.ecocyc.TRANS-RXN0-268"
entity_type: "reaction"
name: "TRANS-RXN0-268"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-268"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-268

`reaction.ecocyc.TRANS-RXN0-268`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-268`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + L-ALA-GAMMA-D-GLU-DAP + WATER -> L-ALA-GAMMA-D-GLU-DAP + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + L-ALA-GAMMA-D-GLU-DAP + WATER -> L-ALA-GAMMA-D-GLU-DAP + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by murein tripeptide ABC transporter (complex.ecocyc.CPLX0-3970). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-alanyl-γ-D-glutamyl-meso-diaminopimelate (molecule.ecocyc.L-ALA-GAMMA-D-GLU-DAP). Products: ADP (molecule.C00008), H+ (molecule.C00080), L-alanyl-γ-D-glutamyl-meso-diaminopimelate (molecule.ecocyc.L-ALA-GAMMA-D-GLU-DAP), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + L-ALA-GAMMA-D-GLU-DAP + WATER -> L-ALA-GAMMA-D-GLU-DAP + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3970|complex.ecocyc.CPLX0-3970]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.L-ALA-GAMMA-D-GLU-DAP|molecule.ecocyc.L-ALA-GAMMA-D-GLU-DAP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.L-ALA-GAMMA-D-GLU-DAP|molecule.ecocyc.L-ALA-GAMMA-D-GLU-DAP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-268`

## Notes

ATP + L-ALA-GAMMA-D-GLU-DAP + WATER -> L-ALA-GAMMA-D-GLU-DAP + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
