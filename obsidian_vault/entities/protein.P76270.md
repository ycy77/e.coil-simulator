---
entity_id: "protein.P76270"
entity_type: "protein"
name: "msrC"
source_database: "UniProt"
source_id: "P76270"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "msrC yebR b1832 JW1821"
---

# msrC

`protein.P76270`

## Static

- Type: `protein`
- Source: `UniProt:P76270`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible oxidation-reduction of the R-enantiomer of free methionine sulfoxide to methionine. Specific for free L-methionine-(R)-S-oxide. {ECO:0000269|PubMed:17535911}.

## Biological Role

Component of free methionine-(R)-sulfoxide reductase (complex.ecocyc.CPLX0-8217).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible oxidation-reduction of the R-enantiomer of free methionine sulfoxide to methionine. Specific for free L-methionine-(R)-S-oxide. {ECO:0000269|PubMed:17535911}.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8217|complex.ecocyc.CPLX0-8217]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1832|gene.b1832]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76270`
- `KEGG:ecj:JW1821;eco:b1832;ecoc:C3026_10440;`
- `GeneID:946086;`
- `GO:GO:0005829; GO:0033745; GO:0042803`
- `EC:1.8.4.14`

## Notes

Free methionine-R-sulfoxide reductase (fRMsr) (EC 1.8.4.14)
