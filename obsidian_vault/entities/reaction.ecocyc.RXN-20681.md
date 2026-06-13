---
entity_id: "reaction.ecocyc.RXN-20681"
entity_type: "reaction"
name: "RXN-20681"
source_database: "EcoCyc"
source_id: "RXN-20681"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20681

`reaction.ecocyc.RXN-20681`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20681`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-Dehydro-D-gulosides -> 3-Dehydro-D-Glucosides; direction=REVERSIBLE EcoCyc reaction equation: 3-Dehydro-D-gulosides -> 3-Dehydro-D-Glucosides; direction=REVERSIBLE.

## Biological Role

Catalyzed by 3-dehydro-D-guloside 4-epimerase (complex.ecocyc.CPLX0-8554). Substrates: a 3-dehydro-D-guloside (molecule.ecocyc.3-Dehydro-D-gulosides). Products: a 3-dehydro-D-glucoside (molecule.ecocyc.3-Dehydro-D-Glucosides).

## Enriched Pathways

- `ecocyc.PWY0-1602` D-gulosides conversion to D-glucosides (EcoCyc)

## Annotation

3-Dehydro-D-gulosides -> 3-Dehydro-D-Glucosides; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1602` D-gulosides conversion to D-glucosides (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8554|complex.ecocyc.CPLX0-8554]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.3-Dehydro-D-Glucosides|molecule.ecocyc.3-Dehydro-D-Glucosides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.3-Dehydro-D-gulosides|molecule.ecocyc.3-Dehydro-D-gulosides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20681`

## Notes

3-Dehydro-D-gulosides -> 3-Dehydro-D-Glucosides; direction=REVERSIBLE
