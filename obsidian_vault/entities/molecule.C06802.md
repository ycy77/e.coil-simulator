---
entity_id: "molecule.C06802"
entity_type: "small_molecule"
name: "Acarbose"
source_database: "KEGG"
source_id: "C06802"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Acarbose"
---

# Acarbose

`molecule.C06802`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06802`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Acarbose CPD-17528 Acarbose is an anti-diabetic drug used to treat type 2 diabetes mellitus and, in some countries, prediabetes. It acts by inhibiting EC-3.2.1.20, an intestinal enzyme that releases glucose from larger carbohydrates. CPD-17528 Acarbose is composed of an CPD-17553 moiety with a MALTOSE at the reducing terminus.

## Enriched Pathways

- `eco00525` Acarbose and validamycin biosynthesis (KEGG)

## Annotation

KEGG compound: Acarbose

## Pathways

- `eco00525` Acarbose and validamycin biosynthesis (KEGG)

## Outgoing Edges (2)

- `represses` --> [[reaction.ecocyc.3.5.1.88-RXN|reaction.ecocyc.3.5.1.88-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-7347|reaction.ecocyc.RXN0-7347]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06802`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
