---
entity_id: "protein.P00894"
entity_type: "protein"
name: "ilvH"
source_database: "UniProt"
source_id: "P00894"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ilvH brnP b0078 JW0077"
---

# ilvH

`protein.P00894`

## Static

- Type: `protein`
- Source: `UniProt:P00894`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Acetolactate synthase isozyme 3 small subunit (EC 2.2.1.6) (ALS-III) (Acetohydroxy-acid synthase III small subunit) (AHAS-III) IlvH is the small regulatory subunit of the bifunctional acetohydroxybutanoate synthase /acetolactate synthase (IlvI/H, AHAS III) which carries out both the first step in valine biosynthesis and the second step in isoleucine biosynthesis. The IlvI/H protein complex catalyzes the conversion of pyruvate and oxobutanoate into 2-aceto-2-hydroxy-butyrate and the conversion of pyruvate into 2-acetolactate. Both reactions generate carbon dioxide as a product. IlvH confers sensitivity to inhibition by valine and is required for full catalytic activity of acetolactate synthase III holoenzyme . The crystal structure of IlvH has been determined at 1.75 Å resolution. It forms a dimer with two ferredoxin domains in each monomer. The valine binding sites can be tentatively assigned to the interface between the two N-terminal domains . C-terminal and N-terminal ilvH mutants were constructed and used to determine the minimum activation peptide necessary to activate IlvI . Mutagenesis of the C-terminal domain of IlvH prevented interdomain contacts resulting in uninhibited activity and low affinity for valine . Interactions between large and small subunits of different AHAS isozymes were investigated...

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

Acetolactate synthase isozyme 3 small subunit (EC 2.2.1.6) (ALS-III) (Acetohydroxy-acid synthase III small subunit) (AHAS-III)

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

- `encodes` <-- [[gene.b0078|gene.b0078]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00894`
- `KEGG:ecj:JW0077;eco:b0078;`
- `GeneID:947267;`
- `GO:GO:0003984; GO:0005829; GO:0005948; GO:0009082; GO:0009097; GO:0009099; GO:1990610`
- `EC:2.2.1.6`

## Notes

Acetolactate synthase isozyme 3 small subunit (EC 2.2.1.6) (ALS-III) (Acetohydroxy-acid synthase III small subunit) (AHAS-III)
