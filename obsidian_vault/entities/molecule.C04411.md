---
entity_id: "molecule.C04411"
entity_type: "small_molecule"
name: "(2R,3S)-3-Isopropylmalate"
source_database: "KEGG"
source_id: "C04411"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(2R,3S)-3-Isopropylmalate"
  - "3-Isopropylmalate"
  - "3-Carboxy-2-hydroxy-4-methylpentanoate"
  - "2-D-threo-Hydroxy-3-carboxy-isocaproate"
---

# (2R,3S)-3-Isopropylmalate

`molecule.C04411`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04411`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (2R,3S)-3-Isopropylmalate; 3-Isopropylmalate; 3-Carboxy-2-hydroxy-4-methylpentanoate; 2-D-threo-Hydroxy-3-carboxy-isocaproate

## Biological Role

Consumed as substrate in 5 reaction(s).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)

## Annotation

KEGG compound: (2R,3S)-3-Isopropylmalate; 3-Isopropylmalate; 3-Carboxy-2-hydroxy-4-methylpentanoate; 2-D-threo-Hydroxy-3-carboxy-isocaproate

## Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)

## Outgoing Edges (5)

- `is_substrate_of` --> [[reaction.R04426|reaction.R04426]] `KEGG` `database` - C04411 + C00003 <=> C04236 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.3-ISOPROPYLMALDEHYDROG-RXN|reaction.ecocyc.3-ISOPROPYLMALDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13158|reaction.ecocyc.RXN-13158]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13163|reaction.ecocyc.RXN-13163]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8991|reaction.ecocyc.RXN-8991]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04411`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
