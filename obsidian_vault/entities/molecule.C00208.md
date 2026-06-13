---
entity_id: "molecule.C00208"
entity_type: "small_molecule"
name: "Maltose"
source_database: "KEGG"
source_id: "C00208"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Maltose"
  - "Malt sugar"
  - "alpha-D-Glucopyranosyl-(1->4)-D-glucopyranose"
---

# Maltose

`molecule.C00208`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00208`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Maltose; Malt sugar; alpha-D-Glucopyranosyl-(1->4)-D-glucopyranose Maltose is composed of two glucose molecules linked by an α 1,4-glycosidic linkage. Maltose is produced by the hydrolysis of starch and similar compounds, and can be hydrolyzed to glucose by the enzyme maltase.

## Biological Role

Consumed as substrate in 8 reaction(s). Produced in 8 reaction(s).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: Maltose; Malt sugar; alpha-D-Glucopyranosyl-(1->4)-D-glucopyranose

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (16)

- `is_product_of` --> [[reaction.R02112|reaction.R02112]] `KEGG` `database` - C00369 <=> C00721 + C00208
- `is_product_of` --> [[reaction.ecocyc.ABC-16-RXN|reaction.ecocyc.ABC-16-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.AMYLOMALT-RXN|reaction.ecocyc.AMYLOMALT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14260|reaction.ecocyc.RXN-14260]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14261|reaction.ecocyc.RXN-14261]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1741|reaction.ecocyc.RXN0-1741]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5183|reaction.ecocyc.RXN0-5183]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-575|reaction.ecocyc.TRANS-RXN0-575]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00028|reaction.R00028]] `KEGG` `database` - C00208 + C00001 <=> 2 C00031
- `is_substrate_of` --> [[reaction.R04111|reaction.R04111]] `KEGG` `database` - C04261 + C00208 <=> C00615 + C02995
- `is_substrate_of` --> [[reaction.ecocyc.ABC-16-RXN|reaction.ecocyc.ABC-16-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MALTACETYLTRAN-RXN|reaction.ecocyc.MALTACETYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MALTODEG-RXN|reaction.ecocyc.MALTODEG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1741|reaction.ecocyc.RXN0-1741]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7347|reaction.ecocyc.RXN0-7347]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-575|reaction.ecocyc.TRANS-RXN0-575]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ABC-16-CPLX|complex.ecocyc.ABC-16-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00208`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
