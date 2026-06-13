---
entity_id: "protein.P30125"
entity_type: "protein"
name: "leuB"
source_database: "UniProt"
source_id: "P30125"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01033}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "leuB b0073 JW5807"
---

# leuB

`protein.P30125`

## Static

- Type: `protein`
- Source: `UniProt:P30125`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01033}.

## Enriched Summary

FUNCTION: Catalyzes the oxidation of 3-carboxy-2-hydroxy-4-methylpentanoate (3-isopropylmalate) to 3-carboxy-4-methyl-2-oxopentanoate. The product decarboxylates to 4-methyl-2 oxopentanoate. {ECO:0000255|HAMAP-Rule:MF_01033, ECO:0000269|PubMed:9003442}.

## Biological Role

Catalyzes (2R,3S)-3-methylmalate:NAD+ oxidoreductase (reaction.R00994), (2R,3S)-3-isopropylmalate:NAD+ oxidoreductase (reaction.R04426). Component of 3-isopropylmalate dehydrogenase (complex.ecocyc.3-ISOPROPYLMALDEHYDROG-CPLX).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the oxidation of 3-carboxy-2-hydroxy-4-methylpentanoate (3-isopropylmalate) to 3-carboxy-4-methyl-2-oxopentanoate. The product decarboxylates to 4-methyl-2 oxopentanoate. {ECO:0000255|HAMAP-Rule:MF_01033, ECO:0000269|PubMed:9003442}.

## Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00994|reaction.R00994]] `KEGG` `database` - via EC:1.1.1.85
- `catalyzes` --> [[reaction.R04426|reaction.R04426]] `KEGG` `database` - via EC:1.1.1.85
- `is_component_of` --> [[complex.ecocyc.3-ISOPROPYLMALDEHYDROG-CPLX|complex.ecocyc.3-ISOPROPYLMALDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0073|gene.b0073]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30125`
- `KEGG:ecj:JW5807;eco:b0073;`
- `GeneID:75202110;944798;`
- `GO:GO:0000287; GO:0003862; GO:0005829; GO:0009098; GO:0030145; GO:0034198; GO:0046872; GO:0051287`
- `EC:1.1.1.85`

## Notes

3-isopropylmalate dehydrogenase (EC 1.1.1.85) (3-IPM-DH) (Beta-IPM dehydrogenase) (IMDH)
