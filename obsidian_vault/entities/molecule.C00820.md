---
entity_id: "molecule.C00820"
entity_type: "small_molecule"
name: "D-Threonine"
source_database: "KEGG"
source_id: "C00820"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Threonine"
  - "D-2-Amino-3-hydroxybutyric acid"
---

# D-Threonine

`molecule.C00820`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00820`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Threonine; D-2-Amino-3-hydroxybutyric acid

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)

## Annotation

KEGG compound: D-Threonine; D-2-Amino-3-hydroxybutyric acid

## Pathways

- `eco00470` D-Amino acid metabolism (KEGG)

## Outgoing Edges (2)

- `represses` --> [[reaction.ecocyc.DSERDEAM-RXN|reaction.ecocyc.DSERDEAM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.THREDEHYD-RXN|reaction.ecocyc.THREDEHYD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00820`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
