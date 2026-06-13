---
entity_id: "protein.P32129"
entity_type: "protein"
name: "yihG"
source_database: "UniProt"
source_id: "P32129"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Single-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yihG f310 b3862 JW3834"
---

# yihG

`protein.P32129`

## Static

- Type: `protein`
- Source: `UniProt:P32129`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Single-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Acyltransferase involved in the biosynthesis of membrane phospholipids (PubMed:32403425). It introduces a cis-vaccenoyl group (18:1) into the sn-2 position of phospholipids (PubMed:32403425). Overproduction of YihG facilitates the synthesis of phospholipids containing a myristoyl group (14:0) and a cis-vaccenoyl group at the sn-2 position, and a cis-vaccenoyl group at the sn-1 position (PubMed:32403425). May affect flagellar formation through modulation of the fatty acyl composition of membrane phospholipids (PubMed:32403425). {ECO:0000269|PubMed:32403425}. yihG encodes a membrane-bound 1-acylglycerol-3-phosphate O-acyltransferase (also called lysophosphatidic acid acyltransferase or LPAAT for short) . Analysis of the phospholipid composition of cells overproducing YihG suggests that the enzyme facilitates synthesis of phospholipids containing cis-vaccenoyl (18:1) and myristoyl (14:0) at the sn-2 position and preferably introduces these groups into lysophospholipids containing cis-vaccenoyl (18:1) at the sn-1 position . Analysis of the phospholipid composition of ΔyihG cells grown at 37°C suggests that the endogenous enzyme transfers cis-vaccenoyl (18:1) from acyl donor substrates (acyl-acyl carrier protein or coenzyme A) to the sn-2 position of membrane phospholipids...

## Biological Role

Catalyzes 1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN (reaction.ecocyc.1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN), RXN-1623 (reaction.ecocyc.RXN-1623).

## Annotation

FUNCTION: Acyltransferase involved in the biosynthesis of membrane phospholipids (PubMed:32403425). It introduces a cis-vaccenoyl group (18:1) into the sn-2 position of phospholipids (PubMed:32403425). Overproduction of YihG facilitates the synthesis of phospholipids containing a myristoyl group (14:0) and a cis-vaccenoyl group at the sn-2 position, and a cis-vaccenoyl group at the sn-1 position (PubMed:32403425). May affect flagellar formation through modulation of the fatty acyl composition of membrane phospholipids (PubMed:32403425). {ECO:0000269|PubMed:32403425}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN|reaction.ecocyc.1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-1623|reaction.ecocyc.RXN-1623]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3862|gene.b3862]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32129`
- `KEGG:ecj:JW3834;eco:b3862;ecoc:C3026_20875;`
- `GeneID:948350;`
- `GO:GO:0003841; GO:0005886; GO:0008654`
- `EC:2.3.1.51`

## Notes

1-acylglycerol-3-phosphate O-acyltransferase YihG (EC 2.3.1.51) (Lysophosphatidic acid acyltransferase) (LPAAT)
