---
entity_id: "protein.P0A9L8"
entity_type: "protein"
name: "proC"
source_database: "UniProt"
source_id: "P0A9L8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01925, ECO:0000269|PubMed:6296787}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "proC b0386 JW0377"
---

# proC

`protein.P0A9L8`

## Static

- Type: `protein`
- Source: `UniProt:P0A9L8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01925, ECO:0000269|PubMed:6296787}.

## Enriched Summary

FUNCTION: Catalyzes the reduction of 1-pyrroline-5-carboxylate (PCA) to L-proline. Does not catalyze the reverse reaction. {ECO:0000255|HAMAP-Rule:MF_01925, ECO:0000269|PubMed:12133, ECO:0000269|PubMed:6296787}.

## Biological Role

Component of pyrroline-5-carboxylate reductase (complex.ecocyc.PYRROLINECARBREDUCT-CPLX).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the reduction of 1-pyrroline-5-carboxylate (PCA) to L-proline. Does not catalyze the reverse reaction. {ECO:0000255|HAMAP-Rule:MF_01925, ECO:0000269|PubMed:12133, ECO:0000269|PubMed:6296787}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.PYRROLINECARBREDUCT-CPLX|complex.ecocyc.PYRROLINECARBREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## Incoming Edges (1)

- `encodes` <-- [[gene.b0386|gene.b0386]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9L8`
- `KEGG:ecj:JW0377;eco:b0386;ecoc:C3026_01870;`
- `GeneID:93777075;945034;`
- `GO:GO:0004735; GO:0005829; GO:0042802; GO:0055129`
- `EC:1.5.1.2`

## Notes

Pyrroline-5-carboxylate reductase (P5C reductase) (P5CR) (EC 1.5.1.2) (PCA reductase)
