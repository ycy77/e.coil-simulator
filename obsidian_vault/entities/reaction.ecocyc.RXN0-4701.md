---
entity_id: "reaction.ecocyc.RXN0-4701"
entity_type: "reaction"
name: "RXN0-4701"
source_database: "EcoCyc"
source_id: "RXN0-4701"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4701

`reaction.ecocyc.RXN0-4701`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4701`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

mRNA-Holder + WATER -> ssRNA-with-3phosphate + ssRNA-with-5OH; direction=LEFT-TO-RIGHT EcoCyc reaction equation: mRNA-Holder + WATER -> ssRNA-with-3phosphate + ssRNA-with-5OH; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ribosome-dependent mRNA interferase toxin YoeB (complex.ecocyc.CPLX0-8311). Substrates: H2O (molecule.C00001), an mRNA (molecule.ecocyc.mRNA-Holder).

## Annotation

mRNA-Holder + WATER -> ssRNA-with-3phosphate + ssRNA-with-5OH; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-3964|complex.ecocyc.CPLX0-3964]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8311|complex.ecocyc.CPLX0-8311]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.mRNA-Holder|molecule.ecocyc.mRNA-Holder]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-4701`

## Notes

mRNA-Holder + WATER -> ssRNA-with-3phosphate + ssRNA-with-5OH; direction=LEFT-TO-RIGHT
