---
entity_id: "protein.P75830"
entity_type: "protein"
name: "macA"
source_database: "UniProt"
source_id: "P75830"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11544226, ECO:0000269|PubMed:17214741}; Single-pass membrane protein {ECO:0000269|PubMed:11544226, ECO:0000269|PubMed:17214741}; Periplasmic side {ECO:0000269|PubMed:11544226, ECO:0000269|PubMed:17214741}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "macA ybjY b0878 JW0862"
---

# macA

`protein.P75830`

## Static

- Type: `protein`
- Source: `UniProt:P75830`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11544226, ECO:0000269|PubMed:17214741}; Single-pass membrane protein {ECO:0000269|PubMed:11544226, ECO:0000269|PubMed:17214741}; Periplasmic side {ECO:0000269|PubMed:11544226, ECO:0000269|PubMed:17214741}.

## Enriched Summary

FUNCTION: Part of the tripartite efflux system MacAB-TolC (PubMed:11544226, PubMed:17214741, PubMed:18955484, PubMed:21696464, PubMed:28504659, PubMed:40083904, PubMed:40461577). MacA stimulates the ATPase activity of MacB by promoting the closed ATP-bound state of MacB, increases the capacity of MacB to bind macrolides such as erythromycin, and provides a physical link between MacB and TolC (PubMed:17214741, PubMed:18955484, PubMed:21696464). When overexpressed, the system confers resistance against macrolides composed of 14- and 15-membered lactones but no or weak resistance against 16-membered ones; also confers resistance against bacitracin and colistin (PubMed:11544226, PubMed:18955484). In addition, MacA binds tightly rough-core lipopolysaccharide (R-LPS), suggesting that the system could also transport R-LPS or a similar glycolipid (PubMed:23974027). As part of the system, involved in the efflux of the immediate heme precursor, protoporphyrin IX (PPIX), which is probably an endogenous substrate (PubMed:25257218). {ECO:0000269|PubMed:11544226, ECO:0000269|PubMed:17214741, ECO:0000269|PubMed:18955484, ECO:0000269|PubMed:21696464, ECO:0000269|PubMed:23974027, ECO:0000269|PubMed:25257218, ECO:0000269|PubMed:28504659, ECO:0000269|PubMed:40083904, ECO:0000269|PubMed:40461577}...

## Biological Role

Component of ABC-type tripartite efflux pump (complex.ecocyc.TRANS-200-CPLX).

## Annotation

FUNCTION: Part of the tripartite efflux system MacAB-TolC (PubMed:11544226, PubMed:17214741, PubMed:18955484, PubMed:21696464, PubMed:28504659, PubMed:40083904, PubMed:40461577). MacA stimulates the ATPase activity of MacB by promoting the closed ATP-bound state of MacB, increases the capacity of MacB to bind macrolides such as erythromycin, and provides a physical link between MacB and TolC (PubMed:17214741, PubMed:18955484, PubMed:21696464). When overexpressed, the system confers resistance against macrolides composed of 14- and 15-membered lactones but no or weak resistance against 16-membered ones; also confers resistance against bacitracin and colistin (PubMed:11544226, PubMed:18955484). In addition, MacA binds tightly rough-core lipopolysaccharide (R-LPS), suggesting that the system could also transport R-LPS or a similar glycolipid (PubMed:23974027). As part of the system, involved in the efflux of the immediate heme precursor, protoporphyrin IX (PPIX), which is probably an endogenous substrate (PubMed:25257218). {ECO:0000269|PubMed:11544226, ECO:0000269|PubMed:17214741, ECO:0000269|PubMed:18955484, ECO:0000269|PubMed:21696464, ECO:0000269|PubMed:23974027, ECO:0000269|PubMed:25257218, ECO:0000269|PubMed:28504659, ECO:0000269|PubMed:40083904, ECO:0000269|PubMed:40461577}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TRANS-200-CPLX|complex.ecocyc.TRANS-200-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6 | EcoCyc transporter component coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0878|gene.b0878]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75830`
- `KEGG:ecj:JW0862;eco:b0878;ecoc:C3026_05455;`
- `GeneID:947322;`
- `GO:GO:0005886; GO:0015562; GO:0016020; GO:0019898; GO:0042802; GO:0042893; GO:0042897; GO:0046677; GO:1990196; GO:1990281; GO:1990961`

## Notes

Macrolide export protein MacA (Membrane fusion protein MacA)
