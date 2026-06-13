---
entity_id: "molecule.C01146"
entity_type: "small_molecule"
name: "2-Hydroxy-3-oxopropanoate"
source_database: "KEGG"
source_id: "C01146"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Hydroxy-3-oxopropanoate"
  - "Tartronate semialdehyde"
---

# 2-Hydroxy-3-oxopropanoate

`molecule.C01146`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01146`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Hydroxy-3-oxopropanoate; Tartronate semialdehyde EcoCyc common name: tartronate semialdehyde.

## Biological Role

Produced in 4 reaction(s).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Annotation

KEGG compound: 2-Hydroxy-3-oxopropanoate; Tartronate semialdehyde

## Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R00013|reaction.R00013]] `KEGG` `database` - 2 C00048 <=> C01146 + C00011
- `is_product_of` --> [[reaction.R01745|reaction.R01745]] `KEGG` `database` - C00258 + C00003 <=> C01146 + C00004 + C00080
- `is_product_of` --> [[reaction.R01747|reaction.R01747]] `KEGG` `database` - C00258 + C00006 <=> C01146 + C00005 + C00080
- `is_product_of` --> [[reaction.ecocyc.RXN0-305|reaction.ecocyc.RXN0-305]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01146`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
