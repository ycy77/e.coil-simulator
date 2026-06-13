---
entity_id: "molecule.C00576"
entity_type: "small_molecule"
name: "Betaine aldehyde"
source_database: "KEGG"
source_id: "C00576"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Betaine aldehyde"
---

# Betaine aldehyde

`molecule.C00576`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00576`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Betaine aldehyde

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)

## Annotation

KEGG compound: Betaine aldehyde

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.CHD-RXN|reaction.ecocyc.CHD-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-6268|reaction.ecocyc.RXN-6268]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7230|reaction.ecocyc.RXN0-7230]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.BADH-RXN|reaction.ecocyc.BADH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17758|reaction.ecocyc.RXN-17758]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00576`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
