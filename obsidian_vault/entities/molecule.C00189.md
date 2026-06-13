---
entity_id: "molecule.C00189"
entity_type: "small_molecule"
name: "Ethanolamine"
source_database: "KEGG"
source_id: "C00189"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Ethanolamine"
  - "Aminoethanol"
  - "2-Hydroxyethylamine"
---

# Ethanolamine

`molecule.C00189`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00189`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Ethanolamine; Aminoethanol; 2-Hydroxyethylamine

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

KEGG compound: Ethanolamine; Aminoethanol; 2-Hydroxyethylamine

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (10)

- `is_product_of` --> [[reaction.ecocyc.RXN-14160|reaction.ecocyc.RXN-14160]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-7948|reaction.ecocyc.RXN-7948]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7012|reaction.ecocyc.RXN0-7012]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7272|reaction.ecocyc.RXN0-7272]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-476|reaction.ecocyc.TRANS-RXN0-476]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00749|reaction.R00749]] `KEGG` `database` - C00189 <=> C00084 + C00014
- `is_substrate_of` --> [[reaction.ecocyc.ETHAMLY-RXN|reaction.ecocyc.ETHAMLY-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-476|reaction.ecocyc.TRANS-RXN0-476]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.4.3.1.17-RXN|reaction.ecocyc.4.3.1.17-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.BETAGALACTOSID-RXN|reaction.ecocyc.BETAGALACTOSID-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00189`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
