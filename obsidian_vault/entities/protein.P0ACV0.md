---
entity_id: "protein.P0ACV0"
entity_type: "protein"
name: "lpxL"
source_database: "UniProt"
source_id: "P0ACV0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01942, ECO:0000269|PubMed:1846149, ECO:0000269|PubMed:18656959, ECO:0000269|PubMed:8662613}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01942}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lpxL htrB waaM b1054 JW1041"
---

# lpxL

`protein.P0ACV0`

## Static

- Type: `protein`
- Source: `UniProt:P0ACV0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01942, ECO:0000269|PubMed:1846149, ECO:0000269|PubMed:18656959, ECO:0000269|PubMed:8662613}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01942}.

## Enriched Summary

FUNCTION: Catalyzes the transfer of laurate from lauroyl-[acyl-carrier-protein] (ACP) to Kdo(2)-lipid IV(A) to form Kdo(2)-(lauroyl)-lipid IV(A). Has 10 fold selectivity for lauroyl-ACP over myristoyl-ACP. In vitro, can also catalyze a slow second acylation reaction leading to the formation of Kdo(2)-(dilauroyl)-lipid IV(A). {ECO:0000269|PubMed:18656959, ECO:0000269|PubMed:2203778, ECO:0000269|PubMed:8662613}. Lauroyl acyltransferase (LpxL) transfers laurate from lauroyl acyl carrier protein (ACP) to the free OH group of the 2'-R-3-hydroxymyristoyl chain of the KDO2-lipid IVA. This is one of the last two acylation reactions needed to synthesize KDO2-lipid A . LpxL is an inner membrane protein with a predicted single N-terminal transmembrane helix . LpxL shares sequence homology and functional similarity to LpxM, the final enzyme in the lipid A biosynthetic pathway . A third ortholog, LpxP, is induced below 20°C and competes with LpxL to transfer palmitoleate chain to KDO2-lipid IVA . Distant sequence homology exists between LpxL and the glycerol-3-phosphate acyltransferase (GPAT) family of enzymes . lpxL, the gene coding for LpxL was previously identified as a high-temperature requirement gene (htrB) because the null mutant was temperature-sensitive for growth above 33°C. Under nonpermissive conditions, cell division ceased, the membrane bulged and the cells slowly lysed...

## Biological Role

Catalyzes LAUROYLACYLTRAN-RXN (reaction.ecocyc.LAUROYLACYLTRAN-RXN).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of laurate from lauroyl-[acyl-carrier-protein] (ACP) to Kdo(2)-lipid IV(A) to form Kdo(2)-(lauroyl)-lipid IV(A). Has 10 fold selectivity for lauroyl-ACP over myristoyl-ACP. In vitro, can also catalyze a slow second acylation reaction leading to the formation of Kdo(2)-(dilauroyl)-lipid IV(A). {ECO:0000269|PubMed:18656959, ECO:0000269|PubMed:2203778, ECO:0000269|PubMed:8662613}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.LAUROYLACYLTRAN-RXN|reaction.ecocyc.LAUROYLACYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1054|gene.b1054]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACV0`
- `KEGG:ecj:JW1041;eco:b1054;ecoc:C3026_06415;`
- `GeneID:93776353;946216;`
- `GO:GO:0005886; GO:0006950; GO:0008913; GO:0009103; GO:0009245; GO:0016020; GO:0016740; GO:0016746; GO:0036104`
- `EC:2.3.1.241`

## Notes

Lipid A biosynthesis lauroyltransferase (EC 2.3.1.241) (Kdo(2)-lipid IV(A) lauroyltransferase)
