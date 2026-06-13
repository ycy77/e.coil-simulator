---
entity_id: "molecule.C04236"
entity_type: "small_molecule"
name: "(2S)-2-Isopropyl-3-oxosuccinate"
source_database: "KEGG"
source_id: "C04236"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(2S)-2-Isopropyl-3-oxosuccinate"
  - "3-Carboxy-4-methyl-2-oxopentanoate"
  - "2-Oxo-4-methyl-3-carboxypentanoate"
---

# (2S)-2-Isopropyl-3-oxosuccinate

`molecule.C04236`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04236`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (2S)-2-Isopropyl-3-oxosuccinate; 3-Carboxy-4-methyl-2-oxopentanoate; 2-Oxo-4-methyl-3-carboxypentanoate

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)

## Annotation

KEGG compound: (2S)-2-Isopropyl-3-oxosuccinate; 3-Carboxy-4-methyl-2-oxopentanoate; 2-Oxo-4-methyl-3-carboxypentanoate

## Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R04426|reaction.R04426]] `KEGG` `database` - C04411 + C00003 <=> C04236 + C00004 + C00080
- `is_product_of` --> [[reaction.ecocyc.3-ISOPROPYLMALDEHYDROG-RXN|reaction.ecocyc.3-ISOPROPYLMALDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-7800|reaction.ecocyc.RXN-7800]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04236`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
