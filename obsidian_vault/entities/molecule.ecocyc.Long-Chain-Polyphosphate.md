---
entity_id: "molecule.ecocyc.Long-Chain-Polyphosphate"
entity_type: "small_molecule"
name: "long chain polyphosphate"
source_database: "EcoCyc"
source_id: "Long-Chain-Polyphosphate"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "(phosphate)(n)"
  - "(phosphate)(n+1)"
  - "(phosphate)(n-1)"
  - "(polyphosphate)(n)"
  - "(polyphosphate)(n+1)"
  - "(polyphosphate)(n-1)"
  - "PolyP"
  - "inorganic polyphosphate"
  - "(polyphosphate)(n-2)"
---

# long chain polyphosphate

`molecule.ecocyc.Long-Chain-Polyphosphate`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Long-Chain-Polyphosphate`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

This class stands for long chain polyphosphates, which are linear polymers of tens or hundreds of orthophosphate (Pi) residues linked in the same manner as the two high-energy phosphoanhydride bonds in ATP. They are substrates of different enzymes, such as exophosphatases (e.g. Ppx in E. coli and the polyphosphate-dependent glucokinases (EC 2.7.1.63). This class stands for long chain polyphosphates, which are linear polymers of tens or hundreds of orthophosphate (Pi) residues linked in the same manner as the two high-energy phosphoanhydride bonds in ATP. They are substrates of different enzymes, such as exophosphatases (e.g. Ppx in E. coli and the polyphosphate-dependent glucokinases (EC 2.7.1.63).

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Annotation

This class stands for long chain polyphosphates, which are linear polymers of tens or hundreds of orthophosphate (Pi) residues linked in the same manner as the two high-energy phosphoanhydride bonds in ATP. They are substrates of different enzymes, such as exophosphatases (e.g. Ppx in E. coli and the polyphosphate-dependent glucokinases (EC 2.7.1.63).

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.EXOPOLYPHOSPHATASE-RXN|reaction.ecocyc.EXOPOLYPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.POLYPHOSPHATE-KINASE-RXN|reaction.ecocyc.POLYPHOSPHATE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.EXOPOLYPHOSPHATASE-RXN|reaction.ecocyc.EXOPOLYPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.POLYPHOSPHATE-KINASE-RXN|reaction.ecocyc.POLYPHOSPHATE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:Long-Chain-Polyphosphate`
- `SEED:cpd27425`
- `METANETX:MNXM6321`
