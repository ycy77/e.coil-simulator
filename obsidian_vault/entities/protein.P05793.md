---
entity_id: "protein.P05793"
entity_type: "protein"
name: "ilvC"
source_database: "UniProt"
source_id: "P05793"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:2653423}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ilvC b3774 JW3747"
---

# ilvC

`protein.P05793`

## Static

- Type: `protein`
- Source: `UniProt:P05793`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:2653423}.

## Enriched Summary

FUNCTION: Involved in the biosynthesis of branched-chain amino acids (BCAA). Catalyzes an alkyl-migration followed by a ketol-acid reduction of (S)-2-acetolactate (S2AL) to yield (R)-2,3-dihydroxy-isovalerate. In the isomerase reaction, S2AL is rearranged via a Mg-dependent methyl migration to produce 3-hydroxy-3-methyl-2-ketobutyrate (HMKB). In the reductase reaction, this 2-ketoacid undergoes a metal-dependent reduction by NADPH to yield (R)-2,3-dihydroxy-isovalerate. Also able to use 2-ketopantoate, 2-ketoisovalerate, 2-ketovalerate, 2-ketobutyrate, 3-hydroxypyruvate, 3-hydroxy-2-ketobutyrate and pyruvate (PubMed:15654896). {ECO:0000269|PubMed:15654896, ECO:0000269|PubMed:21515217, ECO:0000269|PubMed:2653423, ECO:0000269|PubMed:9015391}.

## Biological Role

Catalyzes (R)-2,3-dihydroxy-3-methylbutanoate:NADP+ oxidoreductase (isomerizing) (reaction.R04439), (R)-2,3-dihydroxy-3-methylbutanoate:NADP+ oxidoreductase (isomerizing) (reaction.R04440). Component of ketol-acid reductoisomerase (NADP+) (complex.ecocyc.CPLX0-7643).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of branched-chain amino acids (BCAA). Catalyzes an alkyl-migration followed by a ketol-acid reduction of (S)-2-acetolactate (S2AL) to yield (R)-2,3-dihydroxy-isovalerate. In the isomerase reaction, S2AL is rearranged via a Mg-dependent methyl migration to produce 3-hydroxy-3-methyl-2-ketobutyrate (HMKB). In the reductase reaction, this 2-ketoacid undergoes a metal-dependent reduction by NADPH to yield (R)-2,3-dihydroxy-isovalerate. Also able to use 2-ketopantoate, 2-ketoisovalerate, 2-ketovalerate, 2-ketobutyrate, 3-hydroxypyruvate, 3-hydroxy-2-ketobutyrate and pyruvate (PubMed:15654896). {ECO:0000269|PubMed:15654896, ECO:0000269|PubMed:21515217, ECO:0000269|PubMed:2653423, ECO:0000269|PubMed:9015391}.

## Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R04439|reaction.R04439]] `KEGG` `database` - via EC:1.1.1.86
- `catalyzes` --> [[reaction.R04440|reaction.R04440]] `KEGG` `database` - via EC:1.1.1.86
- `is_component_of` --> [[complex.ecocyc.CPLX0-7643|complex.ecocyc.CPLX0-7643]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3774|gene.b3774]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05793`
- `KEGG:ecj:JW3747;eco:b3774;ecoc:C3026_20440;`
- `GeneID:948286;`
- `GO:GO:0000287; GO:0004455; GO:0005829; GO:0008677; GO:0009097; GO:0009099; GO:0015940; GO:0032991; GO:0042802; GO:0050661`
- `EC:1.1.1.86`

## Notes

Ketol-acid reductoisomerase (NADP(+)) (KARI) (EC 1.1.1.86) (Acetohydroxy-acid isomeroreductase) (AHIR) (Alpha-keto-beta-hydroxylacyl reductoisomerase) (Ketol-acid reductoisomerase type 2) (Ketol-acid reductoisomerase type II)
