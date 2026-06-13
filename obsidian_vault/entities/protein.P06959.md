---
entity_id: "protein.P06959"
entity_type: "protein"
name: "aceF"
source_database: "UniProt"
source_id: "P06959"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aceF b0115 JW0111"
---

# aceF

`protein.P06959`

## Static

- Type: `protein`
- Source: `UniProt:P06959`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The pyruvate dehydrogenase complex catalyzes the overall conversion of pyruvate to acetyl-CoA and CO(2). It contains multiple copies of three enzymatic components: pyruvate dehydrogenase (E1), dihydrolipoamide acetyltransferase (E2) and lipoamide dehydrogenase (E3). AceF, the "E2" or "core" component of the pyruvate dehydrogenase multienzyme complex, assembles into a 24-subunit cube . The E1 dimers of the pyruvate dehydrogenase multienzyme complex catalyze acetylation of the lipoate moieties that are attached to the E2 subunits . The E2 subunits (AceF) also exhibit transacetylation . The structure of the pyruvate dehydrogenase multienzyme complex and the spatial distribution of the E2 lipoyl moieties have been studied by scanning transmission electron microscopy . AceF is a soluble cytoplasmic protein that contains an acidic N-terminal lipoyl domain with three roughly 100-residue repeats, each with a lipoyl modification motif and an alanine- and proline-rich segment . A single lipoyl domain suffices with respect to enzyme activity and protein function . The lipoyl domains appear to function independently of each other . Lipoyl modification sites (of sequence GDKASME, lipoylated on the lysine) of all three lipoyl domain repeats appear to be fully lipoylated, and all of these lipoyl groups are subject to acetylation by the pyruvate dehydrogenase complex...

## Biological Role

Catalyzes RXN0-1133 (reaction.ecocyc.RXN0-1133). Component of pyruvate dehydrogenase (complex.ecocyc.PYRUVATEDEH-CPLX).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)

## Annotation

FUNCTION: The pyruvate dehydrogenase complex catalyzes the overall conversion of pyruvate to acetyl-CoA and CO(2). It contains multiple copies of three enzymatic components: pyruvate dehydrogenase (E1), dihydrolipoamide acetyltransferase (E2) and lipoamide dehydrogenase (E3).

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1133|reaction.ecocyc.RXN0-1133]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.PYRUVATEDEH-CPLX|complex.ecocyc.PYRUVATEDEH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=24 | EcoCyc protcplxs.col coefficient=24

## Incoming Edges (1)

- `encodes` <-- [[gene.b0115|gene.b0115]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06959`
- `KEGG:ecj:JW0111;eco:b0115;ecoc:C3026_00480;`
- `GeneID:944794;`
- `GO:GO:0004742; GO:0005737; GO:0006086; GO:0031405; GO:0042867; GO:0045254; GO:0097532`
- `EC:2.3.1.12`

## Notes

Dihydrolipoyllysine-residue acetyltransferase component of pyruvate dehydrogenase complex (EC 2.3.1.12) (Dihydrolipoamide acetyltransferase component of pyruvate dehydrogenase complex) (E2)
