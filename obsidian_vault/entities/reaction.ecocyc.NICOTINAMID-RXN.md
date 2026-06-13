---
entity_id: "reaction.ecocyc.NICOTINAMID-RXN"
entity_type: "reaction"
name: "NICOTINAMID-RXN"
source_database: "EcoCyc"
source_id: "NICOTINAMID-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Nicotine deamidase"
---

# NICOTINAMID-RXN

`reaction.ecocyc.NICOTINAMID-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NICOTINAMID-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in the cycling of NAD. EcoCyc reaction equation: NIACINAMIDE + WATER -> AMMONIUM + NIACINE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is involved in the cycling of NAD.

## Biological Role

Catalyzed by pncA (protein.P21369). Substrates: H2O (molecule.C00001), Nicotinamide (molecule.C00153). Products: Nicotinate (molecule.C00253), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PYRIDNUCSAL-PWY` NAD salvage pathway I (PNC VI cycle) (EcoCyc)

## Annotation

This reaction is involved in the cycling of NAD.

## Pathways

- `ecocyc.PYRIDNUCSAL-PWY` NAD salvage pathway I (PNC VI cycle) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P21369|protein.P21369]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00253|molecule.C00253]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00153|molecule.C00153]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:NICOTINAMID-RXN`

## Notes

NIACINAMIDE + WATER -> AMMONIUM + NIACINE; direction=PHYSIOL-LEFT-TO-RIGHT
