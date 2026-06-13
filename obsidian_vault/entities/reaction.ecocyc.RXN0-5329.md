---
entity_id: "reaction.ecocyc.RXN0-5329"
entity_type: "reaction"
name: "RXN0-5329"
source_database: "EcoCyc"
source_id: "RXN0-5329"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5329

`reaction.ecocyc.RXN0-5329`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5329`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1122 -> CPD0-1123; direction=REVERSIBLE EcoCyc reaction equation: CPD0-1122 -> CPD0-1123; direction=REVERSIBLE.

## Biological Role

Catalyzed by N-acetylneuraminate mutarotase (complex.ecocyc.CPLX0-7658). Substrates: N-acetyl-α-neuraminate (molecule.ecocyc.CPD0-1122). Products: N-acetyl-β-neuraminate (molecule.ecocyc.CPD0-1123).

## Annotation

CPD0-1122 -> CPD0-1123; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7658|complex.ecocyc.CPLX0-7658]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1123|molecule.ecocyc.CPD0-1123]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1122|molecule.ecocyc.CPD0-1122]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5329`

## Notes

CPD0-1122 -> CPD0-1123; direction=REVERSIBLE
