---
entity_id: "reaction.ecocyc.3-ISOPROPYLMALISOM-RXN"
entity_type: "reaction"
name: "3-isopropylmalate dehydratase"
source_database: "EcoCyc"
source_id: "3-ISOPROPYLMALISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-isopropylmalate dehydratase

`reaction.ecocyc.3-ISOPROPYLMALISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3-ISOPROPYLMALISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second step in leucine biosynthesis after the fork with valine synthesis. The reaction involves hydration to give an intermediate dimethylcitraconate and dehydration of the intermediate, to give an isomer of the original substrate, which effects interconversion of two isomers. EcoCyc reaction equation: CPD-9451 + WATER -> 3-CARBOXY-3-HYDROXY-ISOCAPROATE; direction=REVERSIBLE. This is the second step in leucine biosynthesis after the fork with valine synthesis. The reaction involves hydration to give an intermediate dimethylcitraconate and dehydration of the intermediate, to give an isomer of the original substrate, which effects interconversion of two isomers.

## Biological Role

Substrates: H2O (molecule.C00001), 2-Isopropylmaleate (molecule.C02631). Products: alpha-Isopropylmalate (molecule.C02504).

## Enriched Pathways

- `ecocyc.LEUSYN-PWY` L-leucine biosynthesis (EcoCyc)

## Annotation

This is the second step in leucine biosynthesis after the fork with valine synthesis. The reaction involves hydration to give an intermediate dimethylcitraconate and dehydration of the intermediate, to give an isomer of the original substrate, which effects interconversion of two isomers.

## Pathways

- `ecocyc.LEUSYN-PWY` L-leucine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C02504|molecule.C02504]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02631|molecule.C02631]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3-ISOPROPYLMALISOM-RXN`

## Notes

CPD-9451 + WATER -> 3-CARBOXY-3-HYDROXY-ISOCAPROATE; direction=REVERSIBLE
