---
entity_id: "molecule.C00601"
entity_type: "small_molecule"
name: "Phenylacetaldehyde"
source_database: "KEGG"
source_id: "C00601"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phenylacetaldehyde"
  - "alpha-Tolualdehyde"
---

# Phenylacetaldehyde

`molecule.C00601`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00601`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phenylacetaldehyde; alpha-Tolualdehyde

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Annotation

KEGG compound: Phenylacetaldehyde; alpha-Tolualdehyde

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.R02613|reaction.R02613]] `KEGG` `database` - C05332 + C00007 + C00001 <=> C00601 + C00014 + C00027
- `is_product_of` --> [[reaction.ecocyc.RXN-10817|reaction.ecocyc.RXN-10817]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-284|reaction.ecocyc.TRANS-RXN0-284]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.PHENDEHYD-RXN|reaction.ecocyc.PHENDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-284|reaction.ecocyc.TRANS-RXN0-284]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.BADH-RXN|reaction.ecocyc.BADH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PHENDEHYD-RXN|reaction.ecocyc.PHENDEHYD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00601`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
