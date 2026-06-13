---
entity_id: "protein.P77268"
entity_type: "protein"
name: "ddpD"
source_database: "UniProt"
source_id: "P77268"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ddpD yddP b1484 JW1479"
---

# ddpD

`protein.P77268`

## Static

- Type: `protein`
- Source: `UniProt:P77268`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex DdpABCDF, which is probably involved in D,D-dipeptide transport (PubMed:9097039). Probably responsible for energy coupling to the transport system. {ECO:0000305|PubMed:9097039}. DdpD is one of two predicted ATP-binding subunits of a D,D-dipeptide uptake system that may function to import D-alanyl-D-alanine for use as an energy source under starvation conditions . ddp: D,D-dipeptide

## Biological Role

Component of putative D,D-dipeptide ABC transporter (complex.ecocyc.ABC-59-CPLX).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex DdpABCDF, which is probably involved in D,D-dipeptide transport (PubMed:9097039). Probably responsible for energy coupling to the transport system. {ECO:0000305|PubMed:9097039}.

## Pathways

- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-59-CPLX|complex.ecocyc.ABC-59-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1484|gene.b1484]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77268`
- `KEGG:ecj:JW1479;eco:b1484;ecoc:C3026_08600;`
- `GeneID:946002;`
- `GO:GO:0005524; GO:0015031; GO:0015640; GO:0016020; GO:0016887; GO:0042938; GO:0055052`

## Notes

Probable D,D-dipeptide transport ATP-binding protein DdpD
