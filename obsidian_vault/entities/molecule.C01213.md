---
entity_id: "molecule.C01213"
entity_type: "small_molecule"
name: "(R)-Methylmalonyl-CoA"
source_database: "KEGG"
source_id: "C01213"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(R)-Methylmalonyl-CoA"
  - "L-Methylmalonyl-CoA"
---

# (R)-Methylmalonyl-CoA

`molecule.C01213`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01213`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (R)-Methylmalonyl-CoA; L-Methylmalonyl-CoA

## Biological Role

Consumed as substrate in 4 reaction(s).

## Enriched Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)

## Annotation

KEGG compound: (R)-Methylmalonyl-CoA; L-Methylmalonyl-CoA

## Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)

## Outgoing Edges (4)

- `is_substrate_of` --> [[reaction.R00833|reaction.R00833]] `KEGG` `database` - C01213 <=> C00091
- `is_substrate_of` --> [[reaction.ecocyc.METHYLMALONYL-COA-EPIM-RXN|reaction.ecocyc.METHYLMALONYL-COA-EPIM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.METHYLMALONYL-COA-MUT-RXN|reaction.ecocyc.METHYLMALONYL-COA-MUT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-310|reaction.ecocyc.RXN0-310]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01213`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
