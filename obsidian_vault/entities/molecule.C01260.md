---
entity_id: "molecule.C01260"
entity_type: "small_molecule"
name: "P1,P4-Bis(5'-adenosyl)tetraphosphate"
source_database: "KEGG"
source_id: "C01260"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "P1,P4-Bis(5'-adenosyl)tetraphosphate"
  - "AppppA"
---

# P1,P4-Bis(5'-adenosyl)tetraphosphate

`molecule.C01260`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01260`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: P1,P4-Bis(5'-adenosyl)tetraphosphate; AppppA EcoCyc common name: P1,P4-bis(5'-adenosyl) tetraphosphate. Several important intracellular and extracellular signaling functions have been ascribed to the diadenosine compounds ADENOSINE5TRIPHOSPHO5ADENOSINE, ADENOSYL-P4, CPD0-1137 and CPD-11932 .

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: P1,P4-Bis(5'-adenosyl)tetraphosphate; AppppA

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN0-5208|reaction.ecocyc.RXN0-5208]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00125|reaction.R00125]] `KEGG` `database` - C01260 + C00001 <=> 2 C00008
- `is_substrate_of` --> [[reaction.ecocyc.3.6.1.41-RXN|reaction.ecocyc.3.6.1.41-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01260`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
