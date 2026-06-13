---
entity_id: "protein.P77754"
entity_type: "protein"
name: "spy"
source_database: "UniProt"
source_id: "P77754"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:21317898, ECO:0000269|PubMed:9068658, ECO:0000269|PubMed:9694902}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "spy b1743 JW1732"
---

# spy

`protein.P77754`

## Static

- Type: `protein`
- Source: `UniProt:P77754`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:21317898, ECO:0000269|PubMed:9068658, ECO:0000269|PubMed:9694902}.

## Enriched Summary

FUNCTION: An ATP-independent periplasmic chaperone, decreases protein aggregation and helps protein refolding. Binds substrate over a large region of its convex inner surface (PubMed:21317898, PubMed:24497545). Substrate protein folds while it is bound to chaperone (PubMed:26619265). Increasing Spy flexibility increases its substrate affinity and overall chaperone activity (shown for 3 different substrates) (PubMed:24497545). Protects proteins in vitro against tannin inactivation; tannins have antimicrobial activity (PubMed:21317898). Overexpression enhances the stability of otherwise unstable periplasmic proteins (PubMed:21317898). {ECO:0000269|PubMed:21317898, ECO:0000269|PubMed:24497545, ECO:0000269|PubMed:26619265}.

## Biological Role

Component of ATP-independent periplasmic chaperone Spy (complex.ecocyc.CPLX0-7923).

## Annotation

FUNCTION: An ATP-independent periplasmic chaperone, decreases protein aggregation and helps protein refolding. Binds substrate over a large region of its convex inner surface (PubMed:21317898, PubMed:24497545). Substrate protein folds while it is bound to chaperone (PubMed:26619265). Increasing Spy flexibility increases its substrate affinity and overall chaperone activity (shown for 3 different substrates) (PubMed:24497545). Protects proteins in vitro against tannin inactivation; tannins have antimicrobial activity (PubMed:21317898). Overexpression enhances the stability of otherwise unstable periplasmic proteins (PubMed:21317898). {ECO:0000269|PubMed:21317898, ECO:0000269|PubMed:24497545, ECO:0000269|PubMed:26619265}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7923|complex.ecocyc.CPLX0-7923]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1743|gene.b1743]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77754`
- `KEGG:ecj:JW1732;eco:b1743;ecoc:C3026_09960;`
- `GeneID:946253;`
- `GO:GO:0006457; GO:0030288; GO:0042803; GO:0044183; GO:0051082`

## Notes

Periplasmic chaperone Spy (Spheroplast protein Y)
