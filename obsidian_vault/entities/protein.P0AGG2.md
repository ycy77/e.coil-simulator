---
entity_id: "protein.P0AGG2"
entity_type: "protein"
name: "tesB"
source_database: "UniProt"
source_id: "P0AGG2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tesB b0452 JW0442"
---

# tesB

`protein.P0AGG2`

## Static

- Type: `protein`
- Source: `UniProt:P0AGG2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Thioesterase that has relatively broad substrate specificity, hydrolyzing primarily medium- and long-chain acyl-CoA substrates to free fatty acids and CoA (PubMed:1645722, PubMed:20547355, PubMed:24271180). Functions in the thioesterase-dependent pathway of beta-oxidation of oleate and conjugated linoleate ((9Z,11E)-octadecadienoate or CLA), which provides all energy and carbon precursors required for the growth of E.coli. Thus, supports growth on oleate or conjugated linoleate as the sole source of carbon by hydrolyzing 3,5-tetradecadienoyl-CoA, the terminal metabolite of oleate beta-oxidation via the alternative thioesterase-dependent pathway, and 3,5-dodecadienoyl-CoA, the end product of CLA beta-oxidation, respectively (PubMed:14707139, PubMed:18702504). Seems to be involved in 3-hydroxyalkanoate production in E.coli (PubMed:20547355). {ECO:0000269|PubMed:14707139, ECO:0000269|PubMed:1645722, ECO:0000269|PubMed:18702504, ECO:0000269|PubMed:20547355, ECO:0000269|PubMed:24271180}. Thioesterase II (TesB) is one of a number of thioesterases present in E. coli. The enzyme has relatively broad substrate specificity, cleaving medium- and long-chain acyl-CoA substrates...

## Biological Role

Catalyzes acyl-CoA hydrolase (reaction.R00383). Component of acyl-CoA thioesterase II (complex.ecocyc.THIOESTERII-CPLX).

## Enriched Pathways

- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Annotation

FUNCTION: Thioesterase that has relatively broad substrate specificity, hydrolyzing primarily medium- and long-chain acyl-CoA substrates to free fatty acids and CoA (PubMed:1645722, PubMed:20547355, PubMed:24271180). Functions in the thioesterase-dependent pathway of beta-oxidation of oleate and conjugated linoleate ((9Z,11E)-octadecadienoate or CLA), which provides all energy and carbon precursors required for the growth of E.coli. Thus, supports growth on oleate or conjugated linoleate as the sole source of carbon by hydrolyzing 3,5-tetradecadienoyl-CoA, the terminal metabolite of oleate beta-oxidation via the alternative thioesterase-dependent pathway, and 3,5-dodecadienoyl-CoA, the end product of CLA beta-oxidation, respectively (PubMed:14707139, PubMed:18702504). Seems to be involved in 3-hydroxyalkanoate production in E.coli (PubMed:20547355). {ECO:0000269|PubMed:14707139, ECO:0000269|PubMed:1645722, ECO:0000269|PubMed:18702504, ECO:0000269|PubMed:20547355, ECO:0000269|PubMed:24271180}.

## Pathways

- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00383|reaction.R00383]] `KEGG` `database` - via EC:3.1.2.20
- `is_component_of` --> [[complex.ecocyc.THIOESTERII-CPLX|complex.ecocyc.THIOESTERII-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0452|gene.b0452]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGG2`
- `KEGG:ecj:JW0442;eco:b0452;ecoc:C3026_02215;`
- `GeneID:93776998;945074;`
- `GO:GO:0005829; GO:0006637; GO:0009062; GO:0042802; GO:0042803; GO:0047617`
- `EC:3.1.2.20`

## Notes

Acyl-CoA thioesterase 2 (EC 3.1.2.20) (Thioesterase II) (TEII)
