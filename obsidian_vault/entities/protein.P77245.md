---
entity_id: "protein.P77245"
entity_type: "protein"
name: "murR"
source_database: "UniProt"
source_id: "P77245"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "murR yfeT b2427 JW2420"
---

# murR

`protein.P77245`

## Static

- Type: `protein`
- Source: `UniProt:P77245`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Represses the expression of the murPQ operon involved in the uptake and degradation of N-acetylmuramic acid (MurNAc). Binds to two adjacent inverted repeats within the operator region. MurNAc 6-phosphate, the substrate of MurQ, is the specific inducer that weakens binding of MurR to the operator. Also represses its own transcription. {ECO:0000269|PubMed:18723630}.

## Biological Role

Component of DNA-binding transcriptional dual regulator MurR (complex.ecocyc.CPLX0-7745), MurR-N-acetyl-D-muramate 6-phosphate (complex.ecocyc.CPLX0-7746), MurR-N-acetylglucosamine-6-phosphate (complex.ecocyc.CPLX0-9152).

## Annotation

FUNCTION: Represses the expression of the murPQ operon involved in the uptake and degradation of N-acetylmuramic acid (MurNAc). Binds to two adjacent inverted repeats within the operator region. MurNAc 6-phosphate, the substrate of MurQ, is the specific inducer that weakens binding of MurR to the operator. Also represses its own transcription. {ECO:0000269|PubMed:18723630}.

## Outgoing Edges (7)

- `activates` --> [[gene.b2427|gene.b2427]] `RegulonDB` `S` - regulator=MurR; target=murR; function=-+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7745|complex.ecocyc.CPLX0-7745]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `is_component_of` --> [[complex.ecocyc.CPLX0-7746|complex.ecocyc.CPLX0-7746]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-9152|complex.ecocyc.CPLX0-9152]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b2427|gene.b2427]] `RegulonDB` `S` - regulator=MurR; target=murR; function=-+
- `represses` --> [[gene.b2428|gene.b2428]] `RegulonDB` `S` - regulator=MurR; target=murQ; function=-
- `represses` --> [[gene.b2429|gene.b2429]] `RegulonDB` `S` - regulator=MurR; target=murP; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2427|gene.b2427]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77245`
- `KEGG:ecj:JW2420;eco:b2427;ecoc:C3026_13485;`
- `GeneID:946568;`
- `GO:GO:0003677; GO:0003700; GO:0006355; GO:0043470; GO:0045892; GO:0097173; GO:0097367; GO:1901135`

## Notes

HTH-type transcriptional regulator MurR (MurPQ operon repressor)
