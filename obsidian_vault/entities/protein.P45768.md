---
entity_id: "protein.P45768"
entity_type: "protein"
name: "yhdY"
source_database: "UniProt"
source_id: "P45768"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yhdY b3270 JW5545"
---

# yhdY

`protein.P45768`

## Static

- Type: `protein`
- Source: `UniProt:P45768`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Probably part of the binding-protein-dependent transport system YdhWXYZ for an amino acid; probably responsible for the translocation of the substrate across the membrane. YhdY is one of two predicted inner membrane subunits of a putative ABC transporter . YhdY is predicted to be an inner membrane protein with 8 transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm .

## Biological Role

Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-52-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Probably part of the binding-protein-dependent transport system YdhWXYZ for an amino acid; probably responsible for the translocation of the substrate across the membrane.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-52-CPLX|complex.ecocyc.ABC-52-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3270|gene.b3270]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45768`
- `KEGG:ecj:JW5545;eco:b3270;ecoc:C3026_17790;`
- `GeneID:947764;`
- `GO:GO:0005886; GO:0006865; GO:0015833; GO:0016020; GO:0022857; GO:0055052`

## Notes

Inner membrane amino-acid ABC transporter permease protein YhdY
