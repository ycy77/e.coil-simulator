---
entity_id: "molecule.C01031"
entity_type: "small_molecule"
name: "S-Formylglutathione"
source_database: "KEGG"
source_id: "C01031"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "S-Formylglutathione"
---

# S-Formylglutathione

`molecule.C01031`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01031`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: S-Formylglutathione

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)

## Annotation

KEGG compound: S-Formylglutathione

## Pathways

- `eco00680` Methane metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R06983|reaction.R06983]] `KEGG` `database` - C14180 + C00003 <=> C01031 + C00004 + C00080
- `is_product_of` --> [[reaction.ecocyc.RXN-2962|reaction.ecocyc.RXN-2962]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00527|reaction.R00527]] `KEGG` `database` - C01031 + C00001 <=> C00058 + C00051
- `is_substrate_of` --> [[reaction.ecocyc.S-FORMYLGLUTATHIONE-HYDROLASE-RXN|reaction.ecocyc.S-FORMYLGLUTATHIONE-HYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01031`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
