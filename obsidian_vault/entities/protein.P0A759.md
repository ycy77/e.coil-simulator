---
entity_id: "protein.P0A759"
entity_type: "protein"
name: "nagB"
source_database: "UniProt"
source_id: "P0A759"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nagB glmD b0678 JW0664"
---

# nagB

`protein.P0A759`

## Static

- Type: `protein`
- Source: `UniProt:P0A759`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible isomerization-deamination of glucosamine 6-phosphate (GlcN6P) to form fructose 6-phosphate (Fru6P) and ammonium ion. {ECO:0000269|PubMed:1734962, ECO:0000269|PubMed:2821923}. Glucosamine-6-phosphate deaminase (NagB) catalyzes the second cytoplasmic reaction in the metabolism of N-acetyl-D-glucosamine. The deamination of glucosamine-6-phosphate generates ammonia and fructose-6-phosphate, which can enter glycolysis directly. Both N-acetylglucosamine and glucosamine can serve as the sole source of carbon for E. coli. Utilization of several amino sugars as carbon sources converges on NagB; additionally, NagB activity needs to be regulated to avoid a futile cycle with L-GLN-FRUCT-6-P-AMINOTRANS-MONOMER GlmS. It is therefore not surprising that a number of regulators have been identified to date. The first to be identified was the compound N-acetyl-D-glucosamine-6-phosphate (GlcNAc6P), which allosterically activates NagB . Both substrate binding and the allosteric transition are entropy-driven processes . However, the growth rate on glucosamine is limited by the supply of substrate to NagB rather than the absence of GlcNAc6P . Replacement of NagB with an orthologous enzyme that is not allosterically regulated has surprisingly little effect on the growth rate or fitness of E...

## Biological Role

Catalyzes D-glucosamine-6-phosphate aminohydrolase (ketol isomerizing); (reaction.R00765). Component of glucosamine-6-phosphate deaminase (complex.ecocyc.GLUCOSAMINE-6-P-DEAMIN-CPLX).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible isomerization-deamination of glucosamine 6-phosphate (GlcN6P) to form fructose 6-phosphate (Fru6P) and ammonium ion. {ECO:0000269|PubMed:1734962, ECO:0000269|PubMed:2821923}.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00765|reaction.R00765]] `KEGG` `database` - via EC:3.5.99.6
- `is_component_of` --> [[complex.ecocyc.GLUCOSAMINE-6-P-DEAMIN-CPLX|complex.ecocyc.GLUCOSAMINE-6-P-DEAMIN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0678|gene.b0678]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A759`
- `KEGG:ecj:JW0664;eco:b0678;ecoc:C3026_03370;`
- `GeneID:86863185;93776807;945290;`
- `GO:GO:0004342; GO:0005737; GO:0005829; GO:0005975; GO:0006043; GO:0006046; GO:0006048; GO:0019262; GO:0042802`
- `EC:3.5.99.6`

## Notes

Glucosamine-6-phosphate deaminase (EC 3.5.99.6) (GlcN6P deaminase) (GNPDA) (Glucosamine-6-phosphate isomerase)
