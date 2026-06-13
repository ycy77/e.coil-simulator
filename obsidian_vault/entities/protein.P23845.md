---
entity_id: "protein.P23845"
entity_type: "protein"
name: "cysN"
source_database: "UniProt"
source_id: "P23845"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysN b2751 JW2721"
---

# cysN

`protein.P23845`

## Static

- Type: `protein`
- Source: `UniProt:P23845`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: With CysD forms the ATP sulfurylase (ATPS) that catalyzes the adenylation of sulfate producing adenosine 5'-phosphosulfate (APS) and diphosphate, the first enzymatic step in sulfur assimilation pathway. APS synthesis involves the formation of a high-energy phosphoric-sulfuric acid anhydride bond driven by GTP hydrolysis by CysN coupled to ATP hydrolysis by CysD. {ECO:0000255|HAMAP-Rule:MF_00062, ECO:0000269|PubMed:2828368, ECO:0000269|PubMed:8003495}. CysN along with CysD are the two subunits which form sulfate adenylyltransferase . CysN contains a GTP-binding consensus sequence and stimulates the synthesis of APS (APS) by a GTPase mechanism . Sulfate adenylyltransferase is involved in the assimilation of sulfate and catalyzes two reactions, GTP hydrolysis and activation of intracellular sulfate to APS which generates a sulfate-phosphate anhydride linkage. This linkage facilitates an energetically-downhill entry into the subsequent metabolic fates of reduction and group transfer. The rate of APS formation is enhanced by both a protein activator and by GTP hydrolysis . Disruption of the cysN gene prevents sulfate activation and decreases expression of the downstream cysC gene . cysN, along with cysD and cysC, resides in the sulfate activation operon .

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

FUNCTION: With CysD forms the ATP sulfurylase (ATPS) that catalyzes the adenylation of sulfate producing adenosine 5'-phosphosulfate (APS) and diphosphate, the first enzymatic step in sulfur assimilation pathway. APS synthesis involves the formation of a high-energy phosphoric-sulfuric acid anhydride bond driven by GTP hydrolysis by CysN coupled to ATP hydrolysis by CysD. {ECO:0000255|HAMAP-Rule:MF_00062, ECO:0000269|PubMed:2828368, ECO:0000269|PubMed:8003495}.

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

- `encodes` <-- [[gene.b2751|gene.b2751]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23845`
- `KEGG:ecj:JW2721;eco:b2751;ecoc:C3026_15125;`
- `GeneID:93779255;947219;`
- `GO:GO:0000103; GO:0003924; GO:0004781; GO:0005524; GO:0005525; GO:0006790; GO:0009336; GO:0070814`
- `EC:2.7.7.4`

## Notes

Sulfate adenylyltransferase subunit 1 (EC 2.7.7.4) (ATP-sulfurylase large subunit) (Sulfate adenylate transferase) (SAT)
