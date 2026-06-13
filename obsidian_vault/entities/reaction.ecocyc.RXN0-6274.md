---
entity_id: "reaction.ecocyc.RXN0-6274"
entity_type: "reaction"
name: "RXN0-6274"
source_database: "EcoCyc"
source_id: "RXN0-6274"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6274

`reaction.ecocyc.RXN0-6274`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6274`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-4211 + tRNA-adenine-37 -> 6-Dimethylallyladenosine37-tRNAs + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-4211 + tRNA-adenine-37 -> 6-Dimethylallyladenosine37-tRNAs + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by miaA (protein.P16384). Substrates: Dimethylallyl diphosphate (molecule.C00235), an adenine37 in tRNA (molecule.ecocyc.tRNA-adenine-37). Products: Diphosphate (molecule.C00013), N6-(3-methylbut-2-en-1-yl)-adenine37 in tRNA (molecule.ecocyc.6-Dimethylallyladenosine37-tRNAs).

## Annotation

CPD-4211 + tRNA-adenine-37 -> 6-Dimethylallyladenosine37-tRNAs + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P16384|protein.P16384]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.6-Dimethylallyladenosine37-tRNAs|molecule.ecocyc.6-Dimethylallyladenosine37-tRNAs]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00235|molecule.C00235]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-adenine-37|molecule.ecocyc.tRNA-adenine-37]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-6274`

## Notes

CPD-4211 + tRNA-adenine-37 -> 6-Dimethylallyladenosine37-tRNAs + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
