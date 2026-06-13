---
entity_id: "protein.P32156"
entity_type: "protein"
name: "rhaM"
source_database: "UniProt"
source_id: "P32156"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rhaM yiiL b3901 JW3872"
---

# rhaM

`protein.P32156`

## Static

- Type: `protein`
- Source: `UniProt:P32156`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Involved in the anomeric conversion of L-rhamnose. {ECO:0000269|PubMed:15060078}. Utilizing NMR techniques, RhaM was shown to catalyze the anomeric conversion of rhamnose . The enzyme has a preference for binding the β-anomer . A crystal structure of RhaM in complex with L-rhamnose was solved at 1.8 Å resolution. Analysis of the catalytic activity of mutants in predicted active site residues allowed the authors to propose a possible catalytic mechanism . A rhaM deletion mutant has a decreased growth rate when grown on low concentrations of L-rhamnose .

## Biological Role

Component of L-rhamnose mutarotase (complex.ecocyc.CPLX0-7649).

## Annotation

FUNCTION: Involved in the anomeric conversion of L-rhamnose. {ECO:0000269|PubMed:15060078}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7649|complex.ecocyc.CPLX0-7649]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3901|gene.b3901]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32156`
- `KEGG:ecj:JW3872;eco:b3901;ecoc:C3026_21090;`
- `GeneID:75174142;948402;`
- `GO:GO:0005737; GO:0016857; GO:0019301; GO:0042803; GO:0062192`
- `EC:5.1.3.32`

## Notes

L-rhamnose mutarotase (EC 5.1.3.32) (Rhamnose 1-epimerase) (Type-3 mutarotase)
