---
entity_id: "molecule.C00237"
entity_type: "small_molecule"
name: "CO"
source_database: "KEGG"
source_id: "C00237"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "CO"
  - "Carbon monoxide"
---

# CO

`molecule.C00237`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00237`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: CO; Carbon monoxide EcoCyc common name: carbon monoxide.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: CO; Carbon monoxide

## Pathways

- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (9)

- `is_product_of` --> [[reaction.ecocyc.PYRIMSYN1-RXN|reaction.ecocyc.PYRIMSYN1-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.QUERCETIN-23-DIOXYGENASE-RXN|reaction.ecocyc.QUERCETIN-23-DIOXYGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-556|reaction.ecocyc.TRANS-RXN0-556]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-556|reaction.ecocyc.TRANS-RXN0-556]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.R621-RXN|reaction.ecocyc.R621-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5256|reaction.ecocyc.RXN0-5256]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5266|reaction.ecocyc.RXN0-5266]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5268|reaction.ecocyc.RXN0-5268]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-7399|reaction.ecocyc.RXN0-7399]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00237`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
