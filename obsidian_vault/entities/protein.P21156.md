---
entity_id: "protein.P21156"
entity_type: "protein"
name: "cysD"
source_database: "UniProt"
source_id: "P21156"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysD b2752 JW2722"
---

# cysD

`protein.P21156`

## Static

- Type: `protein`
- Source: `UniProt:P21156`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: With CysN forms the ATP sulfurylase (ATPS) that catalyzes the adenylation of sulfate producing adenosine 5'-phosphosulfate (APS) and diphosphate, the first enzymatic step in sulfur assimilation pathway. APS synthesis involves the formation of a high-energy phosphoric-sulfuric acid anhydride bond driven by GTP hydrolysis by CysN coupled to ATP hydrolysis by CysD. {ECO:0000255|HAMAP-Rule:MF_00064, ECO:0000269|PubMed:2828368, ECO:0000269|PubMed:8003495}. CysD along with CysN are the two subunits which form sulfate adenylyltransferase . This enzyme is involved in the assimilation of sulfate and catalyzes two reactions, GTP hydrolysis and activation of intracellular sulfate to APS (APS) which generates a sulfate-phosphate anhydride linkage. This linkage facilitates an energetically-downhill entry into the subsequent metabolic fates of reduction and group transfer. The rate of APS formation is enhanced by both a protein activator and by GTP hydrolysis . Mutations in the cysD gene prevent the anabolic utilization of sulfate . cysD, along with cysN and cysC, resides in the sulfate activation operon . cysD belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 . cysD as well as other genes involved in sulfur metabolism was significantly upregulated in a MG1655 lysogen carrying the Stx2a phage PA8...

## Biological Role

Catalyzes ATP:sulfate adenylyltransferase (reaction.R00529). Component of sulfate adenylyltransferase (complex.ecocyc.SULFATE-ADENYLYLTRANS-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Annotation

FUNCTION: With CysN forms the ATP sulfurylase (ATPS) that catalyzes the adenylation of sulfate producing adenosine 5'-phosphosulfate (APS) and diphosphate, the first enzymatic step in sulfur assimilation pathway. APS synthesis involves the formation of a high-energy phosphoric-sulfuric acid anhydride bond driven by GTP hydrolysis by CysN coupled to ATP hydrolysis by CysD. {ECO:0000255|HAMAP-Rule:MF_00064, ECO:0000269|PubMed:2828368, ECO:0000269|PubMed:8003495}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00529|reaction.R00529]] `KEGG` `database` - via EC:2.7.7.4
- `is_component_of` --> [[complex.ecocyc.SULFATE-ADENYLYLTRANS-CPLX|complex.ecocyc.SULFATE-ADENYLYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2752|gene.b2752]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21156`
- `KEGG:ecj:JW2722;eco:b2752;ecoc:C3026_15130;`
- `GeneID:93779254;947217;`
- `GO:GO:0000103; GO:0004781; GO:0005524; GO:0006790; GO:0006979; GO:0009336; GO:0034599; GO:0070814`
- `EC:2.7.7.4`

## Notes

Sulfate adenylyltransferase subunit 2 (EC 2.7.7.4) (ATP-sulfurylase small subunit) (Sulfate adenylate transferase) (SAT)
