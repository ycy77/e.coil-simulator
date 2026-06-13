---
entity_id: "molecule.C00163"
entity_type: "small_molecule"
name: "Propanoate"
source_database: "KEGG"
source_id: "C00163"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Propanoate"
  - "Propionate"
  - "Propanoic acid"
  - "Propionic acid"
---

# Propanoate

`molecule.C00163`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00163`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Propanoate; Propionate; Propanoic acid; Propionic acid

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Annotation

KEGG compound: Propanoate; Propionate; Propanoic acid; Propionic acid

## Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.ecocyc.RXN0-268|reaction.ecocyc.RXN0-268]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-505|reaction.ecocyc.TRANS-RXN0-505]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.PROPIONATE--COA-LIGASE-RXN|reaction.ecocyc.PROPIONATE--COA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PROPKIN-RXN|reaction.ecocyc.PROPKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-505|reaction.ecocyc.TRANS-RXN0-505]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ACETATE--COA-LIGASE-RXN|reaction.ecocyc.ACETATE--COA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRANS-RXN0-571|reaction.ecocyc.TRANS-RXN0-571]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00163`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
