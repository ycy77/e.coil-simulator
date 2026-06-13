---
entity_id: "molecule.ecocyc.mRNA-Holder"
entity_type: "small_molecule"
name: "an mRNA"
source_database: "EcoCyc"
source_id: "mRNA-Holder"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
---

# an mRNA

`molecule.ecocyc.mRNA-Holder`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:mRNA-Holder`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

This class stands for general mRNA substrates, to be used in general reactions such as mRNA modification. It is not the same as the super class mRNAs mRNAs, which includes all mRNAs in the database. This class stands for general mRNA substrates, to be used in general reactions such as mRNA modification. It is not the same as the super class mRNAs mRNAs, which includes all mRNAs in the database.

## Biological Role

Consumed as substrate in 3 reaction(s).

## Annotation

This class stands for general mRNA substrates, to be used in general reactions such as mRNA modification. It is not the same as the super class mRNAs mRNAs, which includes all mRNAs in the database.

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.ecocyc.3.1.27.6-RXN|reaction.ecocyc.3.1.27.6-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4701|reaction.ecocyc.RXN0-4701]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5509|reaction.ecocyc.RXN0-5509]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:mRNA-Holder`
