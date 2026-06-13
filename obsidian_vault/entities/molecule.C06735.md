---
entity_id: "molecule.C06735"
entity_type: "small_molecule"
name: "Aminoacetaldehyde"
source_database: "KEGG"
source_id: "C06735"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Aminoacetaldehyde"
  - "2-Aminoacetaldehyde"
---

# Aminoacetaldehyde

`molecule.C06735`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06735`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Aminoacetaldehyde; 2-Aminoacetaldehyde EcoCyc common name: 2-aminoacetaldehyde.

## Biological Role

Produced in 4 reaction(s).

## Enriched Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)

## Annotation

KEGG compound: Aminoacetaldehyde; 2-Aminoacetaldehyde

## Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R05320|reaction.R05320]] `KEGG` `database` - C00245 + C00026 + C00007 <=> C00094 + C06735 + C00042 + C00011
- `is_product_of` --> [[reaction.ecocyc.RXN-16002|reaction.ecocyc.RXN-16002]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16003|reaction.ecocyc.RXN-16003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-299|reaction.ecocyc.RXN0-299]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06735`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
