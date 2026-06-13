---
entity_id: "protein.P76113"
entity_type: "protein"
name: "curA"
source_database: "UniProt"
source_id: "P76113"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "curA yncB b1449 JW5907"
---

# curA

`protein.P76113`

## Static

- Type: `protein`
- Source: `UniProt:P76113`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the metal-independent reduction of curcumin to dihydrocurcumin (DHC) as an intermediate product, followed by further reduction to tetrahydrocurcumin (THC) as an end product. It also acts on 3-octene-2-one, 3-hepten-2-one, resveratrol, and trans-2-octenal. {ECO:0000269|PubMed:21467222}.

## Biological Role

Component of NADPH-dependent curcumin/dihydrocurcumin reductase (complex.ecocyc.CPLX0-7927).

## Annotation

FUNCTION: Catalyzes the metal-independent reduction of curcumin to dihydrocurcumin (DHC) as an intermediate product, followed by further reduction to tetrahydrocurcumin (THC) as an end product. It also acts on 3-octene-2-one, 3-hepten-2-one, resveratrol, and trans-2-octenal. {ECO:0000269|PubMed:21467222}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7927|complex.ecocyc.CPLX0-7927]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1449|gene.b1449]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76113`
- `KEGG:ecj:JW5907;eco:b1449;ecoc:C3026_08430;`
- `GeneID:946012;`
- `GO:GO:0052849`
- `EC:1.3.1.n3`

## Notes

NADPH-dependent curcumin reductase (EC 1.3.1.n3) (NADPH-dependent curcumin/dihydrocurcumin reductase)
