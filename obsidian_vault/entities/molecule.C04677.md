---
entity_id: "molecule.C04677"
entity_type: "small_molecule"
name: "1-(5'-Phosphoribosyl)-5-amino-4-imidazolecarboxamide"
source_database: "KEGG"
source_id: "C04677"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "1-(5'-Phosphoribosyl)-5-amino-4-imidazolecarboxamide"
  - "5'-Phosphoribosyl-5-amino-4-imidazolecarboxamide"
  - "5'-Phospho-ribosyl-5-amino-4-imidazole carboxamide"
  - "AICAR"
  - "5-Aminoimidazole-4-carboxamide ribotide"
  - "5-Phosphoribosyl-4-carbamoyl-5-aminoimidazole"
  - "5-Amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxamide"
  - "5-Amino-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamide"
---

# 1-(5'-Phosphoribosyl)-5-amino-4-imidazolecarboxamide

`molecule.C04677`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04677`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 1-(5'-Phosphoribosyl)-5-amino-4-imidazolecarboxamide; 5'-Phosphoribosyl-5-amino-4-imidazolecarboxamide; 5'-Phospho-ribosyl-5-amino-4-imidazole carboxamide; AICAR; 5-Aminoimidazole-4-carboxamide ribotide; 5-Phosphoribosyl-4-carbamoyl-5-aminoimidazole; 5-Amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxamide; 5-Amino-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamide EcoCyc common name: 5-amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxamide.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00340` Histidine metabolism (KEGG)

## Annotation

KEGG compound: 1-(5'-Phosphoribosyl)-5-amino-4-imidazolecarboxamide; 5'-Phosphoribosyl-5-amino-4-imidazolecarboxamide; 5'-Phospho-ribosyl-5-amino-4-imidazole carboxamide; AICAR; 5-Aminoimidazole-4-carboxamide ribotide; 5-Phosphoribosyl-4-carbamoyl-5-aminoimidazole; 5-Amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxamide; 5-Amino-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamide

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00340` Histidine metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R12152|reaction.R12152]] `KEGG` `database` - C04916 + C00014 <=> C04677 + C04666 + C00001
- `is_product_of` --> [[reaction.ecocyc.AICARSYN-RXN|reaction.ecocyc.AICARSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUTAMIDOTRANS-RXN|reaction.ecocyc.GLUTAMIDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17900|reaction.ecocyc.RXN-17900]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.AICARTRANSFORM-RXN|reaction.ecocyc.AICARTRANSFORM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04677`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
