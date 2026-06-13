---
entity_id: "reaction.ecocyc.LYXISOM-RXN"
entity_type: "reaction"
name: "LYXISOM-RXN"
source_database: "EcoCyc"
source_id: "LYXISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# LYXISOM-RXN

`reaction.ecocyc.LYXISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LYXISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this alternative substrate reaction of E.C. 5.1.3.14, L-lyxose is isomerized to L-xylulose. EcoCyc reaction equation: L-LYXOSE -> L-XYLULOSE; direction=REVERSIBLE. In this alternative substrate reaction of E.C. 5.1.3.14, L-lyxose is isomerized to L-xylulose.

## Biological Role

Catalyzed by L-rhamnose isomerase (complex.ecocyc.CPLX0-7652). Substrates: β-L-lyxopyranose (molecule.ecocyc.L-LYXOSE). Products: L-Xylulose (molecule.C00312).

## Enriched Pathways

- `ecocyc.LYXMET-PWY` L-lyxose degradation (EcoCyc)

## Annotation

In this alternative substrate reaction of E.C. 5.1.3.14, L-lyxose is isomerized to L-xylulose.

## Pathways

- `ecocyc.LYXMET-PWY` L-lyxose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7652|complex.ecocyc.CPLX0-7652]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00312|molecule.C00312]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.L-LYXOSE|molecule.ecocyc.L-LYXOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:LYXISOM-RXN`

## Notes

L-LYXOSE -> L-XYLULOSE; direction=REVERSIBLE
