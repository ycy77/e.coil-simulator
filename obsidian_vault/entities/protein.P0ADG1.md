---
entity_id: "protein.P0ADG1"
entity_type: "protein"
name: "ilvM"
source_database: "UniProt"
source_id: "P0ADG1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ilvM b3769 JW3742"
---

# ilvM

`protein.P0ADG1`

## Static

- Type: `protein`
- Source: `UniProt:P0ADG1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Acetolactate synthase isozyme 2 small subunit (EC 2.2.1.6) (ALS-II) (Acetohydroxy-acid synthase II small subunit) (AHAS-II) Acetohydroxyacid synthase II (AHAS II) encoded by ilvG and ilvM catalyzes the biosynthesis of α-aceto-α-hydroxybutyrate and α-acetolactate. AHAS II is not found in E. coli K-12 due to a mutation in ilvG, although it is found in other E. coli strains. See the entry for G8221-MONOMER for more information. In non-K-12 strains AHAS II is a bifunctional enzyme that catalyzes the biosynthesis of α-aceto-α-hydroxybutyrate for the isoleucine pathway and of α-acetolactate for the valine pathway . Both the large catalytic subunit IlvG and the small regulatory subunit IlvM are required for this activity, though the exact stoichiometry of the IlvM subunit is unclear . The kinetics of AHAS II have been evaluated .

## Biological Role

Catalyzes pyruvate:pyruvate acetaldehydetransferase (decarboxylating); (reaction.R00006), pyruvate:thiamin diphosphate acetaldehydetransferase (decarboxylating) (reaction.R00014), pyruvate:pyruvate acetaldehydetransferase (decarboxylating); (reaction.R00226), (S)-2-acetolactate pyruvate-lyase (carboxylating) (reaction.R04672), (S)-2-aceto-2-hydroxybutanoate pyruvate-lyase (carboxylating) (reaction.R04673). Component of acetohydroxybutanoate synthase / acetolactate synthase (complex.ecocyc.ACETOLACTSYNII-CPLX).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

Acetolactate synthase isozyme 2 small subunit (EC 2.2.1.6) (ALS-II) (Acetohydroxy-acid synthase II small subunit) (AHAS-II)

## Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.R00006|reaction.R00006]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` --> [[reaction.R00014|reaction.R00014]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` --> [[reaction.R00226|reaction.R00226]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` --> [[reaction.R04672|reaction.R04672]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` --> [[reaction.R04673|reaction.R04673]] `KEGG` `database` - via EC:2.2.1.6
- `is_component_of` --> [[complex.ecocyc.ACETOLACTSYNII-CPLX|complex.ecocyc.ACETOLACTSYNII-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3769|gene.b3769]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADG1`
- `KEGG:ecj:JW3742;eco:b3769;ecoc:C3026_20415;`
- `GeneID:86861876;93778176;948279;`
- `GO:GO:0003984; GO:0005948; GO:0008652; GO:0009082; GO:0009097; GO:0009099`
- `EC:2.2.1.6`

## Notes

Acetolactate synthase isozyme 2 small subunit (EC 2.2.1.6) (ALS-II) (Acetohydroxy-acid synthase II small subunit) (AHAS-II)
