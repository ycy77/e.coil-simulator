---
entity_id: "molecule.C00638"
entity_type: "small_molecule"
name: "Long-chain fatty acid"
source_database: "KEGG"
source_id: "C00638"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Long-chain fatty acid"
  - "Higher fatty acid"
---

# Long-chain fatty acid

`molecule.C00638`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00638`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Long-chain fatty acid; Higher fatty acid EcoCyc common name: a long-chain fatty acid. The term "fatty acid" was originally coined to describe aliphatic monocarboxylic acids derived from or contained in esterified form in an animal or vegetable fat, oil or wax. However, over the years the term has been expanded to refer to additional, shorter monocarboxylic acids with an aliphatic tail such as PROPIONATE and BUTYRIC_ACID (but not the shorter FORMATE and ACET). The length of a fatty acid is determined by the length of the longest carbon chain, including the carbon of the carboxy group. Common natural fatty acids usually have an even number of carbons in the longest chain and can be either saturated or unsaturated. In many organisms they are often modified by branching, hydroxylation, methylation, epoxidation and other types of modifications. Inside living cells fatty acids are rarely found in free form. They are usually bound to coenzyme A or acyl-carrier proteins, or form part of Triacylglycerides triglycerides, Phospholipids phospholipids, Lipopolysaccharides lipopolysaccharides, and Cholesterol-esters cholesterol esters. Many enzymes that act on fatty acids, as well as the corresponding Fatty-Acyl-CoAs "fatty acyl-CoAs", alcohols, and aldehydes, have evolved to recognize substrates with a limited range of chain lengths...

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)

## Annotation

KEGG compound: Long-chain fatty acid; Higher fatty acid

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)

## Outgoing Edges (4)

- `activates` --> [[reaction.ecocyc.RXN-11496|reaction.ecocyc.RXN-11496]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.RXN0-1802|reaction.ecocyc.RXN0-1802]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00390|reaction.R00390]] `KEGG` `database` - C00002 + C00638 + C00010 <=> C00020 + C00013 + C02843
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1802|reaction.ecocyc.RXN0-1802]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00638`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
