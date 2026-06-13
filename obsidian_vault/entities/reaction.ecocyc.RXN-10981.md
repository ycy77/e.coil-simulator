---
entity_id: "reaction.ecocyc.RXN-10981"
entity_type: "reaction"
name: "RXN-10981"
source_database: "EcoCyc"
source_id: "RXN-10981"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-10981

`reaction.ecocyc.RXN-10981`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-10981`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acceptor + ASCORBATE + PROTON -> Donor-H2 + CPD-318; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Acceptor + ASCORBATE + PROTON -> Donor-H2 + CPD-318; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: Ascorbate (molecule.C00072), H+ (molecule.C00080). Products: Monodehydroascorbate (molecule.C01041).

## Annotation

Acceptor + ASCORBATE + PROTON -> Donor-H2 + CPD-318; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C01041|molecule.C01041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00072|molecule.C00072]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-10981`

## Notes

Acceptor + ASCORBATE + PROTON -> Donor-H2 + CPD-318; direction=LEFT-TO-RIGHT
