---
entity_id: "molecule.C00532"
entity_type: "small_molecule"
name: "L-Arabitol"
source_database: "KEGG"
source_id: "C00532"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Arabitol"
  - "L-Arabinol"
  - "L-Arabinitol"
  - "L-Lyxitol"
---

# L-Arabitol

`molecule.C00532`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00532`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Arabitol; L-Arabinol; L-Arabinitol; L-Lyxitol EcoCyc common name: L-arabinitol.

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Annotation

KEGG compound: L-Arabitol; L-Arabinol; L-Arabinitol; L-Lyxitol

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.ecocyc.RXN-8772|reaction.ecocyc.RXN-8772]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ARABISOM-RXN|reaction.ecocyc.ARABISOM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DARABISOM-RXN|reaction.ecocyc.DARABISOM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00532`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
