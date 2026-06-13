---
entity_id: "protein.P45767"
entity_type: "protein"
name: "yhdX"
source_database: "UniProt"
source_id: "P45767"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00441}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yhdX b3269 JW5544"
---

# yhdX

`protein.P45767`

## Static

- Type: `protein`
- Source: `UniProt:P45767`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00441}.

## Enriched Summary

FUNCTION: Probably part of the binding-protein-dependent transport system YdhWXYZ for an amino acid; probably responsible for the translocation of the substrate across the membrane. YhdX is one of two predicted inner membrane subunits of a putative ABC transporter .

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

- `encodes` <-- [[gene.b3269|gene.b3269]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45767`
- `KEGG:ecj:JW5544;eco:b3269;ecoc:C3026_17785;`
- `GeneID:75173440;947765;`
- `GO:GO:0005886; GO:0006865; GO:0015833; GO:0016020; GO:0022857; GO:0055052`

## Notes

Putative amino-acid ABC transporter permease protein YhdX
