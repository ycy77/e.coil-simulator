---
entity_id: "molecule.C00536"
entity_type: "small_molecule"
name: "Triphosphate"
source_database: "KEGG"
source_id: "C00536"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Triphosphate"
  - "Triphosphoric acid"
  - "Tripolyphosphate"
  - "Inorganic triphosphate"
---

# Triphosphate

`molecule.C00536`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00536`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Triphosphate; Triphosphoric acid; Tripolyphosphate; Inorganic triphosphate

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 7 reaction(s).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)

## Annotation

KEGG compound: Triphosphate; Triphosphoric acid; Tripolyphosphate; Inorganic triphosphate

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)

## Outgoing Edges (10)

- `is_product_of` --> [[reaction.R07268|reaction.R07268]] `KEGG` `database` - C00002 + C05774 <=> C00536 + C06508
- `is_product_of` --> [[reaction.R12183|reaction.R12183]] `KEGG` `database` - 2 C00002 + 2 C00541 + C03024 <=> 2 C00536 + 2 C00194 + C03161
- `is_product_of` --> [[reaction.ecocyc.BTUR2-RXN|reaction.ecocyc.BTUR2-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.COBALADENOSYLTRANS-RXN|reaction.ecocyc.COBALADENOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DGTPTRIPHYDRO-RXN|reaction.ecocyc.DGTPTRIPHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19343|reaction.ecocyc.RXN-19343]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5507|reaction.ecocyc.RXN0-5507]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00138|reaction.R00138]] `KEGG` `database` - C00536 + C00001 <=> C00013 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.TRIPHOSPHATASE-RXN|reaction.ecocyc.TRIPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.S-ADENMETSYN-RXN|reaction.ecocyc.S-ADENMETSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00536`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
