---
entity_id: "reaction.ecocyc.ALDEHYDE-DEHYDROGENASE-NADP_-RXN"
entity_type: "reaction"
name: "ALDEHYDE-DEHYDROGENASE-NADP+-RXN"
source_database: "EcoCyc"
source_id: "ALDEHYDE-DEHYDROGENASE-NADP+-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ALDEHYDE-DEHYDROGENASE-NADP+-RXN

`reaction.ecocyc.ALDEHYDE-DEHYDROGENASE-NADP_-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALDEHYDE-DEHYDROGENASE-NADP+-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Aldehydes + WATER + NADP -> Carboxylates + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Aldehydes + WATER + NADP -> Carboxylates + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006), Aldehyde (molecule.C00071). Products: NADPH (molecule.C00005), H+ (molecule.C00080), a carboxylate (molecule.ecocyc.Carboxylates).

## Annotation

Aldehydes + WATER + NADP -> Carboxylates + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Carboxylates|molecule.ecocyc.Carboxylates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00071|molecule.C00071]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ALDEHYDE-DEHYDROGENASE-NADP+-RXN`

## Notes

Aldehydes + WATER + NADP -> Carboxylates + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
