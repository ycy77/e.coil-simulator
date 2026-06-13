---
entity_id: "molecule.C00437"
entity_type: "small_molecule"
name: "N-Acetylornithine"
source_database: "KEGG"
source_id: "C00437"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N-Acetylornithine"
  - "N2-Acetyl-L-ornithine"
---

# N-Acetylornithine

`molecule.C00437`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00437`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N-Acetylornithine; N2-Acetyl-L-ornithine EcoCyc common name: N-acetyl-L-ornithine.

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)

## Annotation

KEGG compound: N-Acetylornithine; N2-Acetyl-L-ornithine

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.R00669|reaction.R00669]] `KEGG` `database` - C00437 + C00001 <=> C00033 + C00077
- `is_substrate_of` --> [[reaction.ecocyc.ACETYLORNDEACET-RXN|reaction.ecocyc.ACETYLORNDEACET-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ACETYLORNTRANSAM-RXN|reaction.ecocyc.ACETYLORNTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00437`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
