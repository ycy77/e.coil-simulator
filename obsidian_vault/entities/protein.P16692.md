---
entity_id: "protein.P16692"
entity_type: "protein"
name: "phnP"
source_database: "UniProt"
source_id: "P16692"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phnP b4092 JW4053"
---

# phnP

`protein.P16692`

## Static

- Type: `protein`
- Source: `UniProt:P16692`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of the cyclic ribose-phosphate to form alpha-D-ribose 1,5-bisphosphate. {ECO:0000269|PubMed:19366688, ECO:0000269|PubMed:21341651}.

## Biological Role

Component of 5-phospho-α-D-ribosyl 1,2-cyclic phosphate phosphodiesterase (complex.ecocyc.CPLX0-7936).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of the cyclic ribose-phosphate to form alpha-D-ribose 1,5-bisphosphate. {ECO:0000269|PubMed:19366688, ECO:0000269|PubMed:21341651}.

## Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7936|complex.ecocyc.CPLX0-7936]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4092|gene.b4092]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16692`
- `KEGG:ecj:JW4053;eco:b4092;ecoc:C3026_22120;`
- `GeneID:948600;`
- `GO:GO:0019700; GO:0030145; GO:0042803; GO:0103043`
- `EC:3.1.4.55`

## Notes

Phosphoribosyl 1,2-cyclic phosphate phosphodiesterase (EC 3.1.4.55) (Phosphoribosyl cyclic phosphodiesterase)
