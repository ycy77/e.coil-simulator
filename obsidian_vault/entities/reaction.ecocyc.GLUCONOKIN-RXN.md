---
entity_id: "reaction.ecocyc.GLUCONOKIN-RXN"
entity_type: "reaction"
name: "GLUCONOKIN-RXN"
source_database: "EcoCyc"
source_id: "GLUCONOKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUCONOKIN-RXN

`reaction.ecocyc.GLUCONOKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUCONOKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction phosphorylates gluconate to 6-phosphogluconate which can then enter two central metabolic pathways: the Entner-Doudoroff and the pentose phosphate pathways. EcoCyc reaction equation: ATP + GLUCONATE -> PROTON + ADP + CPD-2961; direction=LEFT-TO-RIGHT. This reaction phosphorylates gluconate to 6-phosphogluconate which can then enter two central metabolic pathways: the Entner-Doudoroff and the pentose phosphate pathways.

## Biological Role

Catalyzed by D-gluconate kinase, thermostable (complex.ecocyc.GLUCONOKINII-CPLX), idnK (protein.P39208). Substrates: ATP (molecule.C00002), D-Gluconic acid (molecule.C00257). Products: ADP (molecule.C00008), H+ (molecule.C00080), 6-Phospho-D-gluconate (molecule.C00345).

## Enriched Pathways

- `ecocyc.GLUCONSUPER-PWY` D-gluconate degradation (EcoCyc)
- `ecocyc.IDNCAT-PWY` L-idonate degradation (EcoCyc)

## Annotation

This reaction phosphorylates gluconate to 6-phosphogluconate which can then enter two central metabolic pathways: the Entner-Doudoroff and the pentose phosphate pathways.

## Pathways

- `ecocyc.GLUCONSUPER-PWY` D-gluconate degradation (EcoCyc)
- `ecocyc.IDNCAT-PWY` L-idonate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.GLUCONOKINII-CPLX|complex.ecocyc.GLUCONOKINII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P39208|protein.P39208]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00345|molecule.C00345]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00257|molecule.C00257]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLUCONOKIN-RXN`

## Notes

ATP + GLUCONATE -> PROTON + ADP + CPD-2961; direction=LEFT-TO-RIGHT
