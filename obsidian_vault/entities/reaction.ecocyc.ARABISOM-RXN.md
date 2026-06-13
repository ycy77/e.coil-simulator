---
entity_id: "reaction.ecocyc.ARABISOM-RXN"
entity_type: "reaction"
name: "ARABISOM-RXN"
source_database: "EcoCyc"
source_id: "ARABISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ARABISOM-RXN

`reaction.ecocyc.ARABISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ARABISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The first step of L-arabinose catabolism after it is transported into the cell. EcoCyc reaction equation: BETA-L-ARABINOSE -> L-RIBULOSE; direction=REVERSIBLE. The first step of L-arabinose catabolism after it is transported into the cell.

## Biological Role

Catalyzed by L-arabinose isomerase (complex.ecocyc.ARABISOM-CPLX). Substrates: β-L-arabinopyranose (molecule.ecocyc.BETA-L-ARABINOSE). Products: L-Ribulose (molecule.C00508).

## Enriched Pathways

- `ecocyc.ARABCAT-PWY` L-arabinose degradation I (EcoCyc)

## Annotation

The first step of L-arabinose catabolism after it is transported into the cell.

## Pathways

- `ecocyc.ARABCAT-PWY` L-arabinose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ARABISOM-CPLX|complex.ecocyc.ARABISOM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00508|molecule.C00508]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.BETA-L-ARABINOSE|molecule.ecocyc.BETA-L-ARABINOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00474|molecule.C00474]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00532|molecule.C00532]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ARABISOM-RXN`

## Notes

BETA-L-ARABINOSE -> L-RIBULOSE; direction=REVERSIBLE
