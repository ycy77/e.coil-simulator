---
entity_id: "molecule.C00361"
entity_type: "small_molecule"
name: "dGDP"
source_database: "KEGG"
source_id: "C00361"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dGDP"
  - "2'-Deoxyguanosine 5'-diphosphate"
---

# dGDP

`molecule.C00361`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00361`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dGDP; 2'-Deoxyguanosine 5'-diphosphate

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: dGDP; 2'-Deoxyguanosine 5'-diphosphate

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (5)

- `activates` --> [[reaction.ecocyc.THYKI-RXN|reaction.ecocyc.THYKI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.GMKALT-RXN|reaction.ecocyc.GMKALT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DGDPKIN-RXN|reaction.ecocyc.DGDPKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GDPREDUCT-RXN|reaction.ecocyc.GDPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-748|reaction.ecocyc.RXN0-748]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00361`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
