---
entity_id: "protein.P05791"
entity_type: "protein"
name: "ilvD"
source_database: "UniProt"
source_id: "P05791"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ilvD b3771 JW5605"
---

# ilvD

`protein.P05791`

## Static

- Type: `protein`
- Source: `UniProt:P05791`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Functions in the biosynthesis of branched-chain amino acids. Catalyzes the dehydration of (2R,3R)-2,3-dihydroxy-3-methylpentanoate (2,3-dihydroxy-3-methylvalerate) into 2-oxo-3-methylpentanoate (2-oxo-3-methylvalerate) and of (2R)-2,3-dihydroxy-3-methylbutanoate (2,3-dihydroxyisovalerate) into 2-oxo-3-methylbutanoate (2-oxoisovalerate), the penultimate precursor to L-isoleucine and L-valine, respectively. {ECO:0000269|PubMed:13727223, ECO:0000269|PubMed:8325851}.

## Biological Role

Component of dihydroxy-acid dehydratase (complex.ecocyc.DIHYDROXYACIDDEHYDRAT-CPLX).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Functions in the biosynthesis of branched-chain amino acids. Catalyzes the dehydration of (2R,3R)-2,3-dihydroxy-3-methylpentanoate (2,3-dihydroxy-3-methylvalerate) into 2-oxo-3-methylpentanoate (2-oxo-3-methylvalerate) and of (2R)-2,3-dihydroxy-3-methylbutanoate (2,3-dihydroxyisovalerate) into 2-oxo-3-methylbutanoate (2-oxoisovalerate), the penultimate precursor to L-isoleucine and L-valine, respectively. {ECO:0000269|PubMed:13727223, ECO:0000269|PubMed:8325851}.

## Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DIHYDROXYACIDDEHYDRAT-CPLX|complex.ecocyc.DIHYDROXYACIDDEHYDRAT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3771|gene.b3771]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05791`
- `KEGG:ecj:JW5605;eco:b3771;ecoc:C3026_20425;`
- `GeneID:948277;`
- `GO:GO:0000287; GO:0004160; GO:0005829; GO:0009097; GO:0009099; GO:0016836; GO:0051536; GO:0051537; GO:0051539`
- `EC:4.2.1.9`

## Notes

Dihydroxy-acid dehydratase (DAD) (EC 4.2.1.9)
