---
entity_id: "molecule.C00380"
entity_type: "small_molecule"
name: "Cytosine"
source_database: "KEGG"
source_id: "C00380"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Cytosine"
---

# Cytosine

`molecule.C00380`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00380`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Cytosine

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: Cytosine

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.R00510|reaction.R00510]] `KEGG` `database` - C00055 + C00001 <=> C00380 + C00117
- `is_product_of` --> [[reaction.R02137|reaction.R02137]] `KEGG` `database` - C00475 + C00001 <=> C00380 + C00121
- `is_product_of` --> [[reaction.ecocyc.RXN-14065|reaction.ecocyc.RXN-14065]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-361|reaction.ecocyc.RXN0-361]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-116|reaction.ecocyc.TRANS-RXN-116]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.CYTDEAM-RXN|reaction.ecocyc.CYTDEAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-116|reaction.ecocyc.TRANS-RXN-116]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.TRANS-RXN-132|reaction.ecocyc.TRANS-RXN-132]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P0AA82|protein.P0AA82]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00380`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
