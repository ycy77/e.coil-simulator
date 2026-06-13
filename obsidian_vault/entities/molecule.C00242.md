---
entity_id: "molecule.C00242"
entity_type: "small_molecule"
name: "Guanine"
source_database: "KEGG"
source_id: "C00242"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Guanine"
  - "2-Amino-6-hydroxypurine"
---

# Guanine

`molecule.C00242`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00242`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Guanine; 2-Amino-6-hydroxypurine

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 8 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: Guanine; 2-Amino-6-hydroxypurine

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (11)

- `is_product_of` --> [[reaction.R02147|reaction.R02147]] `KEGG` `database` - C00387 + C00009 <=> C00242 + C00620
- `is_product_of` --> [[reaction.R10209|reaction.R10209]] `KEGG` `database` - C01977 + C16675 <=> C20446 + C00242
- `is_product_of` --> [[reaction.ecocyc.DEOXYGUANPHOSPHOR-RXN|reaction.ecocyc.DEOXYGUANPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GUANPRIBOSYLTRAN-RXN|reaction.ecocyc.GUANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1321|reaction.ecocyc.RXN0-1321]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5199|reaction.ecocyc.RXN0-5199]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7352|reaction.ecocyc.RXN0-7352]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-578|reaction.ecocyc.TRANS-RXN0-578]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GUANINE-DEAMINASE-RXN|reaction.ecocyc.GUANINE-DEAMINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-578|reaction.ecocyc.TRANS-RXN0-578]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.TRANS-RXN0-562|reaction.ecocyc.TRANS-RXN0-562]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.Q46817|protein.Q46817]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00242`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
