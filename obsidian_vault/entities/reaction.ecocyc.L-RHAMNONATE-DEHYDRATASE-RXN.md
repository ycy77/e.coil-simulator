---
entity_id: "reaction.ecocyc.L-RHAMNONATE-DEHYDRATASE-RXN"
entity_type: "reaction"
name: "L-RHAMNONATE-DEHYDRATASE-RXN"
source_database: "EcoCyc"
source_id: "L-RHAMNONATE-DEHYDRATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-RHAMNONATE-DEHYDRATASE-RXN

`reaction.ecocyc.L-RHAMNONATE-DEHYDRATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:L-RHAMNONATE-DEHYDRATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-RHAMNONATE -> DEHYDRO-3-DEOXY-L-RHAMNONATE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-RHAMNONATE -> DEHYDRO-3-DEOXY-L-RHAMNONATE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by L-rhamnonate dehydratase (complex.ecocyc.CPLX0-7722). Substrates: L-Rhamnonate (molecule.C01934). Products: H2O (molecule.C00001), 2-Dehydro-3-deoxy-L-rhamnonate (molecule.C03979).

## Annotation

L-RHAMNONATE -> DEHYDRO-3-DEOXY-L-RHAMNONATE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7722|complex.ecocyc.CPLX0-7722]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03979|molecule.C03979]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01934|molecule.C01934]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:L-RHAMNONATE-DEHYDRATASE-RXN`

## Notes

L-RHAMNONATE -> DEHYDRO-3-DEOXY-L-RHAMNONATE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
