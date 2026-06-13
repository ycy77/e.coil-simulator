---
entity_id: "molecule.C01888"
entity_type: "small_molecule"
name: "Aminoacetone"
source_database: "KEGG"
source_id: "C01888"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Aminoacetone"
  - "1-Amino-2-propanone"
---

# Aminoacetone

`molecule.C01888`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01888`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Aminoacetone; 1-Amino-2-propanone

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)

## Annotation

KEGG compound: Aminoacetone; 1-Amino-2-propanone

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.R10852|reaction.R10852]] `KEGG` `database` - C05519 + C00006 <=> C01888 + C00011 + C00005 + C00080
- `is_product_of` --> [[reaction.ecocyc.AMINOPROPDEHYDROG-RXN|reaction.ecocyc.AMINOPROPDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14249|reaction.ecocyc.RXN-14249]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16001|reaction.ecocyc.RXN-16001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.THREOSPON-RXN|reaction.ecocyc.THREOSPON-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R03758|reaction.R03758]] `KEGG` `database` - C01888 + C00011 <=> C03508
- `is_substrate_of` --> [[reaction.ecocyc.AMACETOXID-RXN|reaction.ecocyc.AMACETOXID-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01888`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
