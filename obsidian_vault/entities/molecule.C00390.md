---
entity_id: "molecule.C00390"
entity_type: "small_molecule"
name: "Ubiquinol"
source_database: "KEGG"
source_id: "C00390"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Ubiquinol"
  - "QH2"
  - "CoQH2"
  - "Ubiquinol-n"
---

# Ubiquinol

`molecule.C00390`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00390`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Ubiquinol; QH2; CoQH2; Ubiquinol-n EcoCyc common name: a ubiquinol. The ubiquinones are a group of lipid-soluble benzoquinones involved in electron transport. Their structures have a variable length side chain, which consists of one to twelve mono-unsaturated trans-isoprenoids units, with ten units being the most common in animals. TAX-4932 has 6 units, TAX-303 has 7, TAX-83333 has 8, TAX-10090 has 9, and TAX-9606 has 10 . The terms ubiquinone/ubiquinol refer to the oxidized/reduced forms, and are often used interchangeably. The forms are readily interconvertable. Ubiquinone is also known as coenzyme Q, or just Q. The names are often followed by the number of the prenoid units in the side chain (e.g. Q-8), or the number of carbons in the chain. For example, the name Q-8 may be substituted with ubiiquinone(40). Since these carbons occur in repeating units of five, these number are multiples of 5.

## Biological Role

Consumed as substrate in 8 reaction(s). Produced in 15 reaction(s).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)

## Annotation

KEGG compound: Ubiquinol; QH2; CoQH2; Ubiquinol-n

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)

## Outgoing Edges (23)

- `is_product_of` --> [[reaction.R03145|reaction.R03145]] `KEGG` `database` - C00022 + C00399 + C00001 <=> C00033 + C00390 + C00011
- `is_product_of` --> [[reaction.R11945|reaction.R11945]] `KEGG` `database` - C00399 + C00004 + C00080 + 4 C00080 <=> C00390 + C00003 + 4 C00080
- `is_product_of` --> [[reaction.ecocyc.DLACTDEHYDROGFAD-RXN|reaction.ecocyc.DLACTDEHYDROGFAD-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.NADH-DEHYDROG-A-RXN|reaction.ecocyc.NADH-DEHYDROG-A-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-11496|reaction.ecocyc.RXN-11496]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21483|reaction.ecocyc.RXN-21483]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5244|reaction.ecocyc.RXN0-5244]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5260|reaction.ecocyc.RXN0-5260]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5330|reaction.ecocyc.RXN0-5330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6373|reaction.ecocyc.RXN0-6373]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6491|reaction.ecocyc.RXN0-6491]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7008|reaction.ecocyc.RXN0-7008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7421|reaction.ecocyc.RXN0-7421]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN|reaction.ecocyc.SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-237|reaction.ecocyc.TRANS-RXN0-237]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R11335|reaction.R11335]] `KEGG` `database` - 2 C00390 + C00007 + 8 C00080 <=> 2 C00399 + 2 C00001 + 8 C00080
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18584|reaction.ecocyc.RXN-18584]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19778|reaction.ecocyc.RXN-19778]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20148|reaction.ecocyc.RXN-20148]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5266|reaction.ecocyc.RXN0-5266]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5268|reaction.ecocyc.RXN0-5268]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6369|reaction.ecocyc.RXN0-6369]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7124|reaction.ecocyc.RXN0-7124]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00390`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
