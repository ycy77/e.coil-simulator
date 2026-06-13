---
entity_id: "reaction.ecocyc.S-FORMYLGLUTATHIONE-HYDROLASE-RXN"
entity_type: "reaction"
name: "S-FORMYLGLUTATHIONE-HYDROLASE-RXN"
source_database: "EcoCyc"
source_id: "S-FORMYLGLUTATHIONE-HYDROLASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# S-FORMYLGLUTATHIONE-HYDROLASE-RXN

`reaction.ecocyc.S-FORMYLGLUTATHIONE-HYDROLASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:S-FORMYLGLUTATHIONE-HYDROLASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-548 + WATER -> PROTON + FORMATE + GLUTATHIONE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-548 + WATER -> PROTON + FORMATE + GLUTATHIONE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by S-formylglutathione hydrolase / S-lactoylglutathione hydrolase (complex.ecocyc.CPLX0-3954), frmB (protein.P51025). Substrates: H2O (molecule.C00001), S-Formylglutathione (molecule.C01031). Products: Glutathione (molecule.C00051), Formate (molecule.C00058), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-1801` formaldehyde oxidation II (glutathione-dependent) (EcoCyc)

## Annotation

CPD-548 + WATER -> PROTON + FORMATE + GLUTATHIONE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-1801` formaldehyde oxidation II (glutathione-dependent) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3954|complex.ecocyc.CPLX0-3954]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P51025|protein.P51025]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01031|molecule.C01031]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETATE|molecule.ecocyc.IODOACETATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:S-FORMYLGLUTATHIONE-HYDROLASE-RXN`

## Notes

CPD-548 + WATER -> PROTON + FORMATE + GLUTATHIONE; direction=PHYSIOL-LEFT-TO-RIGHT
