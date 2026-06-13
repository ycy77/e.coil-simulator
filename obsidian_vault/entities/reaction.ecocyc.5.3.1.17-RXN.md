---
entity_id: "reaction.ecocyc.5.3.1.17-RXN"
entity_type: "reaction"
name: "5.3.1.17-RXN"
source_database: "EcoCyc"
source_id: "5.3.1.17-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 5.3.1.17-RXN

`reaction.ecocyc.5.3.1.17-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:5.3.1.17-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-37 -> CPD-343; direction=REVERSIBLE EcoCyc reaction equation: CPD-37 -> CPD-343; direction=REVERSIBLE.

## Biological Role

Catalyzed by 5-dehydro-4-deoxy-D-glucuronate isomerase (complex.ecocyc.CPLX-8401). Substrates: 5-Dehydro-4-deoxy-D-glucuronate (molecule.C04053). Products: (4S)-4,6-Dihydroxy-2,5-dioxohexanoate (molecule.C04349).

## Annotation

CPD-37 -> CPD-343; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX-8401|complex.ecocyc.CPLX-8401]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04349|molecule.C04349]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04053|molecule.C04053]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:5.3.1.17-RXN`

## Notes

CPD-37 -> CPD-343; direction=REVERSIBLE
