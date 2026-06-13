---
entity_id: "protein.P0A991"
entity_type: "protein"
name: "fbaB"
source_database: "UniProt"
source_id: "P0A991"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fbaB dhnA b2097 JW5344"
---

# fbaB

`protein.P0A991`

## Static

- Type: `protein`
- Source: `UniProt:P0A991`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the reversible aldol condensation/cleavage reaction between glyceraldehyde 3-phosphate and dihydroxyacetone phosphate (DHAP) to yield fructose-bisphosphate (FBP). {ECO:0000269|PubMed:9531482}.

## Biological Role

Component of fructose-bisphosphate aldolase class I (complex.ecocyc.FRUCBISALD-CLASSI).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible aldol condensation/cleavage reaction between glyceraldehyde 3-phosphate and dihydroxyacetone phosphate (DHAP) to yield fructose-bisphosphate (FBP). {ECO:0000269|PubMed:9531482}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.FRUCBISALD-CLASSI|complex.ecocyc.FRUCBISALD-CLASSI]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## Incoming Edges (1)

- `encodes` <-- [[gene.b2097|gene.b2097]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A991`
- `KEGG:ecj:JW5344;eco:b2097;ecoc:C3026_11770;`
- `GeneID:75205967;946632;`
- `GO:GO:0004332; GO:0005829; GO:0006096; GO:0016020; GO:0042802`
- `EC:4.1.2.13`

## Notes

Fructose-bisphosphate aldolase class 1 (EC 4.1.2.13) (Fructose-bisphosphate aldolase class I) (FBP aldolase)
