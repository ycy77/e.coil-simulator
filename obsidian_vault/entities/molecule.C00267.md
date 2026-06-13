---
entity_id: "molecule.C00267"
entity_type: "small_molecule"
name: "alpha-D-Glucose"
source_database: "KEGG"
source_id: "C00267"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "alpha-D-Glucose"
---

# alpha-D-Glucose

`molecule.C00267`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00267`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: alpha-D-Glucose EcoCyc common name: α-D-glucopyranose.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 7 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Annotation

KEGG compound: alpha-D-Glucose

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Outgoing Edges (9)

- `is_product_of` --> [[reaction.R00802|reaction.R00802]] `KEGG` `database` - C00089 + C00001 <=> C02336 + C00267
- `is_product_of` --> [[reaction.ecocyc.MALTODEXGLUCOSID-RXN|reaction.ecocyc.MALTODEXGLUCOSID-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14282|reaction.ecocyc.RXN-14282]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14283|reaction.ecocyc.RXN-14283]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15312|reaction.ecocyc.RXN-15312]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5183|reaction.ecocyc.RXN0-5183]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TREHALA-RXN|reaction.ecocyc.TREHALA-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00307|reaction.R00307]] `KEGG` `database` - C00267 <=> C22502
- `is_substrate_of` --> [[reaction.ecocyc.ALDOSE-1-EPIMERASE-RXN|reaction.ecocyc.ALDOSE-1-EPIMERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00267`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
