---
entity_id: "protein.P31460"
entity_type: "protein"
name: "dgoR"
source_database: "UniProt"
source_id: "P31460"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dgoR yidW b4479 JW5627"
---

# dgoR

`protein.P31460`

## Static

- Type: `protein`
- Source: `UniProt:P31460`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the regulation of D-galactonate metabolism (PubMed:211976, PubMed:30455279). Represses the expression of the dgoRKADT operon by binding to two closely spaced inverted repeats in the cis-acting element, which overlap with the D-galactonate responsive dgo promoter (PubMed:30455279). Employs a derepression mechanism using D-galactonate as a specific effector molecule (PubMed:30455279, PubMed:33068046, PubMed:33224125). {ECO:0000269|PubMed:211976, ECO:0000269|PubMed:30455279, ECO:0000269|PubMed:33068046, ECO:0000269|PubMed:33224125}.

## Biological Role

Component of DNA-binding transcriptional repressor DgoR (complex.ecocyc.CPLX0-8578).

## Annotation

FUNCTION: Involved in the regulation of D-galactonate metabolism (PubMed:211976, PubMed:30455279). Represses the expression of the dgoRKADT operon by binding to two closely spaced inverted repeats in the cis-acting element, which overlap with the D-galactonate responsive dgo promoter (PubMed:30455279). Employs a derepression mechanism using D-galactonate as a specific effector molecule (PubMed:30455279, PubMed:33068046, PubMed:33224125). {ECO:0000269|PubMed:211976, ECO:0000269|PubMed:30455279, ECO:0000269|PubMed:33068046, ECO:0000269|PubMed:33224125}.

## Outgoing Edges (6)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8578|complex.ecocyc.CPLX0-8578]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b3691|gene.b3691]] `RegulonDB` `C` - regulator=DgoR; target=dgoT; function=-
- `represses` --> [[gene.b3693|gene.b3693]] `RegulonDB` `C` - regulator=DgoR; target=dgoK; function=-
- `represses` --> [[gene.b4477|gene.b4477]] `RegulonDB` `C` - regulator=DgoR; target=dgoA; function=-
- `represses` --> [[gene.b4478|gene.b4478]] `RegulonDB` `C` - regulator=DgoR; target=dgoD; function=-
- `represses` --> [[gene.b4479|gene.b4479]] `RegulonDB` `C` - regulator=DgoR; target=dgoR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4479|gene.b4479]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31460`
- `KEGG:ecj:JW5627;eco:b4479;ecoc:C3026_20030;`
- `GeneID:2847767;89518592;93778436;`
- `GO:GO:0000976; GO:0000987; GO:0001217; GO:0003677; GO:0003700; GO:0006355; GO:0042802; GO:0046872; GO:0098531; GO:2000143`

## Notes

Galactonate operon transcriptional repressor (HTH-type transcriptional repressor DgoR)
