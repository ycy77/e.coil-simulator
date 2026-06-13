---
entity_id: "molecule.C00448"
entity_type: "small_molecule"
name: "trans,trans-Farnesyl diphosphate"
source_database: "KEGG"
source_id: "C00448"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "trans,trans-Farnesyl diphosphate"
  - "Farnesyl diphosphate"
  - "Farnesyl pyrophosphate"
  - "2-trans,6-trans-Farnesyl diphosphate"
  - "(2E,6E)-Farnesyl diphosphate"
---

# trans,trans-Farnesyl diphosphate

`molecule.C00448`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00448`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: trans,trans-Farnesyl diphosphate; Farnesyl diphosphate; Farnesyl pyrophosphate; 2-trans,6-trans-Farnesyl diphosphate; (2E,6E)-Farnesyl diphosphate EcoCyc common name: (2E,6E)-farnesyl diphosphate. For polyisoprenols and polyisoprenyl phosphates nomenclature, see Polyisoprenoids.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Annotation

KEGG compound: trans,trans-Farnesyl diphosphate; Farnesyl diphosphate; Farnesyl pyrophosphate; 2-trans,6-trans-Farnesyl diphosphate; (2E,6E)-Farnesyl diphosphate

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.FPPSYN-RXN|reaction.ecocyc.FPPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.HEMEOSYN-RXN|reaction.ecocyc.HEMEOSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11776|reaction.ecocyc.RXN-11776]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8992|reaction.ecocyc.RXN-8992]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8999|reaction.ecocyc.RXN-8999]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00448`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
