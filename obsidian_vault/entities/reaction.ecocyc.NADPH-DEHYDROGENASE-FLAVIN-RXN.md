---
entity_id: "reaction.ecocyc.NADPH-DEHYDROGENASE-FLAVIN-RXN"
entity_type: "reaction"
name: "NADPH-DEHYDROGENASE-FLAVIN-RXN"
source_database: "EcoCyc"
source_id: "NADPH-DEHYDROGENASE-FLAVIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NADPH-DEHYDROGENASE-FLAVIN-RXN

`reaction.ecocyc.NADPH-DEHYDROGENASE-FLAVIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NADPH-DEHYDROGENASE-FLAVIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-316 + NADP -> PROTON + RIBOFLAVIN + NADPH; direction=RIGHT-TO-LEFT EcoCyc reaction equation: CPD-316 + NADP -> PROTON + RIBOFLAVIN + NADPH; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by sulfite reductase, flavoprotein subunit complex (complex.ecocyc.CPLX0-7841), fre (protein.P0AEN1). Substrates: NADP+ (molecule.C00006), Reduced riboflavin (molecule.C01007). Products: NADPH (molecule.C00005), H+ (molecule.C00080), Riboflavin (molecule.C00255).

## Annotation

CPD-316 + NADP -> PROTON + RIBOFLAVIN + NADPH; direction=RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7841|complex.ecocyc.CPLX0-7841]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AEN1|protein.P0AEN1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00255|molecule.C00255]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01007|molecule.C01007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01727|molecule.C01727]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-19571|molecule.ecocyc.CPD-19571]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1187|molecule.ecocyc.CPD0-1187]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETATE|molecule.ecocyc.IODOACETATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:NADPH-DEHYDROGENASE-FLAVIN-RXN`

## Notes

CPD-316 + NADP -> PROTON + RIBOFLAVIN + NADPH; direction=RIGHT-TO-LEFT
