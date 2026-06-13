---
entity_id: "reaction.ecocyc.RXN0-303"
entity_type: "reaction"
name: "RXN0-303"
source_database: "EcoCyc"
source_id: "RXN0-303"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-303

`reaction.ecocyc.RXN0-303`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-303`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-ALLOSE-6-PHOSPHATE -> D-ALLULOSE-6-PHOSPHATE; direction=REVERSIBLE EcoCyc reaction equation: D-ALLOSE-6-PHOSPHATE -> D-ALLULOSE-6-PHOSPHATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by allose-6-phosphate isomerase / ribose-5-phosphate isomerase B (complex.ecocyc.RIB5PISOMB-CPLX). Substrates: D-Allose 6-phosphate (molecule.C02962). Products: D-Allulose 6-phosphate (molecule.C18096).

## Enriched Pathways

- `ecocyc.PWY0-44` D-allose degradation (EcoCyc)

## Annotation

D-ALLOSE-6-PHOSPHATE -> D-ALLULOSE-6-PHOSPHATE; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-44` D-allose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.RIB5PISOMB-CPLX|complex.ecocyc.RIB5PISOMB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C18096|molecule.C18096]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C02962|molecule.C02962]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-303`

## Notes

D-ALLOSE-6-PHOSPHATE -> D-ALLULOSE-6-PHOSPHATE; direction=REVERSIBLE
