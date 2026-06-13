---
entity_id: "protein.P12996"
entity_type: "protein"
name: "bioB"
source_database: "UniProt"
source_id: "P12996"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bioB b0775 JW0758"
---

# bioB

`protein.P12996`

## Static

- Type: `protein`
- Source: `UniProt:P12996`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of dethiobiotin (DTB) to biotin by the insertion of a sulfur atom into dethiobiotin via a radical-based mechanism. {ECO:0000269|PubMed:8142361}.

## Biological Role

Component of biotin synthase (complex.ecocyc.BIOTIN-SYN-CPLX).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of dethiobiotin (DTB) to biotin by the insertion of a sulfur atom into dethiobiotin via a radical-based mechanism. {ECO:0000269|PubMed:8142361}.

## Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.BIOTIN-SYN-CPLX|complex.ecocyc.BIOTIN-SYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0775|gene.b0775]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P12996`
- `KEGG:ecj:JW0758;eco:b0775;ecoc:C3026_04925;`
- `GeneID:93776655;945370;`
- `GO:GO:0004076; GO:0005506; GO:0009102; GO:0042803; GO:0051537; GO:0051539`
- `EC:2.8.1.6`

## Notes

Biotin synthase (EC 2.8.1.6) (Biotin synthetase)
