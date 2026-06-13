---
entity_id: "protein.P39315"
entity_type: "protein"
name: "qorB"
source_database: "UniProt"
source_id: "P39315"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "qorB qor2 ytfG b4211 JW4169"
---

# qorB

`protein.P39315`

## Static

- Type: `protein`
- Source: `UniProt:P39315`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Quinone oxidoreductase that may play some additional role beyond quinone reduction. Potential redox sensor protein. Overexpression induces retardation of growth. {ECO:0000269|PubMed:18455185}. QorB is an NAD(P)H:quinone oxidoreductase. EPR and kinetic studies suggest that the enzyme catalyzes the two-electron reduction of quinones using a ping-pong mechanism. Crystal structures of the enzyme alone and in complex with NADPH have been solved . QorB shows very low flavin reductase activity and ferrous iron release activity in the presence of free FAD . A qorB mutant shows no significant growth phenotype, while overexpression of qorB leads to growth retardation and lowered expression of a number of proteins involved in carbon metabolism . The gene was identified by a computational analysis as a candidate for encoding resistance to the antiobiotic CPD-9195. Resistance was confirmed by wet-lab experiments that compared the minimum inhibitory concentration (MIC) of a knock-out strain to that of the wild-type strain . QorB: "NAD(P)H-dependent quinone oxidoreductase"

## Biological Role

Catalyzes RXN0-5387 (reaction.ecocyc.RXN0-5387).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Quinone oxidoreductase that may play some additional role beyond quinone reduction. Potential redox sensor protein. Overexpression induces retardation of growth. {ECO:0000269|PubMed:18455185}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5387|reaction.ecocyc.RXN0-5387]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4211|gene.b4211]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39315`
- `KEGG:ecj:JW4169;eco:b4211;ecoc:C3026_22745;`
- `GeneID:948731;`
- `GO:GO:0005829; GO:0008753; GO:0016655; GO:0050136`
- `EC:1.6.5.2`

## Notes

Quinone oxidoreductase 2 (EC 1.6.5.2)
