---
entity_id: "molecule.ecocyc.Quaternary-Amines"
entity_type: "small_molecule"
name: "a quaternary ammonium compound"
source_database: "EcoCyc"
source_id: "Quaternary-Amines"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "a quaternary ammonium ion"
  - "a quaternary amine"
---

# a quaternary ammonium compound

`molecule.ecocyc.Quaternary-Amines`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Quaternary-Amines`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

A quaternary ammonium compound is a derivative of ammonium in which all four of the hydrogens bonded to nitrogen have been replaced with univalent (usually organyl) groups. A quaternary ammonium compound is a derivative of ammonium in which all four of the hydrogens bonded to nitrogen have been replaced with univalent (usually organyl) groups.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Annotation

A quaternary ammonium compound is a derivative of ammonium in which all four of the hydrogens bonded to nitrogen have been replaced with univalent (usually organyl) groups.

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.RXN-8638|reaction.ecocyc.RXN-8638]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8638|reaction.ecocyc.RXN-8638]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ABC-26-CPLX|complex.ecocyc.ABC-26-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:Quaternary-Amines`
- `METANETX:MNXM80081`
- `CHEBI:35267`
