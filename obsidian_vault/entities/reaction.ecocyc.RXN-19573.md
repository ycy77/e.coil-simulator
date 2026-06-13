---
entity_id: "reaction.ecocyc.RXN-19573"
entity_type: "reaction"
name: "RXN-19573"
source_database: "EcoCyc"
source_id: "RXN-19573"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19573

`reaction.ecocyc.RXN-19573`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19573`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLUTATHIONE + CPD-21167 -> CPD-21160 + CL- + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLUTATHIONE + CPD-21167 -> CPD-21160 + CL- + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Glutathione (molecule.C00051), monochlorobimane (molecule.ecocyc.CPD-21167). Products: H+ (molecule.C00080), chloride (molecule.ecocyc.CL-), (glutathion-S-yl)-bimane (molecule.ecocyc.CPD-21160).

## Annotation

GLUTATHIONE + CPD-21167 -> CPD-21160 + CL- + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CL-|molecule.ecocyc.CL-]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21160|molecule.ecocyc.CPD-21160]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21167|molecule.ecocyc.CPD-21167]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19573`

## Notes

GLUTATHIONE + CPD-21167 -> CPD-21160 + CL- + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
