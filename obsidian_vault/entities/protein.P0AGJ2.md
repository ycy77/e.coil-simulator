---
entity_id: "protein.P0AGJ2"
entity_type: "protein"
name: "trmH"
source_database: "UniProt"
source_id: "P0AGJ2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trmH spoU b3651 JW3626"
---

# trmH

`protein.P0AGJ2`

## Static

- Type: `protein`
- Source: `UniProt:P0AGJ2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the 2'-O methylation of guanosine at position 18 in tRNA. Type II methylase, which methylates only a subset of tRNA species. {ECO:0000269|PubMed:9321663}.

## Biological Role

Catalyzes S-adenosyl-L-methionine:tRNA (guanosine-2'-O-)-methyltransferase (reaction.R02917). Component of tRNA (Gm18) 2'-O-methyltransferase (complex.ecocyc.CPLX0-11183).

## Annotation

FUNCTION: Catalyzes the 2'-O methylation of guanosine at position 18 in tRNA. Type II methylase, which methylates only a subset of tRNA species. {ECO:0000269|PubMed:9321663}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R02917|reaction.R02917]] `KEGG` `database` - via EC:2.1.1.34
- `is_component_of` --> [[complex.ecocyc.CPLX0-11183|complex.ecocyc.CPLX0-11183]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3651|gene.b3651]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGJ2`
- `KEGG:ecj:JW3626;eco:b3651;ecoc:C3026_19780;`
- `GeneID:93778366;948161;`
- `GO:GO:0000049; GO:0002938; GO:0030488; GO:0141100`
- `EC:2.1.1.34`

## Notes

tRNA (guanosine(18)-2'-O)-methyltransferase (EC 2.1.1.34) (tRNA [Gm18] methyltransferase)
