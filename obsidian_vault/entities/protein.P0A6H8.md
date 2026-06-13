---
entity_id: "protein.P0A6H8"
entity_type: "protein"
name: "clsA"
source_database: "UniProt"
source_id: "P0A6H8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00190, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:1663113, ECO:0000269|PubMed:19341704}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00190, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:1663113}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "clsA cls nov yciJ b1249 JW1241"
---

# clsA

`protein.P0A6H8`

## Static

- Type: `protein`
- Source: `UniProt:P0A6H8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00190, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:1663113, ECO:0000269|PubMed:19341704}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00190, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:1663113}.

## Enriched Summary

FUNCTION: Catalyzes the reversible phosphatidyl group transfer from one phosphatidylglycerol molecule to another to form cardiolipin (CL) (diphosphatidylglycerol) and glycerol. {ECO:0000255|HAMAP-Rule:MF_00190, ECO:0000269|PubMed:1663113, ECO:0000269|PubMed:22988102}. ClsA is the major cardiolipin synthase in E. coli. Synthesis of cardiolipin during exponential growth is due to the activity of ClsA, while all three cardiolipin synthases, ClsA, G6406-MONOMER ClsB and G6551-MONOMER ClsC, contribute to cardiolipin synthesis in stationary phase . The ClsA protein appears to undergo posttranslational processing at the N terminus . A Δ2-60 deletion mutant retains activity and membrane association . The catalytic domain of ClsA is located in the cytoplasm; ClsA mainly localizes to the cell poles; localization is cardiolipin-dependent . ClsA is predicted to contain two N-terminal transmembrane domains followed by a soluble C-terminal globular domain; ClsA is a dual-topology protein which retains or flips its catalytic domain to supply cardiolipin on the desired leaflet of the inner membrane; ClsA temporarily adopts an "inverted" topology (the catalytic domain is on the periplasmic side of the inner membrane) in cells subject to osmotic down-shock . A clsA mutant is resistant to rac-3,4-dihydroxybutyl 1-phosphonate (DBP)...

## Biological Role

Catalyzes CARDIOLIPSYN-RXN (reaction.ecocyc.CARDIOLIPSYN-RXN).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible phosphatidyl group transfer from one phosphatidylglycerol molecule to another to form cardiolipin (CL) (diphosphatidylglycerol) and glycerol. {ECO:0000255|HAMAP-Rule:MF_00190, ECO:0000269|PubMed:1663113, ECO:0000269|PubMed:22988102}.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.CARDIOLIPSYN-RXN|reaction.ecocyc.CARDIOLIPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1249|gene.b1249]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6H8`
- `KEGG:ecj:JW1241;eco:b1249;ecoc:C3026_07335;`
- `GeneID:93775314;945821;`
- `GO:GO:0005886; GO:0008808; GO:0016020; GO:0032049; GO:0060187`
- `EC:2.7.8.-`

## Notes

Cardiolipin synthase A (CL synthase) (EC 2.7.8.-)
