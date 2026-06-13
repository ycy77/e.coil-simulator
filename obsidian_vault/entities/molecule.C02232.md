---
entity_id: "molecule.C02232"
entity_type: "small_molecule"
name: "3-Oxoadipyl-CoA"
source_database: "KEGG"
source_id: "C02232"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-Oxoadipyl-CoA"
  - "beta-Ketoadipyl-CoA"
---

# 3-Oxoadipyl-CoA

`molecule.C02232`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02232`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-Oxoadipyl-CoA; beta-Ketoadipyl-CoA EcoCyc common name: 3-oxoadipoyl-CoA.

## Biological Role

Produced in 4 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00930` Caprolactam degradation (KEGG)

## Annotation

KEGG compound: 3-Oxoadipyl-CoA; beta-Ketoadipyl-CoA

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00930` Caprolactam degradation (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R00829|reaction.R00829]] `KEGG` `database` - C00091 + C00024 <=> C00010 + C02232
- `is_product_of` --> [[reaction.R06941|reaction.R06941]] `KEGG` `database` - C14145 + C00003 <=> C02232 + C00004 + C00080
- `is_product_of` --> [[reaction.ecocyc.RXN-3641|reaction.ecocyc.RXN-3641]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-2044|reaction.ecocyc.RXN0-2044]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02232`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
