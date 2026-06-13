---
entity_id: "protein.P0ABF8"
entity_type: "protein"
name: "pgsA"
source_database: "UniProt"
source_id: "P0ABF8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pgsA b1912 JW1897"
---

# pgsA

`protein.P0ABF8`

## Static

- Type: `protein`
- Source: `UniProt:P0ABF8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Catalyzes the conversion of cytidine diphosphate diacylglycerol (CDP-DG) and glycerol 3-phosphate into phosphatidylglycerol (PubMed:3003065, PubMed:8824831). Essential for the synthesis of anionic phospholipids, thereby playing a role in balancing the ratio of zwitterionic and anionic phospholipids, which is thought to be important for normal membrane function (PubMed:3003065, PubMed:8824831). {ECO:0000269|PubMed:3003065, ECO:0000269|PubMed:8824831}. Phosphatidylglycerophosphate (PGP) synthase catalyzes the committed step in the biosynthesis of acidic phospholipids. PGP synthase is an integral membrane protein tightly associated with the cytoplasmic membrane . A pgsA null E. coli strain exhibits relatively normal cell division and shows elevated amounts of phospholipid precursors and the normally minimal phospholipid N-acylphosphatidylethanolamine (N-acyl-PE) .

## Biological Role

Catalyzes PHOSPHAGLYPSYN-RXN (reaction.ecocyc.PHOSPHAGLYPSYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of cytidine diphosphate diacylglycerol (CDP-DG) and glycerol 3-phosphate into phosphatidylglycerol (PubMed:3003065, PubMed:8824831). Essential for the synthesis of anionic phospholipids, thereby playing a role in balancing the ratio of zwitterionic and anionic phospholipids, which is thought to be important for normal membrane function (PubMed:3003065, PubMed:8824831). {ECO:0000269|PubMed:3003065, ECO:0000269|PubMed:8824831}.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PHOSPHAGLYPSYN-RXN|reaction.ecocyc.PHOSPHAGLYPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1912|gene.b1912]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABF8`
- `KEGG:ecj:JW1897;eco:b1912;ecoc:C3026_10850;`
- `GeneID:86860050;93776217;945791;`
- `GO:GO:0005886; GO:0006655; GO:0008444; GO:0046474`
- `EC:2.7.8.5`

## Notes

CDP-diacylglycerol--glycerol-3-phosphate 3-phosphatidyltransferase (EC 2.7.8.5) (Phosphatidylglycerophosphate synthase) (PGP synthase)
