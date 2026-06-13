---
entity_id: "protein.P26647"
entity_type: "protein"
name: "plsC"
source_database: "UniProt"
source_id: "P26647"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:1557036}; Peripheral membrane protein {ECO:0000269|PubMed:1557036}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "plsC parF b3018 JW2986"
---

# plsC

`protein.P26647`

## Static

- Type: `protein`
- Source: `UniProt:P26647`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:1557036}; Peripheral membrane protein {ECO:0000269|PubMed:1557036}.

## Enriched Summary

FUNCTION: Converts lysophosphatidic acid (LPA) into phosphatidic acid by incorporating an acyl moiety at the 2 position. This enzyme can utilize either acyl-CoA or acyl-ACP as the fatty acyl donor. {ECO:0000269|PubMed:2211622}. Membrane-bound 1-acylglycerol-3-phosphate O-acyltransferase (PlsC) catalyzes the second step in phospholipid biosynthesis and is thought to function in close proximity to the preceding enzyme, GLYCEROL-3-P-ACYLTRANSFER-MONOMER (PlsB) . PlsC is specific for acylation at the sn-2 position of ACYL-SN-GLYCEROL-3P and can utilize either acyl-acyl carrier protein (acyl-ACP) or acyl-coenzyme A (acyl-CoA) as the fatty acyl donor to form L-PHOSPHATIDATE (a phosphatidate, a phosphatidic acid) . PlsB and PlsC activity has been reconstituted in a cell-free liposome system . Fatty acids that are endogenously synthesized are attached to ACP, and exogenously added fatty acids are attached to CoA . In E. coli phospholipids, the sn-1 position is occupied mainly by either palmitate or cis-vaccenate, whereas the sn-2 position is predominantly palmitoleate or cis-vaccenate...

## Biological Role

Catalyzes 1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN (reaction.ecocyc.1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN), RXN-1623 (reaction.ecocyc.RXN-1623), RXN-17012 (reaction.ecocyc.RXN-17012), RXN-17013 (reaction.ecocyc.RXN-17013), RXN-17020 (reaction.ecocyc.RXN-17020), RXN-17022 (reaction.ecocyc.RXN-17022), RXN-17024 (reaction.ecocyc.RXN-17024), 1-acylglycerol-3-phosphate O-acyltransferase (reaction.ecocyc.RXN0-5514), and 1 more.

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Converts lysophosphatidic acid (LPA) into phosphatidic acid by incorporating an acyl moiety at the 2 position. This enzyme can utilize either acyl-CoA or acyl-ACP as the fatty acyl donor. {ECO:0000269|PubMed:2211622}.

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (9)

- `catalyzes` --> [[reaction.ecocyc.1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN|reaction.ecocyc.1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-1623|reaction.ecocyc.RXN-1623]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17012|reaction.ecocyc.RXN-17012]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17013|reaction.ecocyc.RXN-17013]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17020|reaction.ecocyc.RXN-17020]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17022|reaction.ecocyc.RXN-17022]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17024|reaction.ecocyc.RXN-17024]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5514|reaction.ecocyc.RXN0-5514]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6705|reaction.ecocyc.RXN0-6705]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3018|gene.b3018]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P26647`
- `KEGG:ecj:JW2986;eco:b3018;ecoc:C3026_16490;`
- `GeneID:947496;`
- `GO:GO:0003841; GO:0005886; GO:0006654; GO:0016024`
- `EC:2.3.1.51; 2.3.1.n4`

## Notes

1-acyl-sn-glycerol-3-phosphate acyltransferase (1-AGP acyltransferase) (1-AGPAT) (EC 2.3.1.51) (EC 2.3.1.n4) (Lysophosphatidic acid acyltransferase) (LPAAT) (Phosphatidic acid synthase) (PA synthase)
