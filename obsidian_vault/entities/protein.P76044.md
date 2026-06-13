---
entity_id: "protein.P76044"
entity_type: "protein"
name: "ycjR"
source_database: "UniProt"
source_id: "P76044"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycjR b1314 JW5202"
---

# ycjR

`protein.P76044`

## Static

- Type: `protein`
- Source: `UniProt:P76044`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the epimerization at C4 of 3-dehydro-D-gulosides leading to 3-dehydro-D-glucosides. Probably functions in a metabolic pathway that transforms D-gulosides to D-glucosides. Can use methyl alpha-3-dehydro-D-glucoside and methyl beta-3-dehydro-D-glucoside as substrates in vitro. However, the actual specific physiological substrates for this metabolic pathway are unknown. Cannot act on D-psicose, D-fructose, D-tagatose, D-sorbose, L-xylulose, or L-ribulose. {ECO:0000269|PubMed:30742415}.

## Biological Role

Component of 3-dehydro-D-guloside 4-epimerase (complex.ecocyc.CPLX0-8554).

## Annotation

FUNCTION: Catalyzes the epimerization at C4 of 3-dehydro-D-gulosides leading to 3-dehydro-D-glucosides. Probably functions in a metabolic pathway that transforms D-gulosides to D-glucosides. Can use methyl alpha-3-dehydro-D-glucoside and methyl beta-3-dehydro-D-glucoside as substrates in vitro. However, the actual specific physiological substrates for this metabolic pathway are unknown. Cannot act on D-psicose, D-fructose, D-tagatose, D-sorbose, L-xylulose, or L-ribulose. {ECO:0000269|PubMed:30742415}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8554|complex.ecocyc.CPLX0-8554]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1314|gene.b1314]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76044`
- `KEGG:ecj:JW5202;eco:b1314;ecoc:C3026_07700;`
- `GeneID:947427;`
- `GO:GO:0005829; GO:0016857; GO:0030145; GO:0042802`
- `EC:5.1.3.-`

## Notes

3-dehydro-D-guloside 4-epimerase (EC 5.1.3.-) (3-keto-D-guloside 4-epimerase)
