---
entity_id: "reaction.ecocyc.RXN0-6373"
entity_type: "reaction"
name: "RXN0-6373"
source_database: "EcoCyc"
source_id: "RXN0-6373"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6373

`reaction.ecocyc.RXN0-6373`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6373`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Involved in the transfer of electrons from the non-phosphorylated aldose sugars to the electron transport chain. Aldose sugar dehydrogenase is associated with the outer membrane under certain physiological conditions while glucose dehydrogenase localizes to the inner membrane . EcoCyc reaction equation: Ubiquinones + Glucopyranose -> Ubiquinols + GLC-D-LACTONE; direction=LEFT-TO-RIGHT. Involved in the transfer of electrons from the non-phosphorylated aldose sugars to the electron transport chain. Aldose sugar dehydrogenase is associated with the outer membrane under certain physiological conditions while glucose dehydrogenase localizes to the inner membrane .

## Biological Role

Catalyzed by gcd (protein.P15877). Substrates: D-Glucose (molecule.C00031), a ubiquinone (molecule.ecocyc.Ubiquinones). Products: D-Glucono-1,5-lactone (molecule.C00198), Ubiquinol (molecule.C00390).

## Enriched Pathways

- `ecocyc.GLUCOSE1PMETAB-PWY` glucose and glucose-1-phosphate degradation (EcoCyc)

## Annotation

Involved in the transfer of electrons from the non-phosphorylated aldose sugars to the electron transport chain. Aldose sugar dehydrogenase is associated with the outer membrane under certain physiological conditions while glucose dehydrogenase localizes to the inner membrane .

## Pathways

- `ecocyc.GLUCOSE1PMETAB-PWY` glucose and glucose-1-phosphate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P15877|protein.P15877]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00198|molecule.C00198]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00216|molecule.C00216]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-227|molecule.ecocyc.CPD-227]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-6001|molecule.ecocyc.CPD-6001]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.L-XYLOSE|molecule.ecocyc.L-XYLOSE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-6373`

## Notes

Ubiquinones + Glucopyranose -> Ubiquinols + GLC-D-LACTONE; direction=LEFT-TO-RIGHT
