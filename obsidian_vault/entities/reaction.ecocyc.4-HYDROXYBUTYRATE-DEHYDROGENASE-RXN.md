---
entity_id: "reaction.ecocyc.4-HYDROXYBUTYRATE-DEHYDROGENASE-RXN"
entity_type: "reaction"
name: "4-HYDROXYBUTYRATE-DEHYDROGENASE-RXN"
source_database: "EcoCyc"
source_id: "4-HYDROXYBUTYRATE-DEHYDROGENASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 4-HYDROXYBUTYRATE-DEHYDROGENASE-RXN

`reaction.ecocyc.4-HYDROXYBUTYRATE-DEHYDROGENASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:4-HYDROXYBUTYRATE-DEHYDROGENASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD + 4-HYDROXY-BUTYRATE -> PROTON + NADH + SUCC-S-ALD; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: NAD + 4-HYDROXY-BUTYRATE -> PROTON + NADH + SUCC-S-ALD; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by 3-sulfolactaldehyde reductase (complex.ecocyc.CPLX0-7794). Substrates: NAD+ (molecule.C00003), 4-Hydroxybutanoic acid (molecule.C00989). Products: NADH (molecule.C00004), H+ (molecule.C00080), Succinate semialdehyde (molecule.C00232).

## Annotation

NAD + 4-HYDROXY-BUTYRATE -> PROTON + NADH + SUCC-S-ALD; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7794|complex.ecocyc.CPLX0-7794]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00232|molecule.C00232]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00989|molecule.C00989]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:4-HYDROXYBUTYRATE-DEHYDROGENASE-RXN`

## Notes

NAD + 4-HYDROXY-BUTYRATE -> PROTON + NADH + SUCC-S-ALD; direction=PHYSIOL-RIGHT-TO-LEFT
