---
entity_id: "molecule.ecocyc.ssRNA-Holder"
entity_type: "small_molecule"
name: "a single-stranded RNA"
source_database: "EcoCyc"
source_id: "ssRNA-Holder"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
---

# a single-stranded RNA

`molecule.ecocyc.ssRNA-Holder`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:ssRNA-Holder`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

This class stands for general ssRNAsubstrates, to be used in general reactions such as enzymes processing mRNAs. It is not the same as the super class ssRNAs, which serves as a master class that includes all ssRNAs in the database. This class stands for general ssRNAsubstrates, to be used in general reactions such as enzymes processing mRNAs. It is not the same as the super class ssRNAs, which serves as a master class that includes all ssRNAs in the database.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Annotation

This class stands for general ssRNAsubstrates, to be used in general reactions such as enzymes processing mRNAs. It is not the same as the super class ssRNAs, which serves as a master class that includes all ssRNAs in the database.

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.2.7.7.8-RXN|reaction.ecocyc.2.7.7.8-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.2.7.7.8-RXN|reaction.ecocyc.2.7.7.8-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6527|reaction.ecocyc.RXN0-6527]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:ssRNA-Holder`
