---
entity_id: "reaction.ecocyc.RXN-15893"
entity_type: "reaction"
name: "RXN-15893"
source_database: "EcoCyc"
source_id: "RXN-15893"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15893

`reaction.ecocyc.RXN-15893`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15893`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-17129 -> CPD-12349; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-17129 -> CPD-12349; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dgoD (protein.Q6BF17). Substrates: 3,6-Anhydro-L-galactonate (molecule.C20903). Products: 2-Dehydro-3-deoxy-L-galactonate (molecule.C20680).

## Enriched Pathways

- `ecocyc.PWY-7562` 3,6-anhydro-α-L-galactopyranose degradation (EcoCyc)

## Annotation

CPD-17129 -> CPD-12349; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7562` 3,6-anhydro-α-L-galactopyranose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.Q6BF17|protein.Q6BF17]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C20680|molecule.C20680]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C20903|molecule.C20903]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15893`

## Notes

CPD-17129 -> CPD-12349; direction=LEFT-TO-RIGHT
