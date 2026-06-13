---
entity_id: "reaction.ecocyc.TRNA-PSEUDOURIDINE-SYNTHASE-I-RXN"
entity_type: "reaction"
name: "TRNA-PSEUDOURIDINE-SYNTHASE-I-RXN"
source_database: "EcoCyc"
source_id: "TRNA-PSEUDOURIDINE-SYNTHASE-I-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "tRNA-uridine isomerase"
  - "tRNA pseudouridylate synthase I"
---

# TRNA-PSEUDOURIDINE-SYNTHASE-I-RXN

`reaction.ecocyc.TRNA-PSEUDOURIDINE-SYNTHASE-I-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRNA-PSEUDOURIDINE-SYNTHASE-I-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tRNA-uridine-38-40 -> tRNA-pseudouridine-38-40; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: tRNA-uridine-38-40 -> tRNA-pseudouridine-38-40; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tRNA pseudouridine38-40 synthase (complex.ecocyc.CPLX0-7728). Substrates: a uridine38-40 in tRNA (molecule.ecocyc.tRNA-uridine-38-40). Products: a pseudouridine38-40 in tRNA (molecule.ecocyc.tRNA-pseudouridine-38-40).

## Annotation

tRNA-uridine-38-40 -> tRNA-pseudouridine-38-40; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7728|complex.ecocyc.CPLX0-7728]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.tRNA-pseudouridine-38-40|molecule.ecocyc.tRNA-pseudouridine-38-40]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-uridine-38-40|molecule.ecocyc.tRNA-uridine-38-40]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRNA-PSEUDOURIDINE-SYNTHASE-I-RXN`

## Notes

tRNA-uridine-38-40 -> tRNA-pseudouridine-38-40; direction=PHYSIOL-LEFT-TO-RIGHT
