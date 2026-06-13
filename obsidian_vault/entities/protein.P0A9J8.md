---
entity_id: "protein.P0A9J8"
entity_type: "protein"
name: "pheA"
source_database: "UniProt"
source_id: "P0A9J8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pheA b2599 JW2580"
---

# pheA

`protein.P0A9J8`

## Static

- Type: `protein`
- Source: `UniProt:P0A9J8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the Claisen rearrangement of chorismate to prephenate and the decarboxylation/dehydration of prephenate to phenylpyruvate. {ECO:0000269|PubMed:4261395}.

## Biological Role

Catalyzes L-arogenate hydro-lyase (decarboxylating; L-phenylalanine-forming) (reaction.R00691). Component of fused chorismate mutase/prephenate dehydratase (complex.ecocyc.CHORISMUTPREPHENDEHYDRAT-CPLX).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the Claisen rearrangement of chorismate to prephenate and the decarboxylation/dehydration of prephenate to phenylpyruvate. {ECO:0000269|PubMed:4261395}.

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00691|reaction.R00691]] `KEGG` `database` - via EC:4.2.1.51
- `is_component_of` --> [[complex.ecocyc.CHORISMUTPREPHENDEHYDRAT-CPLX|complex.ecocyc.CHORISMUTPREPHENDEHYDRAT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2599|gene.b2599]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9J8`
- `KEGG:ecj:JW2580;eco:b2599;ecoc:C3026_14395;`
- `GeneID:947081;`
- `GO:GO:0004106; GO:0004664; GO:0005737; GO:0006571; GO:0009094; GO:0042803; GO:0046417`
- `EC:4.2.1.51; 5.4.99.5`

## Notes

Bifunctional chorismate mutase/prephenate dehydratase (Chorismate mutase-prephenate dehydratase) (P-protein) [Includes: Chorismate mutase (CM) (EC 5.4.99.5); Prephenate dehydratase (PDT) (EC 4.2.1.51)]
