---
entity_id: "molecule.C03373"
entity_type: "small_molecule"
name: "Aminoimidazole ribotide"
source_database: "KEGG"
source_id: "C03373"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Aminoimidazole ribotide"
  - "AIR"
  - "1-(5'-Phosphoribosyl)-5-aminoimidazole"
  - "5'-Phosphoribosyl-5-aminoimidazole"
  - "1-(5-Phospho-D-ribosyl)-5-aminoimidazole"
  - "5-Amino-1-(5-phospho-D-ribosyl)imidazole"
  - "5-Amino-1-(5-phospho-beta-D-ribosyl)imidazole"
---

# Aminoimidazole ribotide

`molecule.C03373`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03373`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Aminoimidazole ribotide; AIR; 1-(5'-Phosphoribosyl)-5-aminoimidazole; 5'-Phosphoribosyl-5-aminoimidazole; 1-(5-Phospho-D-ribosyl)-5-aminoimidazole; 5-Amino-1-(5-phospho-D-ribosyl)imidazole; 5-Amino-1-(5-phospho-beta-D-ribosyl)imidazole EcoCyc common name: 5-amino-1-(5-phospho-β-D-ribosyl)imidazole. 5-PHOSPHORIBOSYL-5-AMINOIMIDAZOLE (AIR) is a key intermediate in the biosynthesis of Purine-Nucleotides "purine nocleotides" and THIAMINE.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: Aminoimidazole ribotide; AIR; 1-(5'-Phosphoribosyl)-5-aminoimidazole; 5'-Phosphoribosyl-5-aminoimidazole; 1-(5-Phospho-D-ribosyl)-5-aminoimidazole; 5-Amino-1-(5-phospho-D-ribosyl)imidazole; 5-Amino-1-(5-phospho-beta-D-ribosyl)imidazole

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.AIRS-RXN|reaction.ecocyc.AIRS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.PYRIMSYN1-RXN|reaction.ecocyc.PYRIMSYN1-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-742|reaction.ecocyc.RXN0-742]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.AIRS-RXN|reaction.ecocyc.AIRS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03373`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
