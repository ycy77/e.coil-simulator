---
entity_id: "molecule.C00301"
entity_type: "small_molecule"
name: "ADP-ribose"
source_database: "KEGG"
source_id: "C00301"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "ADP-ribose"
  - "ADP-D-ribose"
  - "Adenosine diphosphate ribose"
---

# ADP-ribose

`molecule.C00301`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00301`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: ADP-ribose; ADP-D-ribose; Adenosine diphosphate ribose EcoCyc common name: ADP-D-ribose.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: ADP-ribose; ADP-D-ribose; Adenosine diphosphate ribose

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (6)

- `activates` --> [[reaction.ecocyc.CITSYN-RXN|reaction.ecocyc.CITSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.RXN-13859|reaction.ecocyc.RXN-13859]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7013|reaction.ecocyc.RXN0-7013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1441|reaction.ecocyc.RXN0-1441]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ACETALD-DEHYDROG-RXN|reaction.ecocyc.ACETALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ALCOHOL-DEHYDROG-RXN|reaction.ecocyc.ALCOHOL-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00301`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
