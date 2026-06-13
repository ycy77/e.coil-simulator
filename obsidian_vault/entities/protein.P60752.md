---
entity_id: "protein.P60752"
entity_type: "protein"
name: "msbA"
source_database: "UniProt"
source_id: "P60752"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01703, ECO:0000269|PubMed:12119303, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:8809774}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01703, ECO:0000269|PubMed:8809774}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "msbA b0914 JW0897"
---

# msbA

`protein.P60752`

## Static

- Type: `protein`
- Source: `UniProt:P60752`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01703, ECO:0000269|PubMed:12119303, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:8809774}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01703, ECO:0000269|PubMed:8809774}.

## Enriched Summary

FUNCTION: Involved in lipopolysaccharide (LPS) biosynthesis. Translocates lipid A-core from the inner to the outer leaflet of the inner membrane (PubMed:12119303, PubMed:15304478, PubMed:28869968, PubMed:8809774, PubMed:9575204). Transmembrane domains (TMD) form a pore in the inner membrane and the ATP-binding domain (NBD) is responsible for energy generation (PubMed:12119303). Shows ATPase activity (PubMed:12119303, PubMed:18024585, PubMed:18344567, PubMed:19132955, PubMed:20412049, PubMed:21462989). May transport glycerophospholipids (PubMed:9575204). In proteoliposomes, mediates the ATP-dependent flipping of a variety of phospholipid and glycolipid derivatives (PubMed:20412049). May also function as a multidrug transporter (PubMed:19132955). {ECO:0000269|PubMed:12119303, ECO:0000269|PubMed:15304478, ECO:0000269|PubMed:18024585, ECO:0000269|PubMed:18344567, ECO:0000269|PubMed:19132955, ECO:0000269|PubMed:20412049, ECO:0000269|PubMed:21462989, ECO:0000269|PubMed:28869968, ECO:0000269|PubMed:8809774, ECO:0000269|PubMed:9575204}. Lipopolysaccharide (LPS), which is a major component of the outer leaflet of the outer membranes of Gram-negative bacteria, consists of lipid A linked to a short core oligosaccharide (lipid A-core) plus a distal O-antigen polysaccharide chain (which is absent in E. coli K-12)...

## Biological Role

Component of ATP-dependent Lipid A-core flippase (complex.ecocyc.CPLX0-7704).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Involved in lipopolysaccharide (LPS) biosynthesis. Translocates lipid A-core from the inner to the outer leaflet of the inner membrane (PubMed:12119303, PubMed:15304478, PubMed:28869968, PubMed:8809774, PubMed:9575204). Transmembrane domains (TMD) form a pore in the inner membrane and the ATP-binding domain (NBD) is responsible for energy generation (PubMed:12119303). Shows ATPase activity (PubMed:12119303, PubMed:18024585, PubMed:18344567, PubMed:19132955, PubMed:20412049, PubMed:21462989). May transport glycerophospholipids (PubMed:9575204). In proteoliposomes, mediates the ATP-dependent flipping of a variety of phospholipid and glycolipid derivatives (PubMed:20412049). May also function as a multidrug transporter (PubMed:19132955). {ECO:0000269|PubMed:12119303, ECO:0000269|PubMed:15304478, ECO:0000269|PubMed:18024585, ECO:0000269|PubMed:18344567, ECO:0000269|PubMed:19132955, ECO:0000269|PubMed:20412049, ECO:0000269|PubMed:21462989, ECO:0000269|PubMed:28869968, ECO:0000269|PubMed:8809774, ECO:0000269|PubMed:9575204}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7704|complex.ecocyc.CPLX0-7704]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0914|gene.b0914]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60752`
- `KEGG:ecj:JW0897;eco:b0914;ecoc:C3026_05630;`
- `GeneID:75205316;945530;`
- `GO:GO:0005524; GO:0005886; GO:0006869; GO:0008289; GO:0008559; GO:0015437; GO:0015920; GO:0016020; GO:0016887; GO:0034040; GO:0034204; GO:0042802; GO:0043190; GO:0055085; GO:1990199`
- `EC:7.5.2.6`

## Notes

ATP-dependent lipid A-core flippase (EC 7.5.2.6) (Lipid A export ATP-binding/permease protein MsbA) (Lipid flippase)
