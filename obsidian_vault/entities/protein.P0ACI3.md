---
entity_id: "protein.P0ACI3"
entity_type: "protein"
name: "xylR"
source_database: "UniProt"
source_id: "P0ACI3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xylR b3569 JW3541"
---

# xylR

`protein.P0ACI3`

## Static

- Type: `protein`
- Source: `UniProt:P0ACI3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Regulatory protein for the xylBAFGHR operon.

## Biological Role

Component of DNA-binding transcriptional dual regulator XylR-α-D-xylopyranose (complex.ecocyc.MONOMER0-165).

## Annotation

FUNCTION: Regulatory protein for the xylBAFGHR operon.

## Outgoing Edges (10)

- `activates` --> [[gene.b3564|gene.b3564]] `RegulonDB` `S` - regulator=XylR; target=xylB; function=+
- `activates` --> [[gene.b3565|gene.b3565]] `RegulonDB` `S` - regulator=XylR; target=xylA; function=+
- `activates` --> [[gene.b3566|gene.b3566]] `RegulonDB` `S` - regulator=XylR; target=xylF; function=+
- `activates` --> [[gene.b3567|gene.b3567]] `RegulonDB` `S` - regulator=XylR; target=xylG; function=+
- `activates` --> [[gene.b3568|gene.b3568]] `RegulonDB` `S` - regulator=XylR; target=xylH; function=+
- `activates` --> [[gene.b3569|gene.b3569]] `RegulonDB` `S` - regulator=XylR; target=xylR; function=+
- `activates` --> [[gene.b4031|gene.b4031]] `RegulonDB` `C` - regulator=XylR; target=xylE; function=+
- `activates` --> [[gene.b4834|gene.b4834]] `RegulonDB` `S` - regulator=XylR; target=xylZ; function=+
- `is_component_of` --> [[complex.ecocyc.MONOMER0-165|complex.ecocyc.MONOMER0-165]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0064|gene.b0064]] `RegulonDB` `S` - regulator=XylR; target=araC; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3569|gene.b3569]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACI3`
- `KEGG:ecj:JW3541;eco:b3569;ecoc:C3026_19350;`
- `GeneID:75203010;948086;`
- `GO:GO:0000976; GO:0003700; GO:0006355`

## Notes

Xylose operon regulatory protein
