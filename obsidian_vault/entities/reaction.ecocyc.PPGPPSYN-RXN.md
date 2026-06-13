---
entity_id: "reaction.ecocyc.PPGPPSYN-RXN"
entity_type: "reaction"
name: "PPGPPSYN-RXN"
source_database: "EcoCyc"
source_id: "PPGPPSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PPGPPSYN-RXN

`reaction.ecocyc.PPGPPSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PPGPPSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction breaks down ppGpp (guanosine 3',5'-bispyrophosphate). EcoCyc reaction equation: GUANOSINE-5DP-3DP + WATER -> PPI + GDP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction breaks down ppGpp (guanosine 3',5'-bispyrophosphate).

## Biological Role

Catalyzed by spoT (protein.P0AG24). Substrates: H2O (molecule.C00001), Guanosine 3',5'-bis(diphosphate) (molecule.C01228). Products: Diphosphate (molecule.C00013), GDP (molecule.C00035).

## Enriched Pathways

- `ecocyc.PPGPPMET-PWY` ppGpp metabolism (EcoCyc)

## Annotation

This reaction breaks down ppGpp (guanosine 3',5'-bispyrophosphate).

## Pathways

- `ecocyc.PPGPPMET-PWY` ppGpp metabolism (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `activates` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[protein.P0AFX4|protein.P0AFX4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P0AG24|protein.P0AG24]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C10164|molecule.C10164]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1413|molecule.ecocyc.CPD0-1413]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1414|molecule.ecocyc.CPD0-1414]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1415|molecule.ecocyc.CPD0-1415]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.LI|molecule.ecocyc.LI_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PPGPPSYN-RXN`

## Notes

GUANOSINE-5DP-3DP + WATER -> PPI + GDP; direction=PHYSIOL-LEFT-TO-RIGHT
