---
entity_id: "molecule.C05775"
entity_type: "small_molecule"
name: "alpha-Ribazole"
source_database: "KEGG"
source_id: "C05775"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "alpha-Ribazole"
  - "N1-(alpha-D-Ribosyl)-5,6-dimethylbenzimidazole"
---

# alpha-Ribazole

`molecule.C05775`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05775`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: alpha-Ribazole; N1-(alpha-D-Ribosyl)-5,6-dimethylbenzimidazole EcoCyc common name: α-ribazole.

## Biological Role

Produced in 2 reaction(s).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: alpha-Ribazole; N1-(alpha-D-Ribosyl)-5,6-dimethylbenzimidazole

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R05223|reaction.R05223]] `KEGG` `database` - C00194 + C00144 <=> C06510 + C05775
- `is_product_of` --> [[reaction.ecocyc.RXN-16788|reaction.ecocyc.RXN-16788]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05775`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
