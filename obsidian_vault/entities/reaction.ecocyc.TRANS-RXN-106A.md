---
entity_id: "reaction.ecocyc.TRANS-RXN-106A"
entity_type: "reaction"
name: "aspartate:succinate antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-106A"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# aspartate:succinate antiport

`reaction.ecocyc.TRANS-RXN-106A`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-106A`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

SUC + L-ASPARTATE -> L-ASPARTATE + SUC; direction=REVERSIBLE EcoCyc reaction equation: SUC + L-ASPARTATE -> L-ASPARTATE + SUC; direction=REVERSIBLE.

## Biological Role

Catalyzed by dcuA (protein.P0ABN5), dcuB (protein.P0ABN9). Substrates: Succinate (molecule.C00042), L-Aspartate (molecule.C00049). Products: Succinate (molecule.C00042), L-Aspartate (molecule.C00049).

## Enriched Pathways

- `ecocyc.PWY-8294` L-aspartate degradation III (anaerobic) (EcoCyc)

## Annotation

SUC + L-ASPARTATE -> L-ASPARTATE + SUC; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-8294` L-aspartate degradation III (anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0ABN5|protein.P0ABN5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ABN9|protein.P0ABN9]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-106A`

## Notes

SUC + L-ASPARTATE -> L-ASPARTATE + SUC; direction=REVERSIBLE
