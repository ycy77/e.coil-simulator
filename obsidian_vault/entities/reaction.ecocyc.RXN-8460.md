---
entity_id: "reaction.ecocyc.RXN-8460"
entity_type: "reaction"
name: "RXN-8460"
source_database: "EcoCyc"
source_id: "RXN-8460"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8460

`reaction.ecocyc.RXN-8460`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8460`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-DIHYDROXY-PHENYLALANINE + OXYGEN-MOLECULE -> PROTON + CPD-253; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-DIHYDROXY-PHENYLALANINE + OXYGEN-MOLECULE -> PROTON + CPD-253; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ygiD (protein.P24197). Substrates: Oxygen (molecule.C00007), 3,4-Dihydroxy-L-phenylalanine (molecule.C00355). Products: H+ (molecule.C00080), 4-(L-Alanin-3-yl)-2-hydroxy-cis,cis-muconate 6-semialdehyde (molecule.C04796).

## Annotation

L-DIHYDROXY-PHENYLALANINE + OXYGEN-MOLECULE -> PROTON + CPD-253; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P24197|protein.P24197]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04796|molecule.C04796]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00355|molecule.C00355]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8460`

## Notes

L-DIHYDROXY-PHENYLALANINE + OXYGEN-MOLECULE -> PROTON + CPD-253; direction=PHYSIOL-LEFT-TO-RIGHT
