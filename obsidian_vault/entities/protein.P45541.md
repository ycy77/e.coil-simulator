---
entity_id: "protein.P45541"
entity_type: "protein"
name: "frlC"
source_database: "UniProt"
source_id: "P45541"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "frlC yhfO yhfP b4474 JW5699"
---

# frlC

`protein.P45541`

## Static

- Type: `protein`
- Source: `UniProt:P45541`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible interconversion of fructoselysine with its C-3 epimer, psicoselysine. Allows E.coli to utilize psicoselysine for growth. Does not act on psicose or fructoselysine 6-phosphate. {ECO:0000269|PubMed:14641112}. Fructoselysine 3-epimerase catalyzes the interconversion of fructoselysine and psicoselysine . Fructoselysine 3-epimerase activity is undetectable when cells are grown on glucose; stationary phase extract of cells grown on fructoselysine or psicoselysine have an epimerase activity of 2 nmol/min per mg of protein . FrlC: "fructoselysine"

## Biological Role

Component of fructoselysine 3-epimerase (complex.ecocyc.CPLX0-3861).

## Annotation

FUNCTION: Catalyzes the reversible interconversion of fructoselysine with its C-3 epimer, psicoselysine. Allows E.coli to utilize psicoselysine for growth. Does not act on psicose or fructoselysine 6-phosphate. {ECO:0000269|PubMed:14641112}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3861|complex.ecocyc.CPLX0-3861]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## Incoming Edges (1)

- `encodes` <-- [[gene.b4474|gene.b4474]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45541`
- `KEGG:ecj:JW5699;eco:b4474;ecoc:C3026_18310;`
- `GeneID:2847758;`
- `GO:GO:0016857; GO:0042802; GO:0046348; GO:0046872`
- `EC:5.1.3.41`

## Notes

Fructoselysine 3-epimerase (EC 5.1.3.41)
