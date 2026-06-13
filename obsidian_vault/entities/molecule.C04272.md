---
entity_id: "molecule.C04272"
entity_type: "small_molecule"
name: "(R)-2,3-Dihydroxy-3-methylbutanoate"
source_database: "KEGG"
source_id: "C04272"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(R)-2,3-Dihydroxy-3-methylbutanoate"
  - "(R)-2,3-Dihydroxy-isovalerate"
  - "(R)-2,3-Dihydroxy-isovaleric acid"
  - "(2R)-2,3-Dihydroxy-3-methylbutanoate"
  - "(2R)-2,3-Dihydroxy-3-methylbutanoic acid"
---

# (R)-2,3-Dihydroxy-3-methylbutanoate

`molecule.C04272`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04272`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (R)-2,3-Dihydroxy-3-methylbutanoate; (R)-2,3-Dihydroxy-isovalerate; (R)-2,3-Dihydroxy-isovaleric acid; (2R)-2,3-Dihydroxy-3-methylbutanoate; (2R)-2,3-Dihydroxy-3-methylbutanoic acid EcoCyc common name: (2R)-2,3-dihydroxy-3-methylbutanoate.

## Biological Role

Consumed as substrate in 4 reaction(s).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Annotation

KEGG compound: (R)-2,3-Dihydroxy-3-methylbutanoate; (R)-2,3-Dihydroxy-isovalerate; (R)-2,3-Dihydroxy-isovaleric acid; (2R)-2,3-Dihydroxy-3-methylbutanoate; (2R)-2,3-Dihydroxy-3-methylbutanoic acid

## Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Outgoing Edges (4)

- `is_substrate_of` --> [[reaction.R04439|reaction.R04439]] `KEGG` `database` - C04272 + C00006 <=> C06010 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R04440|reaction.R04440]] `KEGG` `database` - C04272 + C00006 <=> C04181 + C00005 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.ACETOLACTREDUCTOISOM-RXN|reaction.ecocyc.ACETOLACTREDUCTOISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DIHYDROXYISOVALDEHYDRAT-RXN|reaction.ecocyc.DIHYDROXYISOVALDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04272`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
