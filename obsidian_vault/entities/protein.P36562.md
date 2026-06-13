---
entity_id: "protein.P36562"
entity_type: "protein"
name: "cobT"
source_database: "UniProt"
source_id: "P36562"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cobT b1991 JW1969"
---

# cobT

`protein.P36562`

## Static

- Type: `protein`
- Source: `UniProt:P36562`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the synthesis of alpha-ribazole-5'-phosphate from nicotinate mononucleotide (NAMN) and 5,6-dimethylbenzimidazole (DMB). E. coli K-12, as well as natural isolates, can synthesize cobalamin only when supplied with the intermediate cobinamide . cobT encodes a predicted dimethylbenzimidazole phosphoribosyltransferase. In addition to its predicted phosphoribosyltransferase activity, it is likely that CobT also participates directly in the synthesis of DMB . Expression of the cobUST operon is induced by cobinamide .

## Biological Role

Catalyzes nicotinate-nucleotide:dimethylbenzimidazole phospho-D-ribosyltransferase (reaction.R04148). Component of nicotinate-nucleotide—dimethylbenzimidazole phosphoribosyltransferase (complex.ecocyc.DMBPPRIBOSYLTRANS-CPLX).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the synthesis of alpha-ribazole-5'-phosphate from nicotinate mononucleotide (NAMN) and 5,6-dimethylbenzimidazole (DMB).

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R04148|reaction.R04148]] `KEGG` `database` - via EC:2.4.2.21
- `is_component_of` --> [[complex.ecocyc.DMBPPRIBOSYLTRANS-CPLX|complex.ecocyc.DMBPPRIBOSYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1991|gene.b1991]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36562`
- `KEGG:ecj:JW1969;eco:b1991;ecoc:C3026_11235;`
- `GeneID:946517;`
- `GO:GO:0008939; GO:0009236`
- `EC:2.4.2.21`

## Notes

Nicotinate-nucleotide--dimethylbenzimidazole phosphoribosyltransferase (NN:DBI PRT) (EC 2.4.2.21) (N(1)-alpha-phosphoribosyltransferase)
