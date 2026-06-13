---
entity_id: "protein.P22106"
entity_type: "protein"
name: "asnB"
source_database: "UniProt"
source_id: "P22106"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "asnB b0674 JW0660"
---

# asnB

`protein.P22106`

## Static

- Type: `protein`
- Source: `UniProt:P22106`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent conversion of aspartate into asparagine, using glutamine as a source of nitrogen. Can also use ammonia as the nitrogen source in vitro, albeit with lower efficiency. As nucleotide substrates, ATP and dATP are utilized at a similar rate in both the glutamine- and ammonia-dependent reactions, whereas GTP utilization is only 15% that of ATP, and CTP, UTP, ITP and XTP are very poor or not substrates. Also exhibits glutaminase activity. {ECO:0000269|PubMed:20853825, ECO:0000269|PubMed:6102982, ECO:0000269|PubMed:7907328}.

## Biological Role

Catalyzes L-glutamine amidohydrolase (reaction.R00256), L-aspartate:ammonia ligase (AMP-forming) (reaction.R00483), L-aspartate:L-glutamine amido-ligase (AMP-forming) (reaction.R00578). Component of asparagine synthetase B (complex.ecocyc.ASNSYNB-CPLX).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the ATP-dependent conversion of aspartate into asparagine, using glutamine as a source of nitrogen. Can also use ammonia as the nitrogen source in vitro, albeit with lower efficiency. As nucleotide substrates, ATP and dATP are utilized at a similar rate in both the glutamine- and ammonia-dependent reactions, whereas GTP utilization is only 15% that of ATP, and CTP, UTP, ITP and XTP are very poor or not substrates. Also exhibits glutaminase activity. {ECO:0000269|PubMed:20853825, ECO:0000269|PubMed:6102982, ECO:0000269|PubMed:7907328}.

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00256|reaction.R00256]] `KEGG` `database` - via EC:6.3.5.4
- `catalyzes` --> [[reaction.R00483|reaction.R00483]] `KEGG` `database` - via EC:6.3.5.4
- `catalyzes` --> [[reaction.R00578|reaction.R00578]] `KEGG` `database` - via EC:6.3.5.4
- `is_component_of` --> [[complex.ecocyc.ASNSYNB-CPLX|complex.ecocyc.ASNSYNB-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0674|gene.b0674]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P22106`
- `KEGG:ecj:JW0660;eco:b0674;ecoc:C3026_03350;`
- `GeneID:89519974;945281;`
- `GO:GO:0004066; GO:0004071; GO:0005524; GO:0005737; GO:0005829; GO:0006529; GO:0006541; GO:0008652; GO:0009063; GO:0016597; GO:0042802; GO:0042803; GO:0070981`
- `EC:6.3.5.4`

## Notes

Asparagine synthetase B [glutamine-hydrolyzing] (AS-B) (EC 6.3.5.4)
