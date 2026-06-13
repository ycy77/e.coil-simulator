---
entity_id: "protein.P00893"
entity_type: "protein"
name: "ilvI"
source_database: "UniProt"
source_id: "P00893"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ilvI b0077 JW0076"
---

# ilvI

`protein.P00893`

## Static

- Type: `protein`
- Source: `UniProt:P00893`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Acetolactate synthase isozyme 3 large subunit (EC 2.2.1.6) (AHAS-III) (ALS-III) (Acetohydroxy-acid synthase III large subunit) IlvI is the large catalytic subunit of the bifunctional acetohydroxybutanoate synthase /acetolactate synthase (IlvI/H, AHAS III) which carries out both the first step in valine biosynthesis and the second step in isoleucine biosynthesis. The IlvI/H protein complex catalyzes the conversion of pyruvate and oxobutanoate into 2-aceto-2-hydroxy-butyrate and the conversion of pyruvate into 2-acetolactate. Both reactions generate carbon dioxide as a product. C-terminal and N-terminal ilvH mutants were constructed and used to determine the minimum activation peptide necessary to activate IlvI . Interactions between large and small subunits of different AHAS isozymes were investigated. IlvI could be activated by IlvM just as well as IlvH. Isolated IlvI has only 5% of the molar activity of its holoenzyme. However, isolated IlvI has similar substrate specificity and similar cofactor dependence as its holoenzyme. Assembly of the holoenzyme requires FAD.

## Biological Role

Catalyzes pyruvate:pyruvate acetaldehydetransferase (decarboxylating); (reaction.R00006), pyruvate:thiamin diphosphate acetaldehydetransferase (decarboxylating) (reaction.R00014), pyruvate:pyruvate acetaldehydetransferase (decarboxylating); (reaction.R00226), (S)-2-acetolactate pyruvate-lyase (carboxylating) (reaction.R04672), (S)-2-aceto-2-hydroxybutanoate pyruvate-lyase (carboxylating) (reaction.R04673). Component of acetolactate synthase / acetohydroxybutanoate synthase (complex.ecocyc.ACETOLACTSYNIII-CPLX).

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

Acetolactate synthase isozyme 3 large subunit (EC 2.2.1.6) (AHAS-III) (ALS-III) (Acetohydroxy-acid synthase III large subunit)

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
- `is_component_of` --> [[complex.ecocyc.ACETOLACTSYNIII-CPLX|complex.ecocyc.ACETOLACTSYNIII-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0077|gene.b0077]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00893`
- `KEGG:ecj:JW0076;eco:b0077;`
- `GeneID:948793;`
- `GO:GO:0000287; GO:0003984; GO:0005829; GO:0005948; GO:0009082; GO:0009097; GO:0009099; GO:0030976; GO:0050660`
- `EC:2.2.1.6`

## Notes

Acetolactate synthase isozyme 3 large subunit (EC 2.2.1.6) (AHAS-III) (ALS-III) (Acetohydroxy-acid synthase III large subunit)
