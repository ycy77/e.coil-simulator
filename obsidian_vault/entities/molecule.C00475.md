---
entity_id: "molecule.C00475"
entity_type: "small_molecule"
name: "Cytidine"
source_database: "KEGG"
source_id: "C00475"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Cytidine"
---

# Cytidine

`molecule.C00475`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00475`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Cytidine

## Biological Role

Consumed as substrate in 10 reaction(s). Produced in 9 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Cytidine

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (20)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8051|complex.ecocyc.CPLX0-8051]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00511|reaction.R00511]] `KEGG` `database` - C00055 + C00001 <=> C00475 + C00009
- `is_product_of` --> [[reaction.R02370|reaction.R02370]] `KEGG` `database` - C05822 + C00001 <=> C00475 + C00009
- `is_product_of` --> [[reaction.R12635|reaction.R12635]] `KEGG` `database` - C22293 + C00001 <=> C00475 + C00033
- `is_product_of` --> [[reaction.ecocyc.RXN-14026|reaction.ecocyc.RXN-14026]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14090|reaction.ecocyc.RXN-14090]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14511|reaction.ecocyc.RXN-14511]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18241|reaction.ecocyc.RXN-18241]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21270|reaction.ecocyc.RXN-21270]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-108B|reaction.ecocyc.TRANS-RXN-108B]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00513|reaction.R00513]] `KEGG` `database` - C00002 + C00475 <=> C00008 + C00055
- `is_substrate_of` --> [[reaction.R00517|reaction.R00517]] `KEGG` `database` - C00044 + C00475 <=> C00035 + C00055
- `is_substrate_of` --> [[reaction.R01878|reaction.R01878]] `KEGG` `database` - C00475 + C00001 <=> C00299 + C00014
- `is_substrate_of` --> [[reaction.R02137|reaction.R02137]] `KEGG` `database` - C00475 + C00001 <=> C00380 + C00121
- `is_substrate_of` --> [[reaction.ecocyc.CYTIDEAM2-RXN|reaction.ecocyc.CYTIDEAM2-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CYTIDINEKIN-RXN|reaction.ecocyc.CYTIDINEKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CYTIKIN-RXN|reaction.ecocyc.CYTIKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-361|reaction.ecocyc.RXN0-361]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6409|reaction.ecocyc.RXN0-6409]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-108B|reaction.ecocyc.TRANS-RXN-108B]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00475`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
