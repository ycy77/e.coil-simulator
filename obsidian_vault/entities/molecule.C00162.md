---
entity_id: "molecule.C00162"
entity_type: "small_molecule"
name: "Fatty acid"
source_database: "KEGG"
source_id: "C00162"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Fatty acid"
---

# Fatty acid

`molecule.C00162`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00162`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Fatty acid EcoCyc common name: a fatty acid. The term "fatty acid" was originally coined to describe aliphatic monocarboxylic acids derived from or contained in esterified form in an animal or vegetable fat, oil or wax. However, over the years the term has been expanded to refer to additional, shorter monocarboxylic acids with an aliphatic tail such as PROPIONATE and BUTYRIC_ACID (but not the shorter FORMATE and ACET). The length of a fatty acid is determined by the length of the longest carbon chain, including the carbon of the carboxy group. Common natural fatty acids usually have an even number of carbons in the longest chain and can be either saturated or unsaturated. In many organisms they are often modified by branching, hydroxylation, methylation, epoxidation and other types of modifications. Inside living cells fatty acids are rarely found in free form. They are usually bound to coenzyme A or acyl-carrier proteins, or form part of Triacylglycerides triglycerides, Phospholipids phospholipids, Lipopolysaccharides lipopolysaccharides, and Cholesterol-esters cholesterol esters. Many enzymes that act on fatty acids, as well as the corresponding Fatty-Acyl-CoAs "fatty acyl-CoAs", Fatty-Alcohols alcohols, and Fatty-Aldehydes aldehydes, have evolved to recognize substrates with a limited range of chain lengths...

## Biological Role

Produced in 7 reaction(s).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)

## Annotation

KEGG compound: Fatty acid

## Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.R01309|reaction.R01309]] `KEGG` `database` - C00157 + 2 C00001 <=> C00670 + 2 C00162
- `is_product_of` --> [[reaction.R01315|reaction.R01315]] `KEGG` `database` - C00157 + C00001 <=> C04230 + C00162
- `is_product_of` --> [[reaction.R01316|reaction.R01316]] `KEGG` `database` - C00157 + C00001 <=> C04233 + C00162
- `is_product_of` --> [[reaction.R03416|reaction.R03416]] `KEGG` `database` - C04438 + C00001 <=> C00162 + C01233
- `is_product_of` --> [[reaction.R03417|reaction.R03417]] `KEGG` `database` - C05973 + C00001 <=> C00162 + C01233
- `is_product_of` --> [[reaction.ecocyc.RXN0-6725|reaction.ecocyc.RXN0-6725]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6952|reaction.ecocyc.RXN0-6952]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00162`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
