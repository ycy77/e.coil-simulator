---
entity_id: "molecule.ecocyc.Glycerophosphodiesters"
entity_type: "small_molecule"
name: "an sn-glycerophosphodiester"
source_database: "EcoCyc"
source_id: "Glycerophosphodiesters"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "glycerophosphodiester"
  - "glycerol-3-P-OR"
---

# an sn-glycerophosphodiester

`molecule.ecocyc.Glycerophosphodiesters`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Glycerophosphodiesters`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

EcoCyc compound Glycerophosphodiesters

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Annotation

EcoCyc compound Glycerophosphodiesters

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-573|reaction.ecocyc.TRANS-RXN0-573]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GLYCPDIESTER-RXN|reaction.ecocyc.GLYCPDIESTER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-573|reaction.ecocyc.TRANS-RXN0-573]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ABC-34-CPLX|complex.ecocyc.ABC-34-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:Glycerophosphodiesters`
- `CHEBI:26706`
- `CHEBI:83408`
- `SEED:cpd02000`
- `METANETX:MNXM163400`
- `LIGAND-CPD:C03120`
