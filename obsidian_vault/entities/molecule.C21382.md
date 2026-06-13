---
entity_id: "molecule.C21382"
entity_type: "small_molecule"
name: "R-THMF"
source_database: "KEGG"
source_id: "C21382"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "R-THMF"
  - "(2R,4S)-2-Methyl-2,3,3,4-tetrahydroxytetrahydrofuran"
---

# R-THMF

`molecule.C21382`

## Static

- Type: `small_molecule`
- Source: `KEGG:C21382`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: R-THMF; (2R,4S)-2-Methyl-2,3,3,4-tetrahydroxytetrahydrofuran EcoCyc common name: autoinducer 2.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

KEGG compound: R-THMF; (2R,4S)-2-Methyl-2,3,3,4-tetrahydroxytetrahydrofuran

## Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (6)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8088|complex.ecocyc.CPLX0-8088]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.RXN-10017|reaction.ecocyc.RXN-10017]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-453|reaction.ecocyc.TRANS-RXN0-453]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-454|reaction.ecocyc.TRANS-RXN0-454]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-453|reaction.ecocyc.TRANS-RXN0-453]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-454|reaction.ecocyc.TRANS-RXN0-454]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C21382`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
