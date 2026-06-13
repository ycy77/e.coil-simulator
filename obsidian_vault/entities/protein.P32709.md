---
entity_id: "protein.P32709"
entity_type: "protein"
name: "nrfD"
source_database: "UniProt"
source_id: "P32709"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nrfD yjcK b4073 JW4034"
---

# nrfD

`protein.P32709`

## Static

- Type: `protein`
- Source: `UniProt:P32709`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Probably involved in the transfer of electrons from the quinone pool to the type-c cytochromes. NrfD is a predicted inner membrane protein containing 8 conserved hydrophobic segments. It may be the naphthoquinol oxidase although a role as a proton pump has not been excluded .

## Biological Role

Component of putative menaquinol-cytochrome c reductase NrfCD (complex.ecocyc.CPLX0-8238).

## Annotation

FUNCTION: Probably involved in the transfer of electrons from the quinone pool to the type-c cytochromes.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8238|complex.ecocyc.CPLX0-8238]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4073|gene.b4073]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32709`
- `KEGG:ecj:JW4034;eco:b4073;ecoc:C3026_22015;`
- `GeneID:75169596;948580;`
- `GO:GO:0005886`

## Notes

Protein NrfD
