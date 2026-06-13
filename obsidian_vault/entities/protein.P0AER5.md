---
entity_id: "protein.P0AER5"
entity_type: "protein"
name: "gltK"
source_database: "UniProt"
source_id: "P0AER5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gltK b0653 JW0648"
---

# gltK

`protein.P0AER5`

## Static

- Type: `protein`
- Source: `UniProt:P0AER5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex GltIJKL involved in glutamate and aspartate uptake. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000305|PubMed:9593292}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from P.luminescens strain TTO1 across the inner membrane to the cytoplasm, where CdiA has a toxic effect. Toxin transport is strain-specific, mutations in this gene do not confer resistance to several other tested CdiA toxins. {ECO:0000269|PubMed:26305955}. GltK is the predicted integral membrane subunit of a glutamate/aspartate ABC transporter complex (see . GltK has been implicated in the import of specific toxins of contact-dependent growth inhibition (CDI) systems in gram-negative bacteria; gltK transposon insertion mutants and gltK in-frame deletion mutants are resistant to the CdiA-CTTT01 toxin; inner membrane proteins such as GltK are thought to act as receptors which bring the nuclease domain of CDI toxins into close proximity with the inner membrane of target cells .

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

- `encodes` <-- [[gene.b0653|gene.b0653]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AER5`
- `KEGG:ecj:JW0648;eco:b0653;ecoc:C3026_03265;`
- `GeneID:93776829;947354;`
- `GO:GO:0005886; GO:0006865; GO:0016020; GO:0022857; GO:0055052; GO:0098712; GO:0140009`

## Notes

Glutamate/aspartate import permease protein GltK
