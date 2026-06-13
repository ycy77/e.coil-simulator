---
entity_id: "reaction.ecocyc.RXN-14160"
entity_type: "reaction"
name: "glycerophosphorylethanolamine phosphodiesterase"
source_database: "EcoCyc"
source_id: "RXN-14160"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# glycerophosphorylethanolamine phosphodiesterase

`reaction.ecocyc.RXN-14160`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14160`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-1-GLYCEROPHOSPHORYLETHANOL-AMINE + WATER -> GLYCEROL-3P + ETHANOL-AMINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-1-GLYCEROPHOSPHORYLETHANOL-AMINE + WATER -> GLYCEROL-3P + ETHANOL-AMINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ugpQ (protein.P10908). Substrates: H2O (molecule.C00001), sn-Glycero-3-phosphoethanolamine (molecule.C01233). Products: H+ (molecule.C00080), sn-Glycerol 3-phosphate (molecule.C00093), Ethanolamine (molecule.C00189).

## Annotation

L-1-GLYCEROPHOSPHORYLETHANOL-AMINE + WATER -> GLYCEROL-3P + ETHANOL-AMINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P10908|protein.P10908]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00189|molecule.C00189]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01233|molecule.C01233]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14160`

## Notes

L-1-GLYCEROPHOSPHORYLETHANOL-AMINE + WATER -> GLYCEROL-3P + ETHANOL-AMINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
