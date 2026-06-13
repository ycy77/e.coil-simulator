---
entity_id: "reaction.ecocyc.4.2.1.99-RXN"
entity_type: "reaction"
name: "4.2.1.99-RXN"
source_database: "EcoCyc"
source_id: "4.2.1.99-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 4.2.1.99-RXN

`reaction.ecocyc.4.2.1.99-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:4.2.1.99-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-618 -> CPD-1136 + WATER; direction=REVERSIBLE EcoCyc reaction equation: CPD-618 -> CPD-1136 + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by bifunctional aconitate hydratase B/2-methylisocitrate dehydratase (complex.ecocyc.CPLX0-7761). Substrates: (2S,3R)-3-Hydroxybutane-1,2,3-tricarboxylate (molecule.C04593). Products: H2O (molecule.C00001), (Z)-But-2-ene-1,2,3-tricarboxylate (molecule.C04225).

## Enriched Pathways

- `ecocyc.PWY0-42` 2-methylcitrate cycle I (EcoCyc)

## Annotation

CPD-618 -> CPD-1136 + WATER; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-42` 2-methylcitrate cycle I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7761|complex.ecocyc.CPLX0-7761]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04225|molecule.C04225]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04593|molecule.C04593]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:4.2.1.99-RXN`

## Notes

CPD-618 -> CPD-1136 + WATER; direction=REVERSIBLE
