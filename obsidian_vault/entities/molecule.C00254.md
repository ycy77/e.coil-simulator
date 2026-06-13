---
entity_id: "molecule.C00254"
entity_type: "small_molecule"
name: "Prephenate"
source_database: "KEGG"
source_id: "C00254"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Prephenate"
  - "Prephenic acid"
---

# Prephenate

`molecule.C00254`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00254`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Prephenate; Prephenic acid

## Biological Role

Consumed as substrate in 9 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Annotation

KEGG compound: Prephenate; Prephenic acid

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Outgoing Edges (12)

- `is_product_of` --> [[reaction.R01731|reaction.R01731]] `KEGG` `database` - C00036 + C00826 <=> C00049 + C00254
- `is_product_of` --> [[reaction.ecocyc.CHORISMATEMUT-RXN|reaction.ecocyc.CHORISMATEMUT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01728|reaction.R01728]] `KEGG` `database` - C00254 + C00003 <=> C01179 + C00011 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.PREPHENATEDEHYDRAT-RXN|reaction.ecocyc.PREPHENATEDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PREPHENATEDEHYDROG-RXN|reaction.ecocyc.PREPHENATEDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21990|reaction.ecocyc.RXN-21990]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-24716|reaction.ecocyc.RXN-24716]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-24717|reaction.ecocyc.RXN-24717]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-24718|reaction.ecocyc.RXN-24718]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-24918|reaction.ecocyc.RXN-24918]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7066|reaction.ecocyc.RXN0-7066]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.CHORISMATEMUT-RXN|reaction.ecocyc.CHORISMATEMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00254`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
