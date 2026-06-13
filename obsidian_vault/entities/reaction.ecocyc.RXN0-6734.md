---
entity_id: "reaction.ecocyc.RXN0-6734"
entity_type: "reaction"
name: "RXN0-6734"
source_database: "EcoCyc"
source_id: "RXN0-6734"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6734

`reaction.ecocyc.RXN0-6734`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6734`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + CPD0-2480 + Donor-H2 -> CPD0-2463 + CH4 + CH33ADO + MET + PROTON + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + CPD0-2480 + Donor-H2 -> CPD0-2463 + CH4 + CH33ADO + MET + PROTON + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phnJ (protein.P16688). Substrates: S-Adenosyl-L-methionine (molecule.C00019), alpha-D-Ribose 1-methylphosphonate 5-phosphate (molecule.C20423). Products: L-Methionine (molecule.C00073), H+ (molecule.C00080), Methane (molecule.C01438), alpha-D-Ribose 1,2-cyclic phosphate 5-phosphate (molecule.C20440), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO).

## Enriched Pathways

- `ecocyc.PWY0-1533` methylphosphonate degradation I (EcoCyc)

## Annotation

S-ADENOSYLMETHIONINE + CPD0-2480 + Donor-H2 -> CPD0-2463 + CH4 + CH33ADO + MET + PROTON + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1533` methylphosphonate degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.ecocyc.S2O4|molecule.ecocyc.S2O4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P16688|protein.P16688]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01438|molecule.C01438]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20440|molecule.C20440]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C20423|molecule.C20423]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6734`

## Notes

S-ADENOSYLMETHIONINE + CPD0-2480 + Donor-H2 -> CPD0-2463 + CH4 + CH33ADO + MET + PROTON + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT
