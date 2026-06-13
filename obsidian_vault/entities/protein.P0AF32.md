---
entity_id: "protein.P0AF32"
entity_type: "protein"
name: "narV"
source_database: "UniProt"
source_id: "P0AF32"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "narV b1465 JW1460"
---

# narV

`protein.P0AF32`

## Static

- Type: `protein`
- Source: `UniProt:P0AF32`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: This is a second nitrate reductase enzyme which can substitute for the NRA enzyme and allows E.coli to use nitrate as an electron acceptor during anaerobic growth. The gamma chain is a membrane-embedded heme-iron unit resembling cytochrome b, which transfers electrons from quinones to the beta subunit. narV encodes the γ subunit of nitrate reductase Z - it has 68% identity with narI (encoding the γ subunit of nitrate reductase A) but 87% similarity at the protein level; it is predicted to be the heme b binding subunit which transfers electrons from the quinone pool to the β subunit .

## Biological Role

Component of nitrate reductase Z (complex.ecocyc.NITRATREDUCTZ-CPLX).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: This is a second nitrate reductase enzyme which can substitute for the NRA enzyme and allows E.coli to use nitrate as an electron acceptor during anaerobic growth. The gamma chain is a membrane-embedded heme-iron unit resembling cytochrome b, which transfers electrons from quinones to the beta subunit.

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.NITRATREDUCTZ-CPLX|complex.ecocyc.NITRATREDUCTZ-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1465|gene.b1465]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF32`
- `KEGG:ecj:JW1460;eco:b1465;ecoc:C3026_08505;`
- `GeneID:75171551;946029;`
- `GO:GO:0005886; GO:0008940; GO:0009055; GO:0009061; GO:0009325; GO:0016020; GO:0019645; GO:0020037; GO:0042126; GO:0042128; GO:0046872; GO:0160182`
- `EC:1.7.5.1`

## Notes

Respiratory nitrate reductase 2 gamma chain (EC 1.7.5.1)
