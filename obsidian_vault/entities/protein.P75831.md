---
entity_id: "protein.P75831"
entity_type: "protein"
name: "macB"
source_database: "UniProt"
source_id: "P75831"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01720, ECO:0000269|PubMed:11544226, ECO:0000269|PubMed:17214741}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01720, ECO:0000269|PubMed:11544226, ECO:0000269|PubMed:17214741}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "macB ybjZ b0879 JW0863"
---

# macB

`protein.P75831`

## Static

- Type: `protein`
- Source: `UniProt:P75831`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01720, ECO:0000269|PubMed:11544226, ECO:0000269|PubMed:17214741}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01720, ECO:0000269|PubMed:11544226, ECO:0000269|PubMed:17214741}.

## Enriched Summary

FUNCTION: Part of the tripartite efflux system MacAB-TolC (PubMed:11544226, PubMed:28504659, PubMed:29109272, PubMed:40083904, PubMed:40461577). MacB is a non-canonical ABC transporter that contains transmembrane domains (TMD), which form a pore in the inner membrane, and an ATP-binding domain (NBD), which is responsible for energy generation (PubMed:17214741, PubMed:18955484, PubMed:29109272). When overexpressed, the system confers resistance against macrolides composed of 14- and 15-membered lactones but no or weak resistance against 16-membered ones; also confers resistance against bacitracin and colistin (PubMed:11544226, PubMed:28504659, PubMed:29109272). Involved in secretion of enterotoxin STII (PubMed:29109272). In addition, the system could also transport R-LPS or a similar glycolipid (PubMed:23974027). As part of the system, involved in the efflux of the immediate heme precursor, protoporphyrin IX (PPIX), which is probably an endogenous substrate (PubMed:25257218). {ECO:0000269|PubMed:11544226, ECO:0000269|PubMed:17214741, ECO:0000269|PubMed:18955484, ECO:0000269|PubMed:23974027, ECO:0000269|PubMed:25257218, ECO:0000269|PubMed:28504659, ECO:0000269|PubMed:29109272, ECO:0000269|PubMed:40083904, ECO:0000269|PubMed:40461577}...

## Biological Role

Component of ABC-type tripartite efflux pump (complex.ecocyc.TRANS-200-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the tripartite efflux system MacAB-TolC (PubMed:11544226, PubMed:28504659, PubMed:29109272, PubMed:40083904, PubMed:40461577). MacB is a non-canonical ABC transporter that contains transmembrane domains (TMD), which form a pore in the inner membrane, and an ATP-binding domain (NBD), which is responsible for energy generation (PubMed:17214741, PubMed:18955484, PubMed:29109272). When overexpressed, the system confers resistance against macrolides composed of 14- and 15-membered lactones but no or weak resistance against 16-membered ones; also confers resistance against bacitracin and colistin (PubMed:11544226, PubMed:28504659, PubMed:29109272). Involved in secretion of enterotoxin STII (PubMed:29109272). In addition, the system could also transport R-LPS or a similar glycolipid (PubMed:23974027). As part of the system, involved in the efflux of the immediate heme precursor, protoporphyrin IX (PPIX), which is probably an endogenous substrate (PubMed:25257218). {ECO:0000269|PubMed:11544226, ECO:0000269|PubMed:17214741, ECO:0000269|PubMed:18955484, ECO:0000269|PubMed:23974027, ECO:0000269|PubMed:25257218, ECO:0000269|PubMed:28504659, ECO:0000269|PubMed:29109272, ECO:0000269|PubMed:40083904, ECO:0000269|PubMed:40461577}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TRANS-200-CPLX|complex.ecocyc.TRANS-200-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0879|gene.b0879]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75831`
- `KEGG:ecj:JW0863;eco:b0879;ecoc:C3026_05460;`
- `GeneID:945164;`
- `GO:GO:0005524; GO:0005886; GO:0008559; GO:0016020; GO:0016887; GO:0022857; GO:0042802; GO:0042803; GO:0042893; GO:0042897; GO:0046677; GO:1990196; GO:1990961`
- `EC:7.6.2.-`

## Notes

Macrolide export ATP-binding/permease protein MacB (EC 7.6.2.-)
