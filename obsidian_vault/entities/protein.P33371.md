---
entity_id: "protein.P33371"
entity_type: "protein"
name: "dusC"
source_database: "UniProt"
source_id: "P33371"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dusC yohI b2140 JW2128"
---

# dusC

`protein.P33371`

## Static

- Type: `protein`
- Source: `UniProt:P33371`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the synthesis of 5,6-dihydrouridine (D), a modified base found in the D-loop of most tRNAs, via the reduction of the C5-C6 double bond in target uridines. DusC specifically modifies U16 in tRNAs. {ECO:0000255|HAMAP-Rule:MF_02043, ECO:0000269|PubMed:11983710, ECO:0000269|PubMed:25902496}. EG11311-MONOMER (DusB) and DusC together account for about half of the 5,6-dihydrouridine modification observed in wild-type cellular tRNA, and EG11932-MONOMER (DusA) accounts for the other half . DusC specifically modifies U16 of the D loop in tRNAs. The site selectivity of the enzyme is conveyed by binding the tRNA substrate in a different orientation when compared to an enzyme that modifies U20, on the opposite side of the D loop . Crystal structures of DusC have been solved, showing an N-terminal catalytic TIM-barrel domain and a C-terminal tRNA binding domain . Crystal structures of DusC in complex with tRNAs elucidated the basis for modification site specificity of the enzyme . A dusA dusB dusC triple mutant exhibits a complete lack of 5,6-dihydrouridine modification in cellular tRNA, whereas each single mutant exhibits a partial reduction, compared to wild type . A G7297 tmcA dusC double deletion strain has a severe cold-sensitive growth defect . Using a ΔdusC mutant, the specificity of DusC for dihydrouridylation of nucleotide 16 was confirmed for LEU-tRNAs (CAG)...

## Biological Role

Catalyzes dihydrouridine synthase (reaction.ecocyc.RXN0-1281).

## Annotation

FUNCTION: Catalyzes the synthesis of 5,6-dihydrouridine (D), a modified base found in the D-loop of most tRNAs, via the reduction of the C5-C6 double bond in target uridines. DusC specifically modifies U16 in tRNAs. {ECO:0000255|HAMAP-Rule:MF_02043, ECO:0000269|PubMed:11983710, ECO:0000269|PubMed:25902496}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1281|reaction.ecocyc.RXN0-1281]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2140|gene.b2140]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33371`
- `KEGG:ecj:JW2128;eco:b2140;ecoc:C3026_11995;`
- `GeneID:945458;`
- `GO:GO:0000049; GO:0002943; GO:0010181; GO:0017150; GO:0050660; GO:0071461; GO:0102262`
- `EC:1.3.1.-`

## Notes

tRNA-dihydrouridine(16) synthase (EC 1.3.1.-) (U16-specific dihydrouridine synthase) (U16-specific Dus) (tRNA-dihydrouridine synthase C)
