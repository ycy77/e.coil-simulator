---
entity_id: "molecule.C02843"
entity_type: "small_molecule"
name: "Long-chain acyl-CoA"
source_database: "KEGG"
source_id: "C02843"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Long-chain acyl-CoA"
  - "Long-chain-fatty acyl-CoA"
---

# Long-chain acyl-CoA

`molecule.C02843`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02843`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Long-chain acyl-CoA; Long-chain-fatty acyl-CoA EcoCyc common name: a long-chain fatty acyl-CoA. Fatty acyl-CoAs are ACYL-COA "acyl-CoAs" derived from Fatty-Acids "fatty acids". Many enzymes that act on fatty acids, as well as the corresponding Fatty-Acyl-CoAs "fatty acyl-CoAs", alcohols, and aldehydes, have evolved to recognize substrates with a limited range of chain lengths. To classify these enzymes, it is helpful to divide the substrates into smaller groups based on their chain length. The following subgroups have been defined: Short-Chain-Acyl-CoAs "Short-chain acyl-CoAs" are derived from Short-chain-fatty-acids "fatty acids that have 3-5 carbons in the longest chain". Medium-Chain-Acyl-CoAs "Medium-chain acyl-CoAs" are derived from Medium-chain-fatty-acids "fatty acids that have 6-12 carbons in the longest chain". Long-Chain-Acyl-CoAs "Long-chain acyl-CoAs" are derived from Long-Chain-Fatty-Acids "fatty acids that have 13-22 carbons in the longest chain". VERY-LONG-CHAIN-FATTY-ACYL-COA "Very-long-chain fatty acyl-CoAs" are derived from Very-long-chain-fatty-acids "fatty acids that have 23-27 carbons in the longest chain". Ultra-Long-Chain-Acyl-CoAs "Ultra-long-chain fatty acyl-CoAs" are derived from Ultra-long-chain-fatty-acids "fatty acids that have more than 27 carbons in the longest chain".

## Biological Role

Produced in 1 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00074` Mycolic acid biosynthesis (KEGG)

## Annotation

KEGG compound: Long-chain acyl-CoA; Long-chain-fatty acyl-CoA

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00074` Mycolic acid biosynthesis (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R00390|reaction.R00390]] `KEGG` `database` - C00002 + C00638 + C00010 <=> C00020 + C00013 + C02843
- `represses` --> [[reaction.ecocyc.GLYC3PDEHYDROGBIOSYN-RXN|reaction.ecocyc.GLYC3PDEHYDROGBIOSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02843`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
