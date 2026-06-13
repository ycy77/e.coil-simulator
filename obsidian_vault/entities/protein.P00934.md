---
entity_id: "protein.P00934"
entity_type: "protein"
name: "thrC"
source_database: "UniProt"
source_id: "P00934"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thrC b0004 JW0003"
---

# thrC

`protein.P00934`

## Static

- Type: `protein`
- Source: `UniProt:P00934`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the gamma-elimination of phosphate from L-phosphohomoserine and the beta-addition of water to produce L-threonine. To a lesser extent, is able to slowly catalyze the deamination of L-threonine into alpha-ketobutyrate and that of L-serine and 3-chloroalanine into pyruvate. Is also able to rapidly convert vinylglycine to threonine, which proves that the pyridoxal p-quinonoid of vinylglycine is an intermediate in the TS reaction. {ECO:0000269|PubMed:7907888}. Threonine synthase (ThrC) carries out the final step in the biosynthesis of L-threonine, the dephosphorylation of O-phospho-homoserine . A reaction mechanism based on extensive evaluation of the enzymatic activity with alternative substrates and inhibitors has been proposed .

## Biological Role

Catalyzes THRESYN-RXN (reaction.ecocyc.THRESYN-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the gamma-elimination of phosphate from L-phosphohomoserine and the beta-addition of water to produce L-threonine. To a lesser extent, is able to slowly catalyze the deamination of L-threonine into alpha-ketobutyrate and that of L-serine and 3-chloroalanine into pyruvate. Is also able to rapidly convert vinylglycine to threonine, which proves that the pyridoxal p-quinonoid of vinylglycine is an intermediate in the TS reaction. {ECO:0000269|PubMed:7907888}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.THRESYN-RXN|reaction.ecocyc.THRESYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0004|gene.b0004]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00934`
- `KEGG:ecj:JW0003;eco:b0004;ecoc:C3026_00020;`
- `GeneID:945198;`
- `GO:GO:0004795; GO:0005829; GO:0009088; GO:0030170`
- `EC:4.2.3.1`

## Notes

Threonine synthase (TS) (EC 4.2.3.1)
