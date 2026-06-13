---
entity_id: "reaction.ecocyc.TRANS-RXN-379"
entity_type: "reaction"
name: "L-aspartate:fumarate antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-379"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-aspartate:fumarate antiport

`reaction.ecocyc.TRANS-RXN-379`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-379`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

L-ASPARTATE + FUM -> L-ASPARTATE + FUM; direction=REVERSIBLE EcoCyc reaction equation: L-ASPARTATE + FUM -> L-ASPARTATE + FUM; direction=REVERSIBLE.

## Biological Role

Catalyzed by dcuA (protein.P0ABN5). Substrates: L-Aspartate (molecule.C00049), Fumarate (molecule.C00122). Products: L-Aspartate (molecule.C00049), Fumarate (molecule.C00122).

## Enriched Pathways

- `ecocyc.PWY-8291` L-aspartate degradation II (aerobic) (EcoCyc)

## Annotation

L-ASPARTATE + FUM -> L-ASPARTATE + FUM; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-8291` L-aspartate degradation II (aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0ABN5|protein.P0ABN5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-379`

## Notes

L-ASPARTATE + FUM -> L-ASPARTATE + FUM; direction=REVERSIBLE
