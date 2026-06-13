---
entity_id: "reaction.ecocyc.N-ACETYLGLUCOSAMINE-KINASE-RXN"
entity_type: "reaction"
name: "N-ACETYLGLUCOSAMINE-KINASE-RXN"
source_database: "EcoCyc"
source_id: "N-ACETYLGLUCOSAMINE-KINASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# N-ACETYLGLUCOSAMINE-KINASE-RXN

`reaction.ecocyc.N-ACETYLGLUCOSAMINE-KINASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:N-ACETYLGLUCOSAMINE-KINASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N-acetyl-D-glucosamine + ATP -> N-ACETYL-D-GLUCOSAMINE-6-P + PROTON + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: N-acetyl-D-glucosamine + ATP -> N-ACETYL-D-GLUCOSAMINE-6-P + PROTON + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nagK (protein.P75959). Substrates: ATP (molecule.C00002), N-Acetyl-D-glucosamine (molecule.C00140). Products: ADP (molecule.C00008), H+ (molecule.C00080), N-Acetyl-D-glucosamine 6-phosphate (molecule.C00357).

## Annotation

N-acetyl-D-glucosamine + ATP -> N-ACETYL-D-GLUCOSAMINE-6-P + PROTON + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P75959|protein.P75959]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00357|molecule.C00357]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00140|molecule.C00140]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:N-ACETYLGLUCOSAMINE-KINASE-RXN`

## Notes

N-acetyl-D-glucosamine + ATP -> N-ACETYL-D-GLUCOSAMINE-6-P + PROTON + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
