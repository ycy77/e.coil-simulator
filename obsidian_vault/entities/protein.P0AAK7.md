---
entity_id: "protein.P0AAK7"
entity_type: "protein"
name: "nrfC"
source_database: "UniProt"
source_id: "P0AAK7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nrfC yjcJ b4072 JW4033"
---

# nrfC

`protein.P0AAK7`

## Static

- Type: `protein`
- Source: `UniProt:P0AAK7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probably involved in the transfer of electrons from the quinone pool to the type-c cytochromes. NrfC is predicted to be membrane bound. It contains 16 conserved cysteine residues and thus is likely to be an Fe-S protein. NrfC contains a double arginine signal sequence .

## Biological Role

Component of putative menaquinol-cytochrome c reductase NrfCD (complex.ecocyc.CPLX0-8238).

## Annotation

FUNCTION: Probably involved in the transfer of electrons from the quinone pool to the type-c cytochromes.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8238|complex.ecocyc.CPLX0-8238]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4072|gene.b4072]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAK7`
- `KEGG:ecj:JW4033;eco:b4072;ecoc:C3026_22010;`
- `GeneID:93777757;948581;`
- `GO:GO:0042279; GO:0046872; GO:0051539`

## Notes

Protein NrfC
