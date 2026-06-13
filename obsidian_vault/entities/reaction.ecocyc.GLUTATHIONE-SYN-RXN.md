---
entity_id: "reaction.ecocyc.GLUTATHIONE-SYN-RXN"
entity_type: "reaction"
name: "GLUTATHIONE-SYN-RXN"
source_database: "EcoCyc"
source_id: "GLUTATHIONE-SYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUTATHIONE-SYN-RXN

`reaction.ecocyc.GLUTATHIONE-SYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUTATHIONE-SYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in glutathione biosynthesis. EcoCyc reaction equation: GLY + L-GAMMA-GLUTAMYLCYSTEINE + ATP -> PROTON + GLUTATHIONE + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second reaction in glutathione biosynthesis.

## Biological Role

Catalyzed by glutathione synthetase (complex.ecocyc.GLUTATHIONE-SYN-CPLX). Substrates: ATP (molecule.C00002), Glycine (molecule.C00037), gamma-L-Glutamyl-L-cysteine (molecule.C00669). Products: ADP (molecule.C00008), Glutathione (molecule.C00051), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.GLUTATHIONESYN-PWY` glutathione biosynthesis (EcoCyc)

## Annotation

This is the second reaction in glutathione biosynthesis.

## Pathways

- `ecocyc.GLUTATHIONESYN-PWY` glutathione biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `catalyzes` <-- [[complex.ecocyc.GLUTATHIONE-SYN-CPLX|complex.ecocyc.GLUTATHIONE-SYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00669|molecule.C00669]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01937|molecule.C01937]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2275|molecule.ecocyc.CPD0-2275]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUTATHIONE-SYN-RXN`

## Notes

GLY + L-GAMMA-GLUTAMYLCYSTEINE + ATP -> PROTON + GLUTATHIONE + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
