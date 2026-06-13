---
entity_id: "reaction.ecocyc.RXN-17956"
entity_type: "reaction"
name: "RXN-17956"
source_database: "EcoCyc"
source_id: "RXN-17956"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17956

`reaction.ecocyc.RXN-17956`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17956`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + CPD-19236 + Donor-H2 -> CPD0-2463 + CPD-19237 + CH33ADO + MET + PROTON + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + CPD-19236 + Donor-H2 -> CPD0-2463 + CPD-19237 + CH33ADO + MET + PROTON + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phnJ (protein.P16688). Substrates: S-Adenosyl-L-methionine (molecule.C00019), α-D-ribose-1-(2-N-acetamidomethylphosphonate) 5-phosphate (molecule.ecocyc.CPD-19236). Products: L-Methionine (molecule.C00073), H+ (molecule.C00080), alpha-D-Ribose 1,2-cyclic phosphate 5-phosphate (molecule.C20440), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO), N-methylacetamide (molecule.ecocyc.CPD-19237).

## Enriched Pathways

- `ecocyc.PWY-7805` (aminomethyl)phosphonate degradation (EcoCyc)

## Annotation

S-ADENOSYLMETHIONINE + CPD-19236 + Donor-H2 -> CPD0-2463 + CPD-19237 + CH33ADO + MET + PROTON + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7805` (aminomethyl)phosphonate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.ecocyc.S2O4|molecule.ecocyc.S2O4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P16688|protein.P16688]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20440|molecule.C20440]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19237|molecule.ecocyc.CPD-19237]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19236|molecule.ecocyc.CPD-19236]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17956`

## Notes

S-ADENOSYLMETHIONINE + CPD-19236 + Donor-H2 -> CPD0-2463 + CPD-19237 + CH33ADO + MET + PROTON + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT
