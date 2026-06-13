---
entity_id: "molecule.C00362"
entity_type: "small_molecule"
name: "dGMP"
source_database: "KEGG"
source_id: "C00362"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dGMP"
  - "2'-Deoxyguanosine 5'-monophosphate"
  - "2'-Deoxyguanosine 5'-phosphate"
  - "Deoxyguanylic acid"
  - "Deoxyguanosine monophosphate"
---

# dGMP

`molecule.C00362`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00362`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dGMP; 2'-Deoxyguanosine 5'-monophosphate; 2'-Deoxyguanosine 5'-phosphate; Deoxyguanylic acid; Deoxyguanosine monophosphate

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: dGMP; 2'-Deoxyguanosine 5'-monophosphate; 2'-Deoxyguanosine 5'-phosphate; Deoxyguanylic acid; Deoxyguanosine monophosphate

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN0-385|reaction.ecocyc.RXN0-385]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GMKALT-RXN|reaction.ecocyc.GMKALT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14142|reaction.ecocyc.RXN-14142]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00362`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
