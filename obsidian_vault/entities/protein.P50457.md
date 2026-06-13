---
entity_id: "protein.P50457"
entity_type: "protein"
name: "puuE"
source_database: "UniProt"
source_id: "P50457"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "puuE goaG b1302 JW1295"
---

# puuE

`protein.P50457`

## Static

- Type: `protein`
- Source: `UniProt:P50457`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the transfer of the amino group from gamma-aminobutyrate (GABA) to alpha-ketoglutarate (KG) to yield succinic semialdehyde (SSA). PuuE is important for utilization of putrescine as the sole nitrogen or carbon source. {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:20639325}. The 4-aminobutyrate aminotransferase PuuE is the initial enzyme of one of two 4-aminobutyrate (GABA) degradation pathways. PuuE was identified as a putrescine-inducible GABA aminotransferase, which allows cells to grow on putrescine as the sole source of nitrogen even in the absence of GabT . PuuE also functions as a 5-aminovalerate aminotransferase during degradation of L-lysine . The function of genes in the puu gene cluster was initially inferred by similarity with the ipuABCDEGFH operon in Pseudomonas sp. . Site-directed mutagenesis confirmed that the K267 residue is essential for catalytic activity . PuuE activity is induced by growth on putrescine and repressed by addition of succinate and under conditions of limited oxygen availability . The three major transaminases in alanine biosynthesis are AvtA, AlaA and AlaC. Expression of aspC, gabT, puuE, tyrB, or ygjG from a plasmid partially suppresses the growth defect of a ΔavtA alaA alaC mutant . The redundancy and promiscuity among aminotransferase enzymes was further investigated...

## Biological Role

Catalyzes GABATRANSAM-RXN (reaction.ecocyc.GABATRANSAM-RXN), VAGL-RXN (reaction.ecocyc.VAGL-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of the amino group from gamma-aminobutyrate (GABA) to alpha-ketoglutarate (KG) to yield succinic semialdehyde (SSA). PuuE is important for utilization of putrescine as the sole nitrogen or carbon source. {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:20639325}.

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GABATRANSAM-RXN|reaction.ecocyc.GABATRANSAM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.VAGL-RXN|reaction.ecocyc.VAGL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1302|gene.b1302]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P50457`
- `KEGG:ecj:JW1295;eco:b1302;`
- `GeneID:945446;`
- `GO:GO:0005829; GO:0009447; GO:0009450; GO:0030170; GO:0034386`
- `EC:2.6.1.19`

## Notes

4-aminobutyrate aminotransferase PuuE (EC 2.6.1.19) (GABA aminotransferase) (GABA-AT) (Gamma-amino-N-butyrate transaminase) (GABA transaminase) (Glutamate:succinic semialdehyde transaminase)
