---
entity_id: "molecule.C00969"
entity_type: "small_molecule"
name: "3-Hydroxypropanal"
source_database: "KEGG"
source_id: "C00969"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-Hydroxypropanal"
---

# 3-Hydroxypropanal

`molecule.C00969`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00969`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-Hydroxypropanal HYDROXYPROPANAL 3-Hydroxypropanal is an intermediate in the degradation of GLYCEROL to CPD-347 (see PWY-6130). It was independently described as an antimicrobial compound produced by the probiotic bacterium TAX-1598, and was named reuterin . It was later shown to be identical to HYDROXYPROPANAL . Reuterin has been shown to be bioactive against bacteria, viruses and fungi . Reuterin induces oxidative stress in cells, most likely by modifying thiol groups in proteins and small molecules .

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)

## Annotation

KEGG compound: 3-Hydroxypropanal

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.RXN0-6487|reaction.ecocyc.RXN0-6487]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20077|reaction.ecocyc.RXN-20077]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20079|reaction.ecocyc.RXN-20079]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5455|reaction.ecocyc.RXN0-5455]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00969`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
