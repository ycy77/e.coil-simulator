---
entity_id: "protein.P77308"
entity_type: "protein"
name: "ddpB"
source_database: "UniProt"
source_id: "P77308"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ddpB yddR b1486 JW1481"
---

# ddpB

`protein.P77308`

## Static

- Type: `protein`
- Source: `UniProt:P77308`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex DdpABCDF, which is probably involved in D,D-dipeptide transport. Probably responsible for the translocation of the substrate across the membrane. DdpB is one of two predicted inner membrane subunits of a putative ATP-dependent D,D-dipeptide uptake system that may function to import D-alanyl-D-alanine for use as an energy source under starvation conditions . DdpB is predicted to be an inner membrane protein with 6 transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm . ddp: D,D-dipeptide

## Biological Role

Component of putative D,D-dipeptide ABC transporter (complex.ecocyc.ABC-59-CPLX).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex DdpABCDF, which is probably involved in D,D-dipeptide transport. Probably responsible for the translocation of the substrate across the membrane.

## Pathways

- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-59-CPLX|complex.ecocyc.ABC-59-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1486|gene.b1486]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77308`
- `KEGG:ecj:JW1481;eco:b1486;ecoc:C3026_08610;`
- `GeneID:75203196;946044;`
- `GO:GO:0005886; GO:0015031; GO:0016020; GO:0042938; GO:0055052; GO:0071916`

## Notes

Probable D,D-dipeptide transport system permease protein DdpB
