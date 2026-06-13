---
entity_id: "protein.P0A9B2"
entity_type: "protein"
name: "gapA"
source_database: "UniProt"
source_id: "P0A9B2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gapA b1779 JW1768"
---

# gapA

`protein.P0A9B2`

## Static

- Type: `protein`
- Source: `UniProt:P0A9B2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the oxidative phosphorylation of glyceraldehyde 3-phosphate (G3P) to 1,3-bisphosphoglycerate (BPG) using the cofactor NAD. The first reaction step involves the formation of a hemiacetal intermediate between G3P and a cysteine residue, and this hemiacetal intermediate is then oxidized to a thioester, with concomitant reduction of NAD to NADH. The reduced NADH is then exchanged with the second NAD, and the thioester is attacked by a nucleophilic inorganic phosphate to produce BPG. {ECO:0000269|PubMed:2659073}.

## Biological Role

Component of glyceraldehyde-3-phosphate dehydrogenase (complex.ecocyc.GAPDH-A-CPLX).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the oxidative phosphorylation of glyceraldehyde 3-phosphate (G3P) to 1,3-bisphosphoglycerate (BPG) using the cofactor NAD. The first reaction step involves the formation of a hemiacetal intermediate between G3P and a cysteine residue, and this hemiacetal intermediate is then oxidized to a thioester, with concomitant reduction of NAD to NADH. The reduced NADH is then exchanged with the second NAD, and the thioester is attacked by a nucleophilic inorganic phosphate to produce BPG. {ECO:0000269|PubMed:2659073}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.GAPDH-A-CPLX|complex.ecocyc.GAPDH-A-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1779|gene.b1779]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9B2`
- `KEGG:ecj:JW1768;eco:b1779;ecoc:C3026_10150;`
- `GeneID:86859465;93775988;947679;`
- `GO:GO:0004365; GO:0005829; GO:0006006; GO:0006096; GO:0016020; GO:0042802; GO:0050661; GO:0051287`
- `EC:1.2.1.12`

## Notes

Glyceraldehyde-3-phosphate dehydrogenase A (GAPDH-A) (EC 1.2.1.12) (NAD-dependent glyceraldehyde-3-phosphate dehydrogenase)
