---
entity_id: "molecule.C01563"
entity_type: "small_molecule"
name: "Carbamate"
source_database: "KEGG"
source_id: "C01563"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Carbamate"
  - "Carbamic acid"
  - "Aminoformic acid"
---

# Carbamate

`molecule.C01563`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01563`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Carbamate; Carbamic acid; Aminoformic acid

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 7 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)

## Annotation

KEGG compound: Carbamate; Carbamic acid; Aminoformic acid

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)

## Outgoing Edges (10)

- `is_product_of` --> [[reaction.R10949|reaction.R10949]] `KEGG` `database` - C00014 + C20969 <=> C01563 + C00009
- `is_product_of` --> [[reaction.R12624|reaction.R12624]] `KEGG` `database` - C20256 + C00001 <=> C20255 + C01563
- `is_product_of` --> [[reaction.ecocyc.R524-RXN|reaction.ecocyc.R524-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12896|reaction.ecocyc.RXN-12896]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16910|reaction.ecocyc.RXN-16910]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22736|reaction.ecocyc.RXN-22736]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6460|reaction.ecocyc.RXN0-6460]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14196|reaction.ecocyc.RXN-14196]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19659|reaction.ecocyc.RXN-19659]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5222|reaction.ecocyc.RXN0-5222]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01563`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
