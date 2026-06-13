---
entity_id: "molecule.C00750"
entity_type: "small_molecule"
name: "Spermine"
source_database: "KEGG"
source_id: "C00750"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Spermine"
  - "N,N'-Bis(3-aminopropyl)-1,4-butanediamine"
---

# Spermine

`molecule.C00750`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00750`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Spermine; N,N'-Bis(3-aminopropyl)-1,4-butanediamine The history of SPERMINE biochemistry goes back more than 300 years. When Antoni van Leeuwenhoek looked at human semen through the lenses of his microscope in 1678, he noted the formation of crystals in aging sperm. More than 200 years later, the basic component of these phosphate crystals was named spermine, after the source .

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Annotation

KEGG compound: Spermine; N,N'-Bis(3-aminopropyl)-1,4-butanediamine

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Outgoing Edges (2)

- `represses` --> [[reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN|reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-2481|reaction.ecocyc.RXN0-2481]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00750`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
