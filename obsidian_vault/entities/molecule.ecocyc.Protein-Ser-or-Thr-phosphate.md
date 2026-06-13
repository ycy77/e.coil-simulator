---
entity_id: "molecule.ecocyc.Protein-Ser-or-Thr-phosphate"
entity_type: "small_molecule"
name: "a [protein] (L-serine/L-threonine) phosphate"
source_database: "EcoCyc"
source_id: "Protein-Ser-or-Thr-phosphate"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
---

# a [protein] (L-serine/L-threonine) phosphate

`molecule.ecocyc.Protein-Ser-or-Thr-phosphate`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Protein-Ser-or-Thr-phosphate`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

This generic class describes either a phosphorylated SER or phosphorylated THR within a protein. In the case of SER, R = H, in the case of THR, R = CH3. This generic class describes either a phosphorylated SER or phosphorylated THR within a protein. In the case of SER, R = H, in the case of THR, R = CH3.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Annotation

This generic class describes either a phosphorylated SER or phosphorylated THR within a protein. In the case of SER, R = H, in the case of THR, R = CH3.

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.PROTEIN-KINASE-RXN|reaction.ecocyc.PROTEIN-KINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.3.1.3.16-RXN|reaction.ecocyc.3.1.3.16-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:Protein-Ser-or-Thr-phosphate`
- `METANETX:MNXM147953`
