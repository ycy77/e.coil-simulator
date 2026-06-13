---
entity_id: "molecule.C00700"
entity_type: "small_molecule"
name: "XTP"
source_database: "KEGG"
source_id: "C00700"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "XTP"
  - "Xanthosine 5'-triphosphate"
---

# XTP

`molecule.C00700`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00700`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: XTP; Xanthosine 5'-triphosphate

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: XTP; Xanthosine 5'-triphosphate

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (4)

- `is_substrate_of` --> [[reaction.R12589|reaction.R12589]] `KEGG` `database` - C00700 + C00001 <=> C01337 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1603|reaction.ecocyc.RXN0-1603]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5074|reaction.ecocyc.RXN0-5074]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GTP-CYCLOHYDRO-II-RXN|reaction.ecocyc.GTP-CYCLOHYDRO-II-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00700`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
