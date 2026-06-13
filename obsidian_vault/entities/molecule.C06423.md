---
entity_id: "molecule.C06423"
entity_type: "small_molecule"
name: "Octanoic acid"
source_database: "KEGG"
source_id: "C06423"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Octanoic acid"
  - "Caprylic acid"
  - "Octylic acid"
  - "Octanoate"
---

# Octanoic acid

`molecule.C06423`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06423`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Octanoic acid; Caprylic acid; Octylic acid; Octanoate EcoCyc common name: octanoate.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Annotation

KEGG compound: Octanoic acid; Caprylic acid; Octylic acid; Octanoate

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-272|reaction.ecocyc.TRANS-RXN0-272]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-5741|reaction.ecocyc.RXN-5741]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5098|reaction.ecocyc.RXN0-5098]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7423|reaction.ecocyc.RXN0-7423]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-272|reaction.ecocyc.TRANS-RXN0-272]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06423`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
