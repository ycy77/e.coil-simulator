---
entity_id: "molecule.ecocyc.Protein-L-serine-or-L-threonine"
entity_type: "small_molecule"
name: "a [protein]-(L-serine/L-threonine)"
source_database: "EcoCyc"
source_id: "Protein-L-serine-or-L-threonine"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "a [protein] Ser/Thr"
  - "a [protein]-L-serine/L-threonine"
---

# a [protein]-(L-serine/L-threonine)

`molecule.ecocyc.Protein-L-serine-or-L-threonine`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Protein-L-serine-or-L-threonine`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

This generic class describes either an SER or THR within a glycoprotein. In the case of SER, R = H, in the case of THR, R = CH3. This generic class describes either an SER or THR within a glycoprotein. In the case of SER, R = H, in the case of THR, R = CH3.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Annotation

This generic class describes either an SER or THR within a glycoprotein. In the case of SER, R = H, in the case of THR, R = CH3.

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.3.1.3.16-RXN|reaction.ecocyc.3.1.3.16-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.PROTEIN-KINASE-RXN|reaction.ecocyc.PROTEIN-KINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7371|reaction.ecocyc.RXN0-7371]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:Protein-L-serine-or-L-threonine`
- `METANETX:MNXM147004`
- `METANETX:MNXM147413`
