---
entity_id: "protein.P32720"
entity_type: "protein"
name: "alsC"
source_database: "UniProt"
source_id: "P32720"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "alsC yjcV b4086 JW4047"
---

# alsC

`protein.P32720`

## Static

- Type: `protein`
- Source: `UniProt:P32720`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of the binding-protein-dependent transport system AlsBAC for D-allose; probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:9401019}. alsC encodes the predicted integral membrane subunit of a D-allose ABC transporter . The alsC gene appears to be defective in E. coli K-12 strain W3110 which does not use D-allose as a carbon source

## Biological Role

Component of D-allose ABC transporter (complex.ecocyc.ABC-42-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the binding-protein-dependent transport system AlsBAC for D-allose; probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:9401019}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-42-CPLX|complex.ecocyc.ABC-42-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4086|gene.b4086]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32720`
- `KEGG:ecj:JW4047;eco:b4086;ecoc:C3026_22090;`
- `GeneID:948594;`
- `GO:GO:0005886; GO:0015752; GO:0015754; GO:0016020; GO:0022857; GO:0055052`

## Notes

D-allose transport system permease protein AlsC
