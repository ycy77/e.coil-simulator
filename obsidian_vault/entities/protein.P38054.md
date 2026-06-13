---
entity_id: "protein.P38054"
entity_type: "protein"
name: "cusA"
source_database: "UniProt"
source_id: "P38054"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cusA ybdE b0575 JW0564"
---

# cusA

`protein.P38054`

## Static

- Type: `protein`
- Source: `UniProt:P38054`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of a cation efflux system that mediates resistance to copper and silver. {ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:12813074}. CusA is a member of the Resistance-Nodulation-Cell Division (RND) Transporter Superfamily and is involved in the detoxification of copper and silver ions in E. coli as part of the CusCFBA copper/silver efflux system. CusA contains 12 transmembrane (TM) segments and a large periplasmic domain formed from two loops located between TM1 and 2 and TM7 and 8 . As an RND transporter, CusA probably forms trimers in vivo, but it forms a mixture of oligomers in detergent solution . The amino acids M573, M623, M672, D405, E412, and A399 of CusA are essential for copper tolerance . Crystal structures of apo and ion bound CusA suggest that the protein uses methionine pairs or clusters to export copper and silver ions from both the cytoplasm and the periplasm. 3 methionine residues - M573, M623 and M672 coordinate Cu(I) bound in a periplasmic cleft. In addition, 3 pairs of methionine residues - M410/501, M403/486 and M391/1009 - located in the transmembrane region and a further pair (M271/755) located in the periplasmic domain of the protein may form a relay of binding sites for the movement of substrate ions . Copper may bind to CusA by a Met2 O/N motif comprising M573, M672 and E625...

## Biological Role

Component of copper/silver export system (complex.ecocyc.CPLX0-1721).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of a cation efflux system that mediates resistance to copper and silver. {ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:12813074}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1721|complex.ecocyc.CPLX0-1721]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0575|gene.b0575]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P38054`
- `KEGG:ecj:JW0564;eco:b0575;ecoc:C3026_02855;`
- `GeneID:945191;`
- `GO:GO:0005375; GO:0005507; GO:0005886; GO:0006878; GO:0009636; GO:0010272; GO:0010273; GO:0015080; GO:0015673; GO:0015679; GO:0016020; GO:0035434; GO:0042910; GO:0046688; GO:0060003; GO:1902601`

## Notes

Cation efflux system protein CusA
