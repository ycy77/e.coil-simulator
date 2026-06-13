---
entity_id: "molecule.C15809"
entity_type: "small_molecule"
name: "Iminoglycine"
source_database: "KEGG"
source_id: "C15809"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Iminoglycine"
  - "Iminoacetic acid"
  - "2-Iminoacetate"
---

# Iminoglycine

`molecule.C15809`

## Static

- Type: `small_molecule`
- Source: `KEGG:C15809`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Iminoglycine; Iminoacetic acid; 2-Iminoacetate EcoCyc common name: 2-iminoacetate.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)

## Annotation

KEGG compound: Iminoglycine; Iminoacetic acid; 2-Iminoacetate

## Pathways

- `eco00730` Thiamine metabolism (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.R10246|reaction.R10246]] `KEGG` `database` - C00082 + C00019 + C00030 <=> C15809 + C01468 + C05198 + C00073 + C00028
- `is_product_of` --> [[reaction.ecocyc.RXN-11319|reaction.ecocyc.RXN-11319]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R10247|reaction.R10247]] `KEGG` `database` - C11437 + C15809 + C15814 <=> C20246 + C15810 + 2 C00001
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13329|reaction.ecocyc.RXN-13329]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7196|reaction.ecocyc.RXN0-7196]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.THIAZOLSYN2-RXN|reaction.ecocyc.THIAZOLSYN2-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C15809`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
