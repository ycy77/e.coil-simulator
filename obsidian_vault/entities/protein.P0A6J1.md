---
entity_id: "protein.P0A6J1"
entity_type: "protein"
name: "cysC"
source_database: "UniProt"
source_id: "P0A6J1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysC b2750 JW2720"
---

# cysC

`protein.P0A6J1`

## Static

- Type: `protein`
- Source: `UniProt:P0A6J1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the synthesis of activated sulfate. Adenylylsulfate kinase (CysC) is involved in the assimilation of sulfate and catalyzes the phosphorylation of adenosine 5-phosphosulfate (APS) to yield 3-phosphoadenosine 5-phosphosulfate (PAPS). The enzyme picks up MgATP first then binds to the substrate indicating the reaction is ordered sequential . The enzyme exhibits a complex steady-state kinetic behavior, showing a variation of ping-pong to sequential pathways as the APS concentration increases . Serine-109 has been identified as the residue that is phosphorylated when incubated with ATP . The enzyme exists predominantly as a homodimer, but a tetrameric form exists when the enzyme is dephosphorylated . cysC, along with cysN and cysD, resides in the sulfate activation operon .

## Biological Role

Catalyzes ATP:adenylylsulfate 3'-phosphotransferase (reaction.R00509). Component of adenylyl-sulfate kinase (complex.ecocyc.ADENYLYLSULFKIN-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Annotation

FUNCTION: Catalyzes the synthesis of activated sulfate.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00509|reaction.R00509]] `KEGG` `database` - via EC:2.7.1.25
- `is_component_of` --> [[complex.ecocyc.ADENYLYLSULFKIN-CPLX|complex.ecocyc.ADENYLYLSULFKIN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2750|gene.b2750]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6J1`
- `KEGG:ecj:JW2720;eco:b2750;ecoc:C3026_15120;`
- `GeneID:93779256;947221;`
- `GO:GO:0000103; GO:0004020; GO:0005524; GO:0042802; GO:0070814`
- `EC:2.7.1.25`

## Notes

Adenylyl-sulfate kinase (EC 2.7.1.25) (APS kinase) (ATP adenosine-5'-phosphosulfate 3'-phosphotransferase) (Adenosine-5'-phosphosulfate kinase)
