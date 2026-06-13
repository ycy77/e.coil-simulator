---
entity_id: "protein.P76387"
entity_type: "protein"
name: "wzc"
source_database: "UniProt"
source_id: "P76387"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wzc b2060 JW2045"
---

# wzc

`protein.P76387`

## Static

- Type: `protein`
- Source: `UniProt:P76387`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Required for the extracellular polysaccharide colanic acid synthesis. The autophosphorylated form is inactive. Probably involved in the export of colanic acid from the cell to medium. Phosphorylates udg. {ECO:0000269|PubMed:12851388}. The G7105 gene encodes a bacterial tyrosine (BY) kinase that regulates production of the extracellular polysaccharide CPD-21504 "colanic acid" (CA). Purified Wzc, incubated in the presence of ATP, autophosphorylates on a tyrosine residue; phosphorylated Wzc is dephosphorylated by G7106-MONOMER Wzb . Wzc-autophosphorylation negatively regulates colanic acid biosynthesis, and Wzb phosphatase activity counteracts this negative regulation . Both the phosphorylated and nonphosphorylated forms of Wzc are required for wild-type synthesis of CA in a CA-producing K-12 strain; Wzc phosphorylation influences the size distribution of CA; Wzc has an ATPase activity in addition to its kinase activity . Wzc also catalyzes tyrosine phosphorylation of UGD-MONOMER (Ugd) and this phosphorylation stimulates Ugd activity...

## Biological Role

Catalyzes RXN-24992 (reaction.ecocyc.RXN-24992). Component of polysaccharide export complex (complex.ecocyc.CPLX0-7529).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Required for the extracellular polysaccharide colanic acid synthesis. The autophosphorylated form is inactive. Probably involved in the export of colanic acid from the cell to medium. Phosphorylates udg. {ECO:0000269|PubMed:12851388}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-24992|reaction.ecocyc.RXN-24992]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-7529|complex.ecocyc.CPLX0-7529]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2060|gene.b2060]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76387`
- `KEGG:ecj:JW2045;eco:b2060;ecoc:C3026_11590;`
- `GeneID:946567;`
- `GO:GO:0000271; GO:0004713; GO:0005524; GO:0005886; GO:0009242; GO:0016887; GO:0042802`
- `EC:2.7.10.-`

## Notes

Tyrosine-protein kinase wzc (EC 2.7.10.-)
