---
entity_id: "protein.P0AA84"
entity_type: "protein"
name: "clsB"
source_database: "UniProt"
source_id: "P0AA84"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305|PubMed:10634942}; Peripheral membrane protein {ECO:0000305|PubMed:10634942}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "clsB ybhO b0789 JW0772"
---

# clsB

`protein.P0AA84`

## Static

- Type: `protein`
- Source: `UniProt:P0AA84`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305|PubMed:10634942}; Peripheral membrane protein {ECO:0000305|PubMed:10634942}.

## Enriched Summary

FUNCTION: Catalyzes the phosphatidyl group transfer from one phosphatidylglycerol molecule to another to form cardiolipin (CL) (diphosphatidylglycerol) and glycerol. Can also catalyze phosphatidyl group transfer to water to form phosphatidate. {ECO:0000255|HAMAP-Rule:MF_01917, ECO:0000269|PubMed:10634942, ECO:0000269|PubMed:22988102}. ClsB is the second cardiolipin synthase in E. coli . Synthesis of cardiolipin during exponential growth is due to the activity of CARDIOLIPSYN-MONOMER ClsA, while all three cardiolipin synthases, ClsA, ClsB and G6551-MONOMER ClsC, contribute to cardiolipin synthesis in stationary phase . ClsB is able to catalyze synthesis of phosphatidylglycerol from phosphatidylethanolamine and glycerol and appears to be involved in the biosynthesis of 6-phosphatidyltrehalose and 6,6'-diphosphatidyltrehalose in certain E. coli strains . Cells with deletions of all three of the genes encoding cardiolipin synthases, ΔclsABC, completely lack cardiolipin . Upon overexpression of AtpF (as well as other membrane proteins), formation of intracellular membranes (ICMs) is observed; the inverted hexagonal phase of ICMs is absent in a ΔclsABC mutant, and thus requires cardiolipin . The effect of deletion and overexpression of clsB on lipid class distribution has been measured...

## Biological Role

Catalyzes CARDIOLIPSYN-RXN (reaction.ecocyc.CARDIOLIPSYN-RXN), RXN0-7272 (reaction.ecocyc.RXN0-7272).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphatidyl group transfer from one phosphatidylglycerol molecule to another to form cardiolipin (CL) (diphosphatidylglycerol) and glycerol. Can also catalyze phosphatidyl group transfer to water to form phosphatidate. {ECO:0000255|HAMAP-Rule:MF_01917, ECO:0000269|PubMed:10634942, ECO:0000269|PubMed:22988102}.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.CARDIOLIPSYN-RXN|reaction.ecocyc.CARDIOLIPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7272|reaction.ecocyc.RXN0-7272]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0789|gene.b0789]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA84`
- `KEGG:ecj:JW0772;eco:b0789;ecoc:C3026_04995;`
- `GeneID:75170854;75204904;945409;`
- `GO:GO:0004630; GO:0005886; GO:0008808; GO:0016020; GO:0032049`
- `EC:2.7.8.-`

## Notes

Cardiolipin synthase B (CL synthase) (EC 2.7.8.-)
