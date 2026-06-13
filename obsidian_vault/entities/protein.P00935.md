---
entity_id: "protein.P00935"
entity_type: "protein"
name: "metB"
source_database: "UniProt"
source_id: "P00935"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "metB b3939 JW3910"
---

# metB

`protein.P00935`

## Static

- Type: `protein`
- Source: `UniProt:P00935`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the formation of L-cystathionine from O-succinyl-L-homoserine (OSHS) and L-cysteine, via a gamma-replacement reaction. In the absence of thiol, catalyzes gamma-elimination to form 2-oxobutanoate, succinate and ammonia. {ECO:0000269|PubMed:2405903}.

## Biological Role

Catalyzes O-succinyl-L-homoserine succinate-lyase (deaminating; 2-oxobutanoate-forming) (reaction.R00999). Component of O-succinylhomoserine(thiol)-lyase / O-succinylhomoserine lyase (complex.ecocyc.O-SUCCHOMOSERLYASE-CPLX).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of L-cystathionine from O-succinyl-L-homoserine (OSHS) and L-cysteine, via a gamma-replacement reaction. In the absence of thiol, catalyzes gamma-elimination to form 2-oxobutanoate, succinate and ammonia. {ECO:0000269|PubMed:2405903}.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00999|reaction.R00999]] `KEGG` `database` - via EC:2.5.1.48
- `is_component_of` --> [[complex.ecocyc.O-SUCCHOMOSERLYASE-CPLX|complex.ecocyc.O-SUCCHOMOSERLYASE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3939|gene.b3939]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00935`
- `KEGG:ecj:JW3910;eco:b3939;ecoc:C3026_21285;`
- `GeneID:948434;`
- `GO:GO:0003962; GO:0004123; GO:0005737; GO:0009086; GO:0019343; GO:0019346; GO:0030170`
- `EC:2.5.1.48`

## Notes

Cystathionine gamma-synthase (CGS) (EC 2.5.1.48) (O-succinylhomoserine (thiol)-lyase)
