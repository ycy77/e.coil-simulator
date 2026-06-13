---
entity_id: "protein.P10371"
entity_type: "protein"
name: "hisA"
source_database: "UniProt"
source_id: "P10371"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hisA b2024 JW2006"
---

# hisA

`protein.P10371`

## Static

- Type: `protein`
- Source: `UniProt:P10371`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase (EC 5.3.1.16) (Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase) N-(5'-phospho-L-ribosyl-formimino)-5-amino-1-(5'-phosphoribosyl)-4-imidazolecarboxamide isomerase (HisA) carries out the fourth step in histidine biosynthesis. HisA catalyzes an internal redox reaction known as an Amadori rearrangement . Spontaneous hisA mutants were investigated .

## Biological Role

Catalyzes N-(5'-phospho-D-ribosylformimino)-5-amino-1- (5''-phospho-D-ribosyl)-4-imidazolecarboxamide ketol-isomerase; (reaction.R04640), PRIBFAICARPISOM-RXN (reaction.ecocyc.PRIBFAICARPISOM-RXN).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase (EC 5.3.1.16) (Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase)

## Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R04640|reaction.R04640]] `KEGG` `database` - via EC:5.3.1.16
- `catalyzes` --> [[reaction.ecocyc.PRIBFAICARPISOM-RXN|reaction.ecocyc.PRIBFAICARPISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2024|gene.b2024]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10371`
- `KEGG:ecj:JW2006;eco:b2024;ecoc:C3026_11410;`
- `GeneID:946521;`
- `GO:GO:0000105; GO:0003949; GO:0005829; GO:0006974`
- `EC:5.3.1.16`

## Notes

1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase (EC 5.3.1.16) (Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase)
