---
entity_id: "reaction.ecocyc.TARTRATE-DEHYDROGENASE-RXN"
entity_type: "reaction"
name: "TARTRATE-DEHYDROGENASE-RXN"
source_database: "EcoCyc"
source_id: "TARTRATE-DEHYDROGENASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TARTRATE-DEHYDROGENASE-RXN

`reaction.ecocyc.TARTRATE-DEHYDROGENASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TARTRATE-DEHYDROGENASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD + TARTRATE -> PROTON + NADH + CPD-66; direction=REVERSIBLE EcoCyc reaction equation: NAD + TARTRATE -> PROTON + NADH + CPD-66; direction=REVERSIBLE.

## Biological Role

Catalyzed by dmlA (protein.P76251). Substrates: NAD+ (molecule.C00003), (R,R)-Tartaric acid (molecule.C00898). Products: NADH (molecule.C00004), H+ (molecule.C00080), 2-Hydroxy-3-oxosuccinate (molecule.C03459).

## Annotation

NAD + TARTRATE -> PROTON + NADH + CPD-66; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P76251|protein.P76251]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03459|molecule.C03459]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00898|molecule.C00898]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TARTRATE-DEHYDROGENASE-RXN`

## Notes

NAD + TARTRATE -> PROTON + NADH + CPD-66; direction=REVERSIBLE
