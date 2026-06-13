---
entity_id: "molecule.C00226"
entity_type: "small_molecule"
name: "Primary alcohol"
source_database: "KEGG"
source_id: "C00226"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Primary alcohol"
  - "1-Alcohol"
---

# Primary alcohol

`molecule.C00226`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00226`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Primary alcohol; 1-Alcohol EcoCyc common name: a primary alcohol. A primary alcohol is a compound in which a hydroxy group, -OH, is attached to a saturated carbon atom that is connected to no more than one other carbon atom. Primary alcohols are also classified based on their length. Short-Chain-Primary-Alcohols "Short-chain primary alcohols" have alkyl chains with fewer than six carbons. Medium-Chain-Primary-Alcohols "Medium-chain primary alcohols" have alkyl chains of 6-12 carbons. Long-Chain-Primary-Alcohols "Long-chain primary alcohols" (also known as fatty alcohols) have alkyl chains of 13-22 carbons. Very-Long-Chain-Primary-Alcohols "Very long-chain primary alcohols" have alkyl chains of 23 carbons or longer.

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)

## Annotation

KEGG compound: Primary alcohol; 1-Alcohol

## Pathways

- `eco00071` Fatty acid degradation (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.R00623|reaction.R00623]] `KEGG` `database` - C00226 + C00003 <=> C00071 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00625|reaction.R00625]] `KEGG` `database` - C00226 + C00006 <=> C00071 + C00005 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.ALCOHOL-DEHYDROG-GENERIC-RXN|reaction.ecocyc.ALCOHOL-DEHYDROG-GENERIC-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00226`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
