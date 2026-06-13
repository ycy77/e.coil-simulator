---
entity_id: "molecule.C04121"
entity_type: "small_molecule"
name: "CMP-3-deoxy-D-manno-octulosonate"
source_database: "KEGG"
source_id: "C04121"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "CMP-3-deoxy-D-manno-octulosonate"
  - "CMP-KDO"
  - "CMP-beta-KDO"
---

# CMP-3-deoxy-D-manno-octulosonate

`molecule.C04121`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04121`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: CMP-3-deoxy-D-manno-octulosonate; CMP-KDO; CMP-beta-KDO EcoCyc common name: CMP-3-deoxy-β-D-manno-octulosonate. KDO (known as Kdo for ketodeoxyoctonate) is a part of the inner core of lipopolysaccharides. It is added to the lipid A precursor LIPID-IV-A in sequential steps, with different Kdo units added by different linkages. The first unit is always added by a (2->6) glycosidic linkage and the second one by a (2->4) linkage. The actual donor of Kdo units is its activated form, CMP-Kdo.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: CMP-3-deoxy-D-manno-octulosonate; CMP-KDO; CMP-beta-KDO

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.CPM-KDOSYNTH-RXN|reaction.ecocyc.CPM-KDOSYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R04658|reaction.R04658]] `KEGG` `database` - C04919 + C04121 <=> C06024 + C00055
- `is_substrate_of` --> [[reaction.ecocyc.KDOTRANS-RXN|reaction.ecocyc.KDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.KDOTRANS2-RXN|reaction.ecocyc.KDOTRANS2-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11326|reaction.ecocyc.RXN-11326]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04121`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
