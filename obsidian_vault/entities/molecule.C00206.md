---
entity_id: "molecule.C00206"
entity_type: "small_molecule"
name: "dADP"
source_database: "KEGG"
source_id: "C00206"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dADP"
  - "2'-Deoxyadenosine 5'-diphosphate"
---

# dADP

`molecule.C00206`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00206`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dADP; 2'-Deoxyadenosine 5'-diphosphate

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: dADP; 2'-Deoxyadenosine 5'-diphosphate

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (7)

- `activates` --> [[reaction.ecocyc.THYKI-RXN|reaction.ecocyc.THYKI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R01138|reaction.R01138]] `KEGG` `database` - C00131 + C00022 <=> C00206 + C00074
- `is_substrate_of` --> [[reaction.R01137|reaction.R01137]] `KEGG` `database` - C00002 + C00206 <=> C00008 + C00131
- `is_substrate_of` --> [[reaction.ecocyc.ADPREDUCT-RXN|reaction.ecocyc.ADPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DADPKIN-RXN|reaction.ecocyc.DADPKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-747|reaction.ecocyc.RXN0-747]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ADENPRIBOSYLTRAN-RXN|reaction.ecocyc.ADENPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00206`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
