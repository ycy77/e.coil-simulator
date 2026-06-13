---
entity_id: "reaction.ecocyc.GMKALT-RXN"
entity_type: "reaction"
name: "GMKALT-RXN"
source_database: "EcoCyc"
source_id: "GMKALT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GMKALT-RXN

`reaction.ecocyc.GMKALT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GMKALT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction recycles dGMP. EcoCyc reaction equation: ATP + DGMP -> ADP + DGDP; direction=REVERSIBLE. This reaction recycles dGMP.

## Biological Role

Catalyzed by guanylate kinase (complex.ecocyc.GUANYL-KIN-CPLX). Substrates: ATP (molecule.C00002), dGMP (molecule.C00362). Products: ADP (molecule.C00008), dGDP (molecule.C00361).

## Annotation

This reaction recycles dGMP.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.GUANYL-KIN-CPLX|complex.ecocyc.GUANYL-KIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00361|molecule.C00361]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00362|molecule.C00362]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GMKALT-RXN`

## Notes

ATP + DGMP -> ADP + DGDP; direction=REVERSIBLE
