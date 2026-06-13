---
entity_id: "protein.P0ABH9"
entity_type: "protein"
name: "clpA"
source_database: "UniProt"
source_id: "P0ABH9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "clpA lopD b0882 JW0866"
---

# clpA

`protein.P0ABH9`

## Static

- Type: `protein`
- Source: `UniProt:P0ABH9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: ATP-dependent specificity component of the ClpAP protease. It directs the protease to specific substrates. It has unfoldase activity. The primary function of the ClpA-ClpP complex appears to be the degradation of unfolded or abnormal proteins.

## Biological Role

Component of ClpAP (complex.ecocyc.CPLX0-3104), ClpAXP (complex.ecocyc.CPLX0-3108), ClpA ATP-dependent protease specificity component and chaperone (complex.ecocyc.CPLX0-881).

## Annotation

FUNCTION: ATP-dependent specificity component of the ClpAP protease. It directs the protease to specific substrates. It has unfoldase activity. The primary function of the ClpA-ClpP complex appears to be the degradation of unfolded or abnormal proteins.

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3104|complex.ecocyc.CPLX0-3104]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` --> [[complex.ecocyc.CPLX0-3108|complex.ecocyc.CPLX0-3108]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6
- `is_component_of` --> [[complex.ecocyc.CPLX0-881|complex.ecocyc.CPLX0-881]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0882|gene.b0882]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABH9`
- `KEGG:ecj:JW0866;eco:b0882;ecoc:C3026_05475;`
- `GeneID:93776538;945764;`
- `GO:GO:0004176; GO:0005524; GO:0005737; GO:0005829; GO:0006508; GO:0006515; GO:0006979; GO:0009368; GO:0016887; GO:0034605; GO:0043335`

## Notes

ATP-dependent Clp protease ATP-binding subunit ClpA
