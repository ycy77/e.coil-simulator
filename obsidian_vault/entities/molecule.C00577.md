---
entity_id: "molecule.C00577"
entity_type: "small_molecule"
name: "D-Glyceraldehyde"
source_database: "KEGG"
source_id: "C00577"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Glyceraldehyde"
---

# D-Glyceraldehyde

`molecule.C00577`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00577`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Glyceraldehyde

## Biological Role

Produced in 2 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)

## Annotation

KEGG compound: D-Glyceraldehyde

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.DHDOGALDOL-RXN|reaction.ecocyc.DHDOGALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7250|reaction.ecocyc.RXN0-7250]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `represses` --> [[reaction.ecocyc.BADH-RXN|reaction.ecocyc.BADH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00577`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
