---
entity_id: "molecule.C00033"
entity_type: "small_molecule"
name: "Acetate"
source_database: "KEGG"
source_id: "C00033"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Acetate"
  - "Acetic acid"
  - "Ethanoic acid"
---

# Acetate

`molecule.C00033`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00033`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Acetate; Acetic acid; Ethanoic acid EcoCyc common name: acetic acid. This compound stands strictly for the conjugate acid of ACET. It only exists at low pH.

## Biological Role

Consumed as substrate in 12 reaction(s). Produced in 30 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Annotation

KEGG compound: Acetate; Acetic acid; Ethanoic acid

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Outgoing Edges (48)

- `is_product_of` --> [[reaction.R00317|reaction.R00317]] `KEGG` `database` - C00227 + C00001 <=> C00033 + C00009
- `is_product_of` --> [[reaction.R00669|reaction.R00669]] `KEGG` `database` - C00437 + C00001 <=> C00033 + C00077
- `is_product_of` --> [[reaction.R01323|reaction.R01323]] `KEGG` `database` - C00024 + C00158 <=> C00033 + C00566
- `is_product_of` --> [[reaction.R03132|reaction.R03132]] `KEGG` `database` - C00979 + C00320 <=> C05824 + C00033
- `is_product_of` --> [[reaction.R03145|reaction.R03145]] `KEGG` `database` - C00022 + C00399 + C00001 <=> C00033 + C00390 + C00011
- `is_product_of` --> [[reaction.R06893|reaction.R06893]] `KEGG` `database` - C13636 + C00001 <=> C00530 + C00033
- `is_product_of` --> [[reaction.R09107|reaction.R09107]] `KEGG` `database` - C15532 + C00001 <=> C00033 + C00327
- `is_product_of` --> [[reaction.R12635|reaction.R12635]] `KEGG` `database` - C22293 + C00001 <=> C00475 + C00033
- `is_product_of` --> [[reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN|reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ACETYLESTERASE-RXN|reaction.ecocyc.ACETYLESTERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ACETYLORNDEACET-RXN|reaction.ecocyc.ACETYLORNDEACET-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ACSERLY-RXN|reaction.ecocyc.ACSERLY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.CITLY-RXN|reaction.ecocyc.CITLY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.CITRATE-PRO-3S-LYASE-THIOLESTERASE-RXN|reaction.ecocyc.CITRATE-PRO-3S-LYASE-THIOLESTERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.CITTRANS-RXN|reaction.ecocyc.CITTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.NAG6PDEACET-RXN|reaction.ecocyc.NAG6PDEACET-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-11496|reaction.ecocyc.RXN-11496]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-13182|reaction.ecocyc.RXN-13182]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21270|reaction.ecocyc.RXN-21270]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22319|reaction.ecocyc.RXN-22319]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1981|reaction.ecocyc.RXN0-1981]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-3341|reaction.ecocyc.RXN0-3341]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-3962|reaction.ecocyc.RXN0-3962]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5414|reaction.ecocyc.RXN0-5414]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7013|reaction.ecocyc.RXN0-7013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7075|reaction.ecocyc.RXN0-7075]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7391|reaction.ecocyc.RXN0-7391]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SULFOCYS-RXN|reaction.ecocyc.SULFOCYS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-571|reaction.ecocyc.TRANS-RXN0-571]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.UDPACYLGLCNACDEACETYL-RXN|reaction.ecocyc.UDPACYLGLCNACDEACETYL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00235|reaction.R00235]] `KEGG` `database` - C00002 + C00033 + C00010 <=> C00020 + C00013 + C00024
- `is_substrate_of` --> [[reaction.R00315|reaction.R00315]] `KEGG` `database` - C00002 + C00033 <=> C00008 + C00227
- `is_substrate_of` --> [[reaction.R00316|reaction.R00316]] `KEGG` `database` - C00002 + C00033 <=> C00013 + C05993
- `is_substrate_of` --> [[reaction.R00393|reaction.R00393]] `KEGG` `database` - C00040 + C00033 <=> C02403 + C00024
- `is_substrate_of` --> [[reaction.ecocyc.ACECOATRANS-RXN|reaction.ecocyc.ACECOATRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ACETATE--COA-LIGASE-RXN|reaction.ecocyc.ACETATE--COA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ACETATEKIN-RXN|reaction.ecocyc.ACETATEKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CITC-RXN|reaction.ecocyc.CITC-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22319|reaction.ecocyc.RXN-22319]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1981|reaction.ecocyc.RXN0-1981]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6375|reaction.ecocyc.RXN0-6375]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-571|reaction.ecocyc.TRANS-RXN0-571]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.3-DEHYDROQUINATE-DEHYDRATASE-RXN|reaction.ecocyc.3-DEHYDROQUINATE-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ACETYLORNDEACET-RXN|reaction.ecocyc.ACETYLORNDEACET-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.KDGALDOL-RXN|reaction.ecocyc.KDGALDOL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.NAG6PDEACET-RXN|reaction.ecocyc.NAG6PDEACET-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.R524-RXN|reaction.ecocyc.R524-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN|reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.CPLX0-7955|complex.ecocyc.CPLX0-7955]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AC98|protein.P0AC98]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00033`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
