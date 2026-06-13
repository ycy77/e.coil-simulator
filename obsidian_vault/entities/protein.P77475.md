---
entity_id: "protein.P77475"
entity_type: "protein"
name: "yqaB"
source_database: "UniProt"
source_id: "P77475"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yqaB b2690 JW2665"
---

# yqaB

`protein.P77475`

## Static

- Type: `protein`
- Source: `UniProt:P77475`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes strongly the dephosphorylation of fructose-1-phosphate (Fru1P) and slightly the dephosphorylation of 6-phosphogluconate (6P-Glu). It has low beta-phosphoglucomutase activity. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279}. YqaB is a sugar phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. In addition to its main fructose-1-phosphatase activity, YqaB has low β-phosphoglucomutase activity . The phosphatase activity of YqaB was first discovered in a high-throughput screen of purified proteins . No measurable sorbitol-6-phosphate phosphatase activity was detected .

## Biological Role

Catalyzes RXN0-5186 (reaction.ecocyc.RXN0-5186). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Catalyzes strongly the dephosphorylation of fructose-1-phosphate (Fru1P) and slightly the dephosphorylation of 6-phosphogluconate (6P-Glu). It has low beta-phosphoglucomutase activity. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5186|reaction.ecocyc.RXN0-5186]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2690|gene.b2690]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77475`
- `KEGG:ecj:JW2665;eco:b2690;ecoc:C3026_14810;`
- `GeneID:93779321;945776;`
- `GO:GO:0000287; GO:0005975; GO:0008801; GO:0016791; GO:0050308`
- `EC:3.1.3.-`

## Notes

Fructose-1-phosphate phosphatase YqaB (EC 3.1.3.-) (Fructose-1-phosphatase)
