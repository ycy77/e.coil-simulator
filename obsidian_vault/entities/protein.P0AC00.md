---
entity_id: "protein.P0AC00"
entity_type: "protein"
name: "frlB"
source_database: "UniProt"
source_id: "P0AC00"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "frlB yhfN b3371 JW5700"
---

# frlB

`protein.P0AC00`

## Static

- Type: `protein`
- Source: `UniProt:P0AC00`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible conversion of fructoselysine 6-phosphate to glucose 6-phosphate and lysine (PubMed:12147680). Functions in a fructoselysine degradation pathway that allows E.coli to grow on fructoselysine or psicoselysine (PubMed:14641112). {ECO:0000269|PubMed:12147680, ECO:0000269|PubMed:14641112}. Fructoselysine 6-phosphate deglycase, which acts in fructoselysine degradation, is an FrlB dodecamer . The fructoselysine 6-phosphate deglycase reaction is reversible in vitro, but is catalyzed in the direction of formation of glucose 6-phosphate and lysine in vivo . A detailed reaction mechanism is discussed . Fructoselysine 6-phosphate deglycase activity is undetectable when cells are grown on glucose; stationary phase extract of cells grown on fructoselysine or psicoselysine have a deglycase activity of 20 nmol/min per mg of protein . An frlA mutant is unable to grow on 20mM fructoselysine or psicoselysine as the sole source of carbon . FrlB: "fructoselysine"

## Biological Role

Component of fructoselysine 6-phosphate deglycase (complex.ecocyc.CPLX0-821).

## Annotation

FUNCTION: Catalyzes the reversible conversion of fructoselysine 6-phosphate to glucose 6-phosphate and lysine (PubMed:12147680). Functions in a fructoselysine degradation pathway that allows E.coli to grow on fructoselysine or psicoselysine (PubMed:14641112). {ECO:0000269|PubMed:12147680, ECO:0000269|PubMed:14641112}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-821|complex.ecocyc.CPLX0-821]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=12

## Incoming Edges (1)

- `encodes` <-- [[gene.b3371|gene.b3371]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC00`
- `KEGG:ecj:JW5700;eco:b3371;ecoc:C3026_18305;`
- `GeneID:947875;`
- `GO:GO:0004360; GO:0006002; GO:0006047; GO:0006487; GO:0016787; GO:0016836; GO:0042802; GO:0097367`
- `EC:3.5.-.-`

## Notes

Fructoselysine 6-phosphate deglycase (EC 3.5.-.-)
