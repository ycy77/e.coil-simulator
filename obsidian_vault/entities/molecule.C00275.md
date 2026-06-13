---
entity_id: "molecule.C00275"
entity_type: "small_molecule"
name: "D-Mannose 6-phosphate"
source_database: "KEGG"
source_id: "C00275"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Mannose 6-phosphate"
---

# D-Mannose 6-phosphate

`molecule.C00275`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00275`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Mannose 6-phosphate This compound class represents a sugar phosphate that exists in solution in multiple configurations. The open-chain structure shown here is provided only as a schematic illustration of chirality. Consult the appropriate class instances for information on specific ring structures and their anomeric configuration.

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: D-Mannose 6-phosphate

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.R00772|reaction.R00772]] `KEGG` `database` - C00275 <=> C00085
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17724|reaction.ecocyc.RXN-17724]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00275`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
