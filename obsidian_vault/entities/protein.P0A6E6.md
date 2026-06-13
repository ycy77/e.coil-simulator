---
entity_id: "protein.P0A6E6"
entity_type: "protein"
name: "atpC"
source_database: "UniProt"
source_id: "P0A6E6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:21778229}; Peripheral membrane protein {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:21778229}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "atpC papG uncC b3731 JW3709"
---

# atpC

`protein.P0A6E6`

## Static

- Type: `protein`
- Source: `UniProt:P0A6E6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:21778229}; Peripheral membrane protein {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:21778229}.

## Enriched Summary

FUNCTION: Produces ATP from ADP in the presence of a proton gradient across the membrane. The epsilon subunit appears to play an important role in coupling the catalytic site events with proton translocation in association with the gamma subunit. The coupling involves conformational changes and probable translocations of one or both subunits. This subunit is also required for binding of the F1 complex to the Fo complex.

## Biological Role

Component of ATP synthase / thiamin triphosphate synthase (complex.ecocyc.ATPSYN-CPLX), ATP synthase F1 complex (complex.ecocyc.F-1-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Produces ATP from ADP in the presence of a proton gradient across the membrane.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ATPSYN-CPLX|complex.ecocyc.ATPSYN-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.F-1-CPLX|complex.ecocyc.F-1-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3731|gene.b3731]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6E6`
- `KEGG:ecj:JW3709;eco:b3731;ecoc:C3026_20220;`
- `GeneID:86861839;948245;`
- `GO:GO:0005524; GO:0005886; GO:0015986; GO:0042777; GO:0045259; GO:0046933`

## Notes

ATP synthase epsilon chain (ATP synthase F1 sector epsilon subunit) (F-ATPase epsilon subunit)
