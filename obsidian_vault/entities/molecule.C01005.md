---
entity_id: "molecule.C01005"
entity_type: "small_molecule"
name: "O-Phospho-L-serine"
source_database: "KEGG"
source_id: "C01005"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "O-Phospho-L-serine"
  - "L-O-Phosphoserine"
  - "3-Phosphoserine"
  - "Dexfosfoserine"
  - "3-Phospho-L-serine"
---

# O-Phospho-L-serine

`molecule.C01005`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01005`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: O-Phospho-L-serine; L-O-Phosphoserine; 3-Phosphoserine; Dexfosfoserine; 3-Phospho-L-serine

## Biological Role

Consumed as substrate in 4 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

KEGG compound: O-Phospho-L-serine; L-O-Phosphoserine; 3-Phosphoserine; Dexfosfoserine; 3-Phospho-L-serine

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (5)

- `is_substrate_of` --> [[reaction.R00582|reaction.R00582]] `KEGG` `database` - C01005 + C00001 <=> C00065 + C00009
- `is_substrate_of` --> [[reaction.R07274|reaction.R07274]] `KEGG` `database` - C01005 + C00283 <=> C00097 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.PSERTRANSAM-RXN|reaction.ecocyc.PSERTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5114|reaction.ecocyc.RXN0-5114]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ORNDECARBOX-RXN|reaction.ecocyc.ORNDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01005`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
