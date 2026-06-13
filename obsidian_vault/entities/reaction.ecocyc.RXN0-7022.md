---
entity_id: "reaction.ecocyc.RXN0-7022"
entity_type: "reaction"
name: "RXN0-7022"
source_database: "EcoCyc"
source_id: "RXN0-7022"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7022

`reaction.ecocyc.RXN0-7022`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7022`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-N-ACETYLMURAMATE + CPD0-1082 + ATP -> UDP-MURNAC-TETRAPEPTIDE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: UDP-N-ACETYLMURAMATE + CPD0-1082 + ATP -> UDP-MURNAC-TETRAPEPTIDE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mpl (protein.P37773). Substrates: ATP (molecule.C00002), UDP-N-acetylmuramate (molecule.C01050), L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanine (molecule.ecocyc.CPD0-1082). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi), UDP-MurNAc-L-Ala-γ-D-Glu-meso-DAP-D-Ala (molecule.ecocyc.UDP-MURNAC-TETRAPEPTIDE).

## Annotation

UDP-N-ACETYLMURAMATE + CPD0-1082 + ATP -> UDP-MURNAC-TETRAPEPTIDE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P37773|protein.P37773]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.UDP-MURNAC-TETRAPEPTIDE|molecule.ecocyc.UDP-MURNAC-TETRAPEPTIDE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01050|molecule.C01050]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1082|molecule.ecocyc.CPD0-1082]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7022`

## Notes

UDP-N-ACETYLMURAMATE + CPD0-1082 + ATP -> UDP-MURNAC-TETRAPEPTIDE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
