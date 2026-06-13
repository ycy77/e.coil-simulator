---
entity_id: "reaction.ecocyc.RXN0-5304"
entity_type: "reaction"
name: "RXN0-5304"
source_database: "EcoCyc"
source_id: "RXN0-5304"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5304

`reaction.ecocyc.RXN0-5304`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5304`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1110 -> CPD0-1108; direction=REVERSIBLE EcoCyc reaction equation: CPD0-1110 -> CPD0-1108; direction=REVERSIBLE.

## Biological Role

Catalyzed by L-fucose mutarotase (complex.ecocyc.CPLX0-7645), D-ribose pyranase (complex.ecocyc.CPLX0-7646). Substrates: β-D-ribopyranose (molecule.ecocyc.CPD0-1110). Products: β-D-ribofuranose (molecule.ecocyc.CPD0-1108).

## Enriched Pathways

- `ecocyc.RIBOKIN-PWY` ribose phosphorylation (EcoCyc)

## Annotation

CPD0-1110 -> CPD0-1108; direction=REVERSIBLE

## Pathways

- `ecocyc.RIBOKIN-PWY` ribose phosphorylation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7645|complex.ecocyc.CPLX0-7645]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7646|complex.ecocyc.CPLX0-7646]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1108|molecule.ecocyc.CPD0-1108]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1110|molecule.ecocyc.CPD0-1110]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5304`

## Notes

CPD0-1110 -> CPD0-1108; direction=REVERSIBLE
