---
entity_id: "molecule.C01678"
entity_type: "small_molecule"
name: "Cysteamine"
source_database: "KEGG"
source_id: "C01678"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Cysteamine"
  - "2-Aminoethanethiol"
  - "beta-Aminoethanethiol"
  - "beta-Mercaptoethylamine"
  - "Mercaptamine"
  - "Thioethanolamine"
---

# Cysteamine

`molecule.C01678`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01678`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Cysteamine; 2-Aminoethanethiol; beta-Aminoethanethiol; beta-Mercaptoethylamine; Mercaptamine; Thioethanolamine

## Biological Role

Produced in 1 reaction(s).

## Enriched Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)

## Annotation

KEGG compound: Cysteamine; 2-Aminoethanethiol; beta-Aminoethanethiol; beta-Mercaptoethylamine; Mercaptamine; Thioethanolamine

## Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN-14514|reaction.ecocyc.RXN-14514]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `represses` --> [[reaction.ecocyc.BETAGALACTOSID-RXN|reaction.ecocyc.BETAGALACTOSID-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.LCYSDESULF-RXN|reaction.ecocyc.LCYSDESULF-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01678`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
