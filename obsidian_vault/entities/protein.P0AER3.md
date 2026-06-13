---
entity_id: "protein.P0AER3"
entity_type: "protein"
name: "gltJ"
source_database: "UniProt"
source_id: "P0AER3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gltJ b0654 JW0649"
---

# gltJ

`protein.P0AER3`

## Static

- Type: `protein`
- Source: `UniProt:P0AER3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex GltIJKL involved in glutamate and aspartate uptake. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000305|PubMed:9593292}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from P.luminescens strain TTO1 across the inner membrane to the cytoplasm, where CdiA has a toxic effect. Toxin transport is strain-specific, mutations in this gene do not confer resistance to several other tested CdiA toxins. {ECO:0000269|PubMed:26305955}. GltJ is the predicted integral membrane subunit of a glutamate/aspartate ABC transporter complex (see .

## Biological Role

Component of glutamate / aspartate ABC transporter (complex.ecocyc.ABC-13-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex GltIJKL involved in glutamate and aspartate uptake. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000305|PubMed:9593292}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from P.luminescens strain TTO1 across the inner membrane to the cytoplasm, where CdiA has a toxic effect. Toxin transport is strain-specific, mutations in this gene do not confer resistance to several other tested CdiA toxins. {ECO:0000269|PubMed:26305955}.

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-13-CPLX|complex.ecocyc.ABC-13-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0654|gene.b0654]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AER3`
- `KEGG:ecj:JW0649;eco:b0654;ecoc:C3026_03270;`
- `GeneID:75170657;75204985;945443;`
- `GO:GO:0005886; GO:0006865; GO:0016020; GO:0022857; GO:0055052; GO:0098712; GO:0140009`

## Notes

Glutamate/aspartate import permease protein GltJ
