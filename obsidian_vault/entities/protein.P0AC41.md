---
entity_id: "protein.P0AC41"
entity_type: "protein"
name: "sdhA"
source_database: "UniProt"
source_id: "P0AC41"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:12560550, ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:12560550, ECO:0000269|PubMed:16079137}; Cytoplasmic side {ECO:0000269|PubMed:12560550, ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sdhA b0723 JW0713"
---

# sdhA

`protein.P0AC41`

## Static

- Type: `protein`
- Source: `UniProt:P0AC41`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:12560550, ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:12560550, ECO:0000269|PubMed:16079137}; Cytoplasmic side {ECO:0000269|PubMed:12560550, ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Two distinct, membrane-bound, FAD-containing enzymes are responsible for the catalysis of fumarate and succinate interconversion; the fumarate reductase is used in anaerobic growth, and the succinate dehydrogenase is used in aerobic growth. {ECO:0000269|PubMed:24374335, ECO:0000305|PubMed:12560550, ECO:0000305|PubMed:16407191, ECO:0000305|PubMed:19710024}. This is one of two catalytic subunits in the four subunit succinate dehydrogenase (SQR) enzyme. This subunit contains the FAD cofactor and the substrate-binding site . The redox potential of SdhA-bound FAD cofactor is -55.5 mV . Succinate, fumarate, citrate, and isocitrate appear to cause increased flavinylation of overproduced SdhA in cell extracts, indicating the existence of an activation mechanism involving TCA cycle intermediates . This protein has similarity to the FrdA subunit of fumarate reductase . A 2.2 Å crystal structure of L-aspartate oxidase suggests that an unusual tertiary structure is shared by L-aspartate oxidase, the SdhA subunit of succinate dehydrogenase, and the FrdA subunit of fumarate reductase . SdhA may play a role in bacteriophage T4 infection .

## Biological Role

Component of succinate:quinone oxidoreductase (complex.ecocyc.CPLX0-8160), succinate:quinone oxidoreductase subcomplex (complex.ecocyc.SUCC-DEHASE).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Two distinct, membrane-bound, FAD-containing enzymes are responsible for the catalysis of fumarate and succinate interconversion; the fumarate reductase is used in anaerobic growth, and the succinate dehydrogenase is used in aerobic growth. {ECO:0000269|PubMed:24374335, ECO:0000305|PubMed:12560550, ECO:0000305|PubMed:16407191, ECO:0000305|PubMed:19710024}.

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8160|complex.ecocyc.CPLX0-8160]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.SUCC-DEHASE|complex.ecocyc.SUCC-DEHASE]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0723|gene.b0723]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC41`
- `KEGG:ecj:JW0713;eco:b0723;ecoc:C3026_03620;`
- `GeneID:93776761;945402;`
- `GO:GO:0000104; GO:0005886; GO:0006099; GO:0008177; GO:0009055; GO:0009060; GO:0009061; GO:0016020; GO:0019646; GO:0045273; GO:0050660`
- `EC:1.3.5.1`

## Notes

Succinate dehydrogenase flavoprotein subunit (EC 1.3.5.1)
