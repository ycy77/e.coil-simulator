---
entity_id: "protein.P19319"
entity_type: "protein"
name: "narZ"
source_database: "UniProt"
source_id: "P19319"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "narZ b1468 JW1463"
---

# narZ

`protein.P19319`

## Static

- Type: `protein`
- Source: `UniProt:P19319`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein.

## Enriched Summary

FUNCTION: This is a second nitrate reductase enzyme which can substitute for the NRA enzyme and allows E.coli to use nitrate as an electron acceptor during anaerobic growth.; FUNCTION: The alpha chain is the actual site of nitrate reduction. narZ encodes the α subunit of nitrate reductase Z; sequence analysis shows it has 76% identity with narG (which encodes the α subunit of nitrate reductase A); it is predicted to be the site of nitrate reduction and to contain the molybdenum cofactor .

## Biological Role

Component of nitrate reductase Z (complex.ecocyc.NITRATREDUCTZ-CPLX).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: This is a second nitrate reductase enzyme which can substitute for the NRA enzyme and allows E.coli to use nitrate as an electron acceptor during anaerobic growth.; FUNCTION: The alpha chain is the actual site of nitrate reduction.

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.NITRATREDUCTZ-CPLX|complex.ecocyc.NITRATREDUCTZ-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1468|gene.b1468]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P19319`
- `KEGG:ecj:JW1463;eco:b1468;ecoc:C3026_08520;`
- `GeneID:945999;`
- `GO:GO:0005886; GO:0008940; GO:0009061; GO:0009325; GO:0016020; GO:0019645; GO:0042126; GO:0042128; GO:0043546; GO:0046872; GO:0051539; GO:0160182`
- `EC:1.7.5.1`

## Notes

Respiratory nitrate reductase 2 alpha chain (EC 1.7.5.1)
