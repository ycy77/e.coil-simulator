---
entity_id: "molecule.C06018"
entity_type: "small_molecule"
name: "dTDP-4-acetamido-4,6-dideoxy-D-glucose"
source_database: "KEGG"
source_id: "C06018"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dTDP-4-acetamido-4,6-dideoxy-D-glucose"
  - "dTDP-4-acetamido-4,6-dideoxy-alpha-D-glucose"
  - "dTDP-N-acetylviosamine"
---

# dTDP-4-acetamido-4,6-dideoxy-D-glucose

`molecule.C06018`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06018`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dTDP-4-acetamido-4,6-dideoxy-D-glucose; dTDP-4-acetamido-4,6-dideoxy-alpha-D-glucose; dTDP-N-acetylviosamine EcoCyc common name: dTDP-4-acetamido-α-D-fucose. CPD-15611 "4-acetamido-4,6-dideoxy-α-D-galactose" (N-acetylthomosamine) is found in the enterobacterial common antigen (ECA) where its synthesis pathway has been elucidated.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: dTDP-4-acetamido-4,6-dideoxy-D-glucose; dTDP-4-acetamido-4,6-dideoxy-alpha-D-glucose; dTDP-N-acetylviosamine

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.TDPFUCACTRANS-RXN|reaction.ecocyc.TDPFUCACTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.FUC4NACTRANS-RXN|reaction.ecocyc.FUC4NACTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06018`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
