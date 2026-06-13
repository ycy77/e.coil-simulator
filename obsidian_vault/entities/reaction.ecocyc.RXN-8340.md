---
entity_id: "reaction.ecocyc.RXN-8340"
entity_type: "reaction"
name: "RXN-8340"
source_database: "EcoCyc"
source_id: "RXN-8340"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8340

`reaction.ecocyc.RXN-8340`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8340`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + GTP + Donor-H2 -> CPD-19179 + MET + CH33ADO + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + GTP + Donor-H2 -> CPD-19179 + MET + CH33ADO + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by moaA (protein.P30745). Substrates: S-Adenosyl-L-methionine (molecule.C00019), GTP (molecule.C00044). Products: L-Methionine (molecule.C00073), H+ (molecule.C00080), (8S)-3',8-Cyclo-7,8-dihydroguanosine 5'-triphosphate (molecule.C21310), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO).

## Enriched Pathways

- `ecocyc.PWY-6823` molybdopterin biosynthesis (EcoCyc)

## Annotation

S-ADENOSYLMETHIONINE + GTP + Donor-H2 -> CPD-19179 + MET + CH33ADO + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6823` molybdopterin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P30745|protein.P30745]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C21310|molecule.C21310]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8340`

## Notes

S-ADENOSYLMETHIONINE + GTP + Donor-H2 -> CPD-19179 + MET + CH33ADO + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
