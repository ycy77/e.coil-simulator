---
entity_id: "reaction.ecocyc.RXN0-7398"
entity_type: "reaction"
name: "RXN0-7398"
source_database: "EcoCyc"
source_id: "RXN0-7398"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7398

`reaction.ecocyc.RXN0-7398`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7398`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15922 + Donor-H2 -> ADENINE + WATER + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-15922 + Donor-H2 -> ADENINE + WATER + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 6-N-hydroxylaminopurine resistance protein (complex.ecocyc.CPLX0-10380), 6-hydroxyaminopurine reductase (complex.ecocyc.CPLX0-8259). Substrates: N6-Hydroxyadenine (molecule.ecocyc.CPD-15922). Products: H2O (molecule.C00001), Adenine (molecule.C00147).

## Annotation

CPD-15922 + Donor-H2 -> ADENINE + WATER + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-10380|complex.ecocyc.CPLX0-10380]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8259|complex.ecocyc.CPLX0-8259]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15922|molecule.ecocyc.CPD-15922]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7398`

## Notes

CPD-15922 + Donor-H2 -> ADENINE + WATER + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT
