---
entity_id: "reaction.ecocyc.RXN0-6981"
entity_type: "reaction"
name: "RXN0-6981"
source_database: "EcoCyc"
source_id: "RXN0-6981"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6981

`reaction.ecocyc.RXN0-6981`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6981`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is needed because automated instantiation of this case fails for the generic version 3.4.13.18-RXN. EcoCyc reaction equation: CPD0-1445 + WATER -> L-ALPHA-ALANINE + GLT; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is needed because automated instantiation of this case fails for the generic version 3.4.13.18-RXN.

## Biological Role

Catalyzed by peptidase D (complex.ecocyc.CPLX0-3001). Substrates: H2O (molecule.C00001), L-alanyl-L-glutamate (molecule.ecocyc.CPD0-1445). Products: L-Glutamate (molecule.C00025), L-Alanine (molecule.C00041).

## Enriched Pathways

- `ecocyc.PWY0-1546` muropeptide degradation (EcoCyc)

## Annotation

This reaction is needed because automated instantiation of this case fails for the generic version 3.4.13.18-RXN.

## Pathways

- `ecocyc.PWY0-1546` muropeptide degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3001|complex.ecocyc.CPLX0-3001]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1445|molecule.ecocyc.CPD0-1445]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6981`

## Notes

CPD0-1445 + WATER -> L-ALPHA-ALANINE + GLT; direction=PHYSIOL-LEFT-TO-RIGHT
