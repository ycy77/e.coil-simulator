---
entity_id: "protein.P0A7A7"
entity_type: "protein"
name: "plsB"
source_database: "UniProt"
source_id: "P0A7A7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16294310, ECO:0000269|PubMed:4943977}; Peripheral membrane protein {ECO:0000269|PubMed:16294310, ECO:0000269|PubMed:4943977}; Cytoplasmic side {ECO:0000269|PubMed:16294310, ECO:0000269|PubMed:4943977}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "plsB b4041 JW4001"
---

# plsB

`protein.P0A7A7`

## Static

- Type: `protein`
- Source: `UniProt:P0A7A7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16294310, ECO:0000269|PubMed:4943977}; Peripheral membrane protein {ECO:0000269|PubMed:16294310, ECO:0000269|PubMed:4943977}; Cytoplasmic side {ECO:0000269|PubMed:16294310, ECO:0000269|PubMed:4943977}.

## Enriched Summary

FUNCTION: Catalyzes the transfer of an acyl group from acyl-ACP to glycerol-3-phosphate (G3P) to form lysophosphatidic acid (LPA). This enzyme can utilize either acyl-CoA or acyl-ACP as the fatty acyl donor. {ECO:0000269|PubMed:17645809, ECO:0000269|PubMed:6997313}. Membrane-bound glycerol-3-phosphate acyltransferase (PlsB) catalyzes the first committed step in phospholipid biosynthesis and is thought to function in close proximity to the succeeding enzyme 1-ACYLGLYCEROL-3-P-ACYLTRANSFER-MONOMER (PlsC) . It is specific for acylation at position 1 of GLYCEROL-3P and can utilize either fatty acyl-acyl carrier protein (acyl-ACP) or fatty acyl-coenzyme A (acyl-CoA) thioesters as acyl donors to form ACYL-SN-GLYCEROL-3P. Fatty acids that are endogenously synthesized are attached to ACP and exogenously added fatty acids are attached to CoA . In E. coli phospholipids the sn 1 position is occupied mainly by either palmitate, or cis-vaccenate, whereas the sn 2 position is predominantly palmitoleate, or cis-vaccenate. This is thought to result from the substrate preferences of the PlsB and PlsC enzymes . The plsB gene has been shown to be regulated by stress response regulators such as RPOE-MONOMER and GUANOSINE-5DP-3DP...

## Biological Role

Catalyzes 2,3-dehydroacyl-CoA:sn-glycerol-3-phosphate O-acyltransferase (reaction.R02617), RXN-10462 (reaction.ecocyc.RXN-10462), RXN-1381 (reaction.ecocyc.RXN-1381), RXN-17016 (reaction.ecocyc.RXN-17016), RXN-17017 (reaction.ecocyc.RXN-17017), RXN-17018 (reaction.ecocyc.RXN-17018).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of an acyl group from acyl-ACP to glycerol-3-phosphate (G3P) to form lysophosphatidic acid (LPA). This enzyme can utilize either acyl-CoA or acyl-ACP as the fatty acyl donor. {ECO:0000269|PubMed:17645809, ECO:0000269|PubMed:6997313}.

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.R02617|reaction.R02617]] `KEGG` `database` - via EC:2.3.1.15
- `catalyzes` --> [[reaction.ecocyc.RXN-10462|reaction.ecocyc.RXN-10462]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-1381|reaction.ecocyc.RXN-1381]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17016|reaction.ecocyc.RXN-17016]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17017|reaction.ecocyc.RXN-17017]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17018|reaction.ecocyc.RXN-17018]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4041|gene.b4041]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7A7`
- `KEGG:ecj:JW4001;eco:b4041;ecoc:C3026_21840;`
- `GeneID:75169496;75204185;948541;`
- `GO:GO:0004366; GO:0005886; GO:0006631; GO:0008654; GO:0016024`
- `EC:2.3.1.15`

## Notes

Glycerol-3-phosphate acyltransferase (GPAT) (EC 2.3.1.15)
