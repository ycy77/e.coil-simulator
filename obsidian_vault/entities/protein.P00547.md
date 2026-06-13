---
entity_id: "protein.P00547"
entity_type: "protein"
name: "thrB"
source_database: "UniProt"
source_id: "P00547"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thrB b0003 JW0002"
---

# thrB

`protein.P00547`

## Static

- Type: `protein`
- Source: `UniProt:P00547`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent phosphorylation of L-homoserine to L-homoserine phosphate. Is also able to phosphorylate the hydroxy group on gamma-carbon of L-homoserine analogs when the functional group at the alpha-position is a carboxyl, an ester, or even a hydroxymethyl group. Neither L-threonine nor L-serine are substrates of the enzyme. {ECO:0000269|PubMed:8973190}.

## Biological Role

Component of homoserine kinase (complex.ecocyc.HOMOSERKIN-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the ATP-dependent phosphorylation of L-homoserine to L-homoserine phosphate. Is also able to phosphorylate the hydroxy group on gamma-carbon of L-homoserine analogs when the functional group at the alpha-position is a carboxyl, an ester, or even a hydroxymethyl group. Neither L-threonine nor L-serine are substrates of the enzyme. {ECO:0000269|PubMed:8973190}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.HOMOSERKIN-CPLX|complex.ecocyc.HOMOSERKIN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0003|gene.b0003]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00547`
- `KEGG:ecj:JW0002;eco:b0003;ecoc:C3026_00015;`
- `GeneID:947498;`
- `GO:GO:0004413; GO:0005524; GO:0005829; GO:0009088`
- `EC:2.7.1.39`

## Notes

Homoserine kinase (HK) (HSK) (EC 2.7.1.39)
