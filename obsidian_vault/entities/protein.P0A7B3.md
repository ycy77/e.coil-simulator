---
entity_id: "protein.P0A7B3"
entity_type: "protein"
name: "nadK"
source_database: "UniProt"
source_id: "P0A7B3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00361}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nadK yfjB yfjE b2615 JW2596"
---

# nadK

`protein.P0A7B3`

## Static

- Type: `protein`
- Source: `UniProt:P0A7B3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00361}.

## Enriched Summary

FUNCTION: Involved in the regulation of the intracellular balance of NAD and NADP, and is a key enzyme in the biosynthesis of NADP. Catalyzes specifically the phosphorylation on 2'-hydroxyl of the adenosine moiety of NAD to yield NADP. It can use ATP and other nucleoside triphosphates (UTP, CTP, GTP, dATP, TTP) as phosphoryl donors, while nucleoside mono- or diphosphates and poly(P) cannot. {ECO:0000255|HAMAP-Rule:MF_00361, ECO:0000269|PubMed:11488932, ECO:0000269|PubMed:15855156, ECO:0000269|PubMed:3025169}. NAD kinase appears to be an allosteric enzyme, with activity tightly coupled to the NADPH/NADP+ and NADH/NAD+ ratios present in the cell. That suggests that NAD kinase may play an important role in the regulation of NADP turnover and size of the NADP pool . nadK is likely essential for growth . Site-directed mutagenesis studies of the E. coli enzyme showed that a R175G mutation relaxed the strict NAD substrate specificity of the enzyme, resulting in a low level of ATP-dependent NADH kinase activity . Structure-function relationships in NAD kinases from archaea, bacteria (including E. coli) and eukaryotes have been reviewed .

## Biological Role

Catalyzes ATP:NAD+ 2'-phosphotransferase (reaction.R00104). Component of NAD kinase (complex.ecocyc.CPLX0-682).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Involved in the regulation of the intracellular balance of NAD and NADP, and is a key enzyme in the biosynthesis of NADP. Catalyzes specifically the phosphorylation on 2'-hydroxyl of the adenosine moiety of NAD to yield NADP. It can use ATP and other nucleoside triphosphates (UTP, CTP, GTP, dATP, TTP) as phosphoryl donors, while nucleoside mono- or diphosphates and poly(P) cannot. {ECO:0000255|HAMAP-Rule:MF_00361, ECO:0000269|PubMed:11488932, ECO:0000269|PubMed:15855156, ECO:0000269|PubMed:3025169}.

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00104|reaction.R00104]] `KEGG` `database` - via EC:2.7.1.23
- `is_component_of` --> [[complex.ecocyc.CPLX0-682|complex.ecocyc.CPLX0-682]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2615|gene.b2615]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7B3`
- `KEGG:ecj:JW2596;eco:b2615;ecoc:C3026_14475;`
- `GeneID:86860736;93774464;947092;`
- `GO:GO:0003951; GO:0005524; GO:0005829; GO:0006741; GO:0019674; GO:0046872; GO:0051287`
- `EC:2.7.1.23`

## Notes

NAD kinase (EC 2.7.1.23) (ATP-dependent NAD kinase)
