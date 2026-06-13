---
entity_id: "protein.P0ADF8"
entity_type: "protein"
name: "ilvN"
source_database: "UniProt"
source_id: "P0ADF8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ilvN b3670 JW3645"
---

# ilvN

`protein.P0ADF8`

## Static

- Type: `protein`
- Source: `UniProt:P0ADF8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Acetolactate synthase isozyme 1 small subunit (EC 2.2.1.6) (Acetohydroxy-acid synthase I small subunit) (AHAS-I) (ALS-I) IlvN is the small regulatory subunit of AHAS I, the bifunctional acetohydroxybutanoate synthase/acetolactate synthase which carries out both the first step in valine biosynthesis and the second step in isoleucine biosynthesis. IlvN was shown to bind close to the FAD binding site of IlvB . The interactions between the large and small subunits from different isozymes were investigated . Wild type cells are sensitive to exogenous valine due to inhibition of the enzymatic activity of IlvB/N . ilvN mutants, however, while still able to grow in the absence of valine and isoleucine, are no longer sensitive in this manner to exogenous valine . The solution structure of IlvN in both the free and valine-bound form was determined by NMR methods. In its free form, IlvN exists as a mixture of conformational states, while in its bound form, IlvN exists as a single conformer . The backbone and side-chain assignments of IlvN in the valine bound form was reported .

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

Acetolactate synthase isozyme 1 small subunit (EC 2.2.1.6) (Acetohydroxy-acid synthase I small subunit) (AHAS-I) (ALS-I)

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

- `encodes` <-- [[gene.b3670|gene.b3670]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADF8`
- `KEGG:ecj:JW3645;eco:b3670;ecoc:C3026_19890;`
- `GeneID:86944341;93778411;948183;`
- `GO:GO:0003984; GO:0005829; GO:0005948; GO:0009082; GO:0009097; GO:0009099; GO:1990610`
- `EC:2.2.1.6`

## Notes

Acetolactate synthase isozyme 1 small subunit (EC 2.2.1.6) (Acetohydroxy-acid synthase I small subunit) (AHAS-I) (ALS-I)
