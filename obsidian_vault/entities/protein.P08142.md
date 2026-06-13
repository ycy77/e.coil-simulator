---
entity_id: "protein.P08142"
entity_type: "protein"
name: "ilvB"
source_database: "UniProt"
source_id: "P08142"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ilvB b3671 JW3646"
---

# ilvB

`protein.P08142`

## Static

- Type: `protein`
- Source: `UniProt:P08142`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Acetolactate synthase isozyme 1 large subunit (AHAS-I) (EC 2.2.1.6) (Acetohydroxy-acid synthase I large subunit) (ALS-I) IlvB is the large catalytic subunit of AHAS I, the bifunctional acetohydroxybutanoate synthase/acetolactate synthase which carries out both the first step in valine biosynthesis and the second step in isoleucine biosynthesis. The IlvB subunit can catalyze the reaction in isolation and is not inhibited by valine in the manner of the holoenzyme. However, the Vmax for the reaction as catalyzed by IlvB alone is sharply reduced, as is the enzyme's affinity for the required FAD cofactor . Both activities are catalyzed by the same active site on IlvB . The interactions between the large and small subunits from different isozymes were investigated .

## Biological Role

Catalyzes pyruvate:pyruvate acetaldehydetransferase (decarboxylating); (reaction.R00006), pyruvate:thiamin diphosphate acetaldehydetransferase (decarboxylating) (reaction.R00014), pyruvate:pyruvate acetaldehydetransferase (decarboxylating); (reaction.R00226), (S)-2-acetolactate pyruvate-lyase (carboxylating) (reaction.R04672), (S)-2-aceto-2-hydroxybutanoate pyruvate-lyase (carboxylating) (reaction.R04673). Component of acetohydroxybutanoate synthase / acetolactate synthase (complex.ecocyc.ACETOLACTSYNI-CPLX).

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

Acetolactate synthase isozyme 1 large subunit (AHAS-I) (EC 2.2.1.6) (Acetohydroxy-acid synthase I large subunit) (ALS-I)

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
- `is_component_of` --> [[complex.ecocyc.ACETOLACTSYNI-CPLX|complex.ecocyc.ACETOLACTSYNI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3671|gene.b3671]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08142`
- `KEGG:ecj:JW3646;eco:b3671;ecoc:C3026_19895;`
- `GeneID:948182;`
- `GO:GO:0000287; GO:0003984; GO:0005948; GO:0009082; GO:0009097; GO:0009099; GO:0030976; GO:0050660`
- `EC:2.2.1.6`

## Notes

Acetolactate synthase isozyme 1 large subunit (AHAS-I) (EC 2.2.1.6) (Acetohydroxy-acid synthase I large subunit) (ALS-I)
