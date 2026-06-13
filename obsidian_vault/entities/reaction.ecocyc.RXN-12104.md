---
entity_id: "reaction.ecocyc.RXN-12104"
entity_type: "reaction"
name: "RXN-12104"
source_database: "EcoCyc"
source_id: "RXN-12104"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12104

`reaction.ecocyc.RXN-12104`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12104`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tRNAs-with-queuine + Acceptor + WATER -> tRNAs-containing-epoxy-quenosine + Donor-H2; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: tRNAs-with-queuine + Acceptor + WATER -> tRNAs-containing-epoxy-quenosine + Donor-H2; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by queG (protein.P39288). Substrates: H2O (molecule.C00001), a queuosine in tRNA (molecule.ecocyc.tRNAs-with-queuine). Products: an epoxyqueuosine34 in tRNA (molecule.ecocyc.tRNAs-containing-epoxy-quenosine).

## Enriched Pathways

- `ecocyc.PWY-6700` queuosine biosynthesis I (de novo) (EcoCyc)

## Annotation

tRNAs-with-queuine + Acceptor + WATER -> tRNAs-containing-epoxy-quenosine + Donor-H2; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-6700` queuosine biosynthesis I (de novo) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P39288|protein.P39288]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.tRNAs-containing-epoxy-quenosine|molecule.ecocyc.tRNAs-containing-epoxy-quenosine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNAs-with-queuine|molecule.ecocyc.tRNAs-with-queuine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12104`

## Notes

tRNAs-with-queuine + Acceptor + WATER -> tRNAs-containing-epoxy-quenosine + Donor-H2; direction=PHYSIOL-RIGHT-TO-LEFT
