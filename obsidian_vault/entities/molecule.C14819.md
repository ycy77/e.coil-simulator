---
entity_id: "molecule.C14819"
entity_type: "small_molecule"
name: "Fe3+"
source_database: "KEGG"
source_id: "C14819"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Fe3+"
  - "Fe(III)"
  - "Ferric ion"
  - "Iron(3+)"
---

# Fe3+

`molecule.C14819`

## Static

- Type: `small_molecule`
- Source: `KEGG:C14819`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Fe3+; Fe(III); Ferric ion; Iron(3+)

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s). Binds superoxide dismutase (Fe) (complex.ecocyc.SUPEROX-DISMUTFE-CPLX).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: Fe3+; Fe(III); Ferric ion; Iron(3+)

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (10)

- `activates` --> [[reaction.ecocyc.BASS-RXN|reaction.ecocyc.BASS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `activates` --> [[reaction.ecocyc.SAMDECARB-RXN|reaction.ecocyc.SAMDECARB-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `binds` --> [[complex.ecocyc.SUPEROX-DISMUTFE-CPLX|complex.ecocyc.SUPEROX-DISMUTFE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.R00078|reaction.R00078]] `KEGG` `database` - C00007 + 4 C14818 + 4 C00080 <=> 4 C14819 + 2 C00001
- `is_product_of` --> [[reaction.ecocyc.RXN-12540|reaction.ecocyc.RXN-12540]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1483|reaction.ecocyc.RXN0-1483]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12541|reaction.ecocyc.RXN-12541]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20002|reaction.ecocyc.RXN-20002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.D-PPENTOMUT-RXN|reaction.ecocyc.D-PPENTOMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.MANNOSE-ISOMERASE-RXN|reaction.ecocyc.MANNOSE-ISOMERASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C14819`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
