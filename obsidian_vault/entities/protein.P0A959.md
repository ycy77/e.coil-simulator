---
entity_id: "protein.P0A959"
entity_type: "protein"
name: "alaA"
source_database: "UniProt"
source_id: "P0A959"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "alaA yfbQ b2290 JW2287"
---

# alaA

`protein.P0A959`

## Static

- Type: `protein`
- Source: `UniProt:P0A959`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Involved in the biosynthesis of alanine. Catalyzes the transamination of pyruvate by glutamate, leading to the formation of L-alanine and 2-oxoglutarate. Is also able to catalyze the reverse reaction. {ECO:0000269|PubMed:20729367}.

## Biological Role

Catalyzes L-alanine:2-oxoglutarate aminotransferase (reaction.R00258). Component of glutamate—pyruvate aminotransferase AlaA (complex.ecocyc.CPLX0-7888).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of alanine. Catalyzes the transamination of pyruvate by glutamate, leading to the formation of L-alanine and 2-oxoglutarate. Is also able to catalyze the reverse reaction. {ECO:0000269|PubMed:20729367}.

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00258|reaction.R00258]] `KEGG` `database` - via EC:2.6.1.2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7888|complex.ecocyc.CPLX0-7888]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2290|gene.b2290]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A959`
- `KEGG:ecj:JW2287;eco:b2290;ecoc:C3026_12775;`
- `GeneID:93774884;946772;`
- `GO:GO:0004021; GO:0005737; GO:0006523; GO:0006974; GO:0008483; GO:0019272; GO:0030170; GO:0030632; GO:0042803; GO:0046677`
- `EC:2.6.1.2`

## Notes

Glutamate-pyruvate aminotransferase AlaA (EC 2.6.1.2)
