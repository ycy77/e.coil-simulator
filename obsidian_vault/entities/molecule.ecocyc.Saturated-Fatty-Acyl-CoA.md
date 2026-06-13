---
entity_id: "molecule.ecocyc.Saturated-Fatty-Acyl-CoA"
entity_type: "small_molecule"
name: "a 2,3,4-saturated fatty acyl CoA"
source_database: "EcoCyc"
source_id: "Saturated-Fatty-Acyl-CoA"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
---

# a 2,3,4-saturated fatty acyl CoA

`molecule.ecocyc.Saturated-Fatty-Acyl-CoA`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Saturated-Fatty-Acyl-CoA`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

This class describes ACYL-COA "acyl-CoAs" that do not contain any double bonds in the 2, 3, and 4 positions. Acyl-CoAs are oxoacids that have been activated by CO-A. They are often classified by the length of their acyl moiety. This class includes the following sub-classes: Short-Chain-234-Saturated-acyl-CoAs "Short-chain 2,3,4-saturated fatty acyl-CoAs" are derived from Short-chain-fatty-acids "2,3,4-saturated fatty acids with aliphatic chains shorter than 6 carbons". Medium-Chain-234-Saturated-acyl-CoAs "Medium-chain 2,3,4-saturated fatty acyl-CoAs" are derived from Medium-chain-fatty-acids "fatty acids with aliphatic chains of 6-12 carbons". Long-Chain-234-Saturated-acyl-CoAs "Long-chain 2,3,4-saturated fatty acyl-CoAs" are derived from Long-Chain-234-Saturated-Fatty-Acids "2,3,4-saturated fatty acids with aliphatic chains of 13-22 carbons". Very-long-Chain-234-Saturated-acyl-CoAs "Very-long-chain 2,3,4-saturated fatty acyl-CoAs" are derived from Very-long-chain-fatty-acids "fatty acids with aliphatic chains of 23 carbons or longer". This class describes ACYL-COA "acyl-CoAs" that do not contain any double bonds in the 2, 3, and 4 positions. Acyl-CoAs are oxoacids that have been activated by CO-A. They are often classified by the length of their acyl moiety...

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 2 reaction(s).

## Annotation

This class describes ACYL-COA "acyl-CoAs" that do not contain any double bonds in the 2, 3, and 4 positions. Acyl-CoAs are oxoacids that have been activated by CO-A. They are often classified by the length of their acyl moiety. This class includes the following sub-classes: Short-Chain-234-Saturated-acyl-CoAs "Short-chain 2,3,4-saturated fatty acyl-CoAs" are derived from Short-chain-fatty-acids "2,3,4-saturated fatty acids with aliphatic chains shorter than 6 carbons". Medium-Chain-234-Saturated-acyl-CoAs "Medium-chain 2,3,4-saturated fatty acyl-CoAs" are derived from Medium-chain-fatty-acids "fatty acids with aliphatic chains of 6-12 carbons". Long-Chain-234-Saturated-acyl-CoAs "Long-chain 2,3,4-saturated fatty acyl-CoAs" are derived from Long-Chain-234-Saturated-Fatty-Acids "2,3,4-saturated fatty acids with aliphatic chains of 13-22 carbons". Very-long-Chain-234-Saturated-acyl-CoAs "Very-long-chain 2,3,4-saturated fatty acyl-CoAs" are derived from Very-long-chain-fatty-acids "fatty acids with aliphatic chains of 23 carbons or longer".

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.ecocyc.ACYLCOASYN-RXN|reaction.ecocyc.ACYLCOASYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-623|reaction.ecocyc.TRANS-RXN0-623]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ACECOATRANS-RXN|reaction.ecocyc.ACECOATRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ACYLCOADEHYDROG-RXN|reaction.ecocyc.ACYLCOADEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.KETOACYLCOATHIOL-RXN|reaction.ecocyc.KETOACYLCOATHIOL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.THIOESTER-RXN|reaction.ecocyc.THIOESTER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANSENOYLCOARED-RXN|reaction.ecocyc.TRANSENOYLCOARED-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.TRANSENOYLCOARED-RXN|reaction.ecocyc.TRANSENOYLCOARED-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:Saturated-Fatty-Acyl-CoA`
- `SEED:cpd28168`
- `METANETX:MNXM96076`
