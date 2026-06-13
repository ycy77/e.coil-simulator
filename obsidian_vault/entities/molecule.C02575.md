---
entity_id: "molecule.C02575"
entity_type: "small_molecule"
name: "Pentachlorophenol"
source_database: "KEGG"
source_id: "C02575"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Pentachlorophenol"
  - "PCP"
---

# Pentachlorophenol

`molecule.C02575`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02575`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Pentachlorophenol; PCP Pentachlorophenol is a polychlorinated aromatic compound used as a wood preservative and broad spectrum biocide.

## Enriched Pathways

- `eco00361` Chlorocyclohexane and chlorobenzene degradation (KEGG)

## Annotation

KEGG compound: Pentachlorophenol; PCP

## Pathways

- `eco00361` Chlorocyclohexane and chlorobenzene degradation (KEGG)

## Outgoing Edges (2)

- `represses` --> [[reaction.ecocyc.R601-RXN|reaction.ecocyc.R601-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN|reaction.ecocyc.SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02575`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
