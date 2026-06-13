---
entity_id: "reaction.ecocyc.RXN0-2361"
entity_type: "reaction"
name: "RXN0-2361"
source_database: "EcoCyc"
source_id: "RXN0-2361"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2361

`reaction.ecocyc.RXN0-2361`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2361`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-N-ACETYLMURAMATE + L-ALA-GAMMA-D-GLU-DAP + ATP -> PROTON + UDP-AAGM-DIAMINOHEPTANEDIOATE + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: UDP-N-ACETYLMURAMATE + L-ALA-GAMMA-D-GLU-DAP + ATP -> PROTON + UDP-AAGM-DIAMINOHEPTANEDIOATE + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mpl (protein.P37773). Substrates: ATP (molecule.C00002), UDP-N-acetylmuramate (molecule.C01050), L-alanyl-γ-D-glutamyl-meso-diaminopimelate (molecule.ecocyc.L-ALA-GAMMA-D-GLU-DAP). Products: ADP (molecule.C00008), H+ (molecule.C00080), UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimelate (molecule.C04877), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Annotation

UDP-N-ACETYLMURAMATE + L-ALA-GAMMA-D-GLU-DAP + ATP -> PROTON + UDP-AAGM-DIAMINOHEPTANEDIOATE + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P37773|protein.P37773]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04877|molecule.C04877]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01050|molecule.C01050]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.L-ALA-GAMMA-D-GLU-DAP|molecule.ecocyc.L-ALA-GAMMA-D-GLU-DAP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2361`

## Notes

UDP-N-ACETYLMURAMATE + L-ALA-GAMMA-D-GLU-DAP + ATP -> PROTON + UDP-AAGM-DIAMINOHEPTANEDIOATE + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
