---
entity_id: "protein.P27431"
entity_type: "protein"
name: "roxA"
source_database: "UniProt"
source_id: "P27431"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "roxA ycfD b1128 JW1114"
---

# roxA

`protein.P27431`

## Static

- Type: `protein`
- Source: `UniProt:P27431`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Growth-regulating oxygenase that catalyzes the hydroxylation of ribosomal protein uL16 on 'Arg-81'. {ECO:0000269|PubMed:23103944, ECO:0000269|PubMed:24530688}.

## Biological Role

Component of 50S ribosomal protein L16-arginine 3-hydroxylase (complex.ecocyc.CPLX0-8112).

## Annotation

FUNCTION: Growth-regulating oxygenase that catalyzes the hydroxylation of ribosomal protein uL16 on 'Arg-81'. {ECO:0000269|PubMed:23103944, ECO:0000269|PubMed:24530688}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8112|complex.ecocyc.CPLX0-8112]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1128|gene.b1128]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27431`
- `KEGG:ecj:JW1114;eco:b1128;ecoc:C3026_06790;`
- `GeneID:75203714;945391;`
- `GO:GO:0008198; GO:0016706; GO:0042803; GO:0043687`
- `EC:1.14.11.47`

## Notes

Ribosomal protein uL16 3-hydroxylase (EC 1.14.11.47) (Ribosomal oxygenase RoxA) (ROX)
