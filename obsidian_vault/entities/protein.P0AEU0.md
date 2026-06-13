---
entity_id: "protein.P0AEU0"
entity_type: "protein"
name: "hisJ"
source_database: "UniProt"
source_id: "P0AEU0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000250|UniProtKB:P02910}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hisJ b2309 JW2306"
---

# hisJ

`protein.P0AEU0`

## Static

- Type: `protein`
- Source: `UniProt:P0AEU0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000250|UniProtKB:P02910}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex HisPMQJ involved in histidine transport (By similarity). Binds histidine (By similarity). Interacts with HisQMP and stimulates ATPase activity of HisP, which results in histidine translocation (By similarity). {ECO:0000250|UniProtKB:P02910}. HisJ is the periplasmic binding protein of an ATP-dependent histidine uptake system. HisJ, purified in the presence of histidine and crystallized, contains two globular domains of similar arrangement connected by a two strand hinge; histidine binds in a deep cleft between the two domains and is held in place by hydrogen bonds, Van der Waals contacts and salt links . Molecular dynamics simulations suggest that HisJ employs a 'Venus fly-trap' type movement where the protein transitions from an open to closed conformation and provide support for the contention that apo-HisJ can transition to a closed form even in the absence of ligand .

## Biological Role

Component of histidine ABC transporter (complex.ecocyc.ABC-14-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex HisPMQJ involved in histidine transport (By similarity). Binds histidine (By similarity). Interacts with HisQMP and stimulates ATPase activity of HisP, which results in histidine translocation (By similarity). {ECO:0000250|UniProtKB:P02910}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-14-CPLX|complex.ecocyc.ABC-14-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2309|gene.b2309]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEU0`
- `KEGG:ecj:JW2306;eco:b2309;ecoc:C3026_12875;`
- `GeneID:86947252;93774865;945309;`
- `GO:GO:0016020; GO:0016597; GO:0030288; GO:0055052; GO:1903810`

## Notes

Histidine-binding periplasmic protein (HBP)
