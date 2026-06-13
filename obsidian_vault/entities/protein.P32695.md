---
entity_id: "protein.P32695"
entity_type: "protein"
name: "dusA"
source_database: "UniProt"
source_id: "P32695"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dusA yjbN b4049 JW5950"
---

# dusA

`protein.P32695`

## Static

- Type: `protein`
- Source: `UniProt:P32695`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the synthesis of 5,6-dihydrouridine (D), a modified base found in the D-loop of most tRNAs, via the reduction of the C5-C6 double bond in target uridines. Specifically modifies U20 and U20a in tRNAs. {ECO:0000255|HAMAP-Rule:MF_02041, ECO:0000269|PubMed:11983710, ECO:0000269|PubMed:22123979, ECO:0000305|PubMed:25902496}. DusA accounts for about half of the 5,6-dihydrouridine modification observed in wild-type cellular tRNA; EG11311-MONOMER (DusB) and EG12022-MONOMER (DusC) together account for the other half. DusA is solely responsible for the 5,6-dihydrouridine modification observed in tRNA2fMet . A dusA dusB dusC triple mutant (Δ3) exhibits a complete lack of 5,6-dihydrouridine modification in cellular tRNA, whereas each single mutant exhibits a partial reduction, compared to wild type . Amino acids that are required for DusA activity have been identified . Using a ΔdusA mutant, the specificity of DusA for dihydrouridylation of nucleotide 20 and 20a was determined in ARG-tRNAs (ICG), ILE-tRNAs (GAU) and LEU-tRNAs (CAG) . Follow-up experiments with the Δ3 mutant found that mRNAs are not dihydrouridylated and that the dihydrouridine nucleotide in 23S rRNA is dihydrouridylated by some other dihydrouridine synthase than DusA, DusB or DusC...

## Biological Role

Catalyzes dihydrouridine synthase (reaction.ecocyc.RXN0-1281).

## Annotation

FUNCTION: Catalyzes the synthesis of 5,6-dihydrouridine (D), a modified base found in the D-loop of most tRNAs, via the reduction of the C5-C6 double bond in target uridines. Specifically modifies U20 and U20a in tRNAs. {ECO:0000255|HAMAP-Rule:MF_02041, ECO:0000269|PubMed:11983710, ECO:0000269|PubMed:22123979, ECO:0000305|PubMed:25902496}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1281|reaction.ecocyc.RXN0-1281]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4049|gene.b4049]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32695`
- `KEGG:ecj:JW5950;eco:b4049;`
- `GeneID:93777783;948558;`
- `GO:GO:0000049; GO:0002943; GO:0005829; GO:0010181; GO:0017150; GO:0050660; GO:0102264; GO:0102266`
- `EC:1.3.1.-; 1.3.1.91`

## Notes

tRNA-dihydrouridine(20/20a) synthase (EC 1.3.1.-) (EC 1.3.1.91) (U20-specific dihydrouridine synthase) (U20-specific Dus) (tRNA-dihydrouridine synthase A)
