---
entity_id: "protein.P0A9C5"
entity_type: "protein"
name: "glnA"
source_database: "UniProt"
source_id: "P0A9C5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250|UniProtKB:P9WN39}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glnA b3870 JW3841"
---

# glnA

`protein.P0A9C5`

## Static

- Type: `protein`
- Source: `UniProt:P0A9C5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250|UniProtKB:P9WN39}.

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent biosynthesis of glutamine from glutamate and ammonia. {ECO:0000250|UniProtKB:P0A1P6}.

## Biological Role

Catalyzes L-glutamate:ammonia ligase (ADP-forming) (reaction.R00253). Component of glutamine synthetase (complex.ecocyc.GLUTAMINESYN-OLIGOMER).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Catalyzes the ATP-dependent biosynthesis of glutamine from glutamate and ammonia. {ECO:0000250|UniProtKB:P0A1P6}.

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00253|reaction.R00253]] `KEGG` `database` - via EC:6.3.1.2
- `is_component_of` --> [[complex.ecocyc.GLUTAMINESYN-OLIGOMER|complex.ecocyc.GLUTAMINESYN-OLIGOMER]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=12

## Incoming Edges (1)

- `encodes` <-- [[gene.b3870|gene.b3870]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9C5`
- `KEGG:ecj:JW3841;eco:b3870;ecoc:C3026_20920;`
- `GeneID:86948480;93778066;948370;`
- `GO:GO:0004356; GO:0005524; GO:0005737; GO:0005829; GO:0006542; GO:0009314; GO:0016020; GO:0019676; GO:0019740; GO:0042802; GO:0046872`
- `EC:6.3.1.2`

## Notes

Glutamine synthetase (GS) (EC 6.3.1.2) (Glutamate--ammonia ligase) (Glutamine synthetase I beta) (GSI beta)
