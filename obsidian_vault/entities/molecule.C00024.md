---
entity_id: "molecule.C00024"
entity_type: "small_molecule"
name: "Acetyl-CoA"
source_database: "KEGG"
source_id: "C00024"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Acetyl-CoA"
  - "Acetyl coenzyme A"
---

# Acetyl-CoA

`molecule.C00024`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00024`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Acetyl-CoA; Acetyl coenzyme A

## Biological Role

Consumed as substrate in 71 reaction(s). Produced in 15 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)
- `eco00984` Steroid degradation (KEGG)

## Annotation

KEGG compound: Acetyl-CoA; Acetyl coenzyme A

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)
- `eco00984` Steroid degradation (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Outgoing Edges (94)

- `activates` --> [[reaction.ecocyc.CITSYN-RXN|reaction.ecocyc.CITSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.PEPCARBOX-RXN|reaction.ecocyc.PEPCARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00228|reaction.R00228]] `KEGG` `database` - C00084 + C00010 + C00003 <=> C00024 + C00004 + C00080
- `is_product_of` --> [[reaction.R00235|reaction.R00235]] `KEGG` `database` - C00002 + C00033 + C00010 <=> C00020 + C00013 + C00024
- `is_product_of` --> [[reaction.R00236|reaction.R00236]] `KEGG` `database` - C05993 + C00010 <=> C00020 + C00024
- `is_product_of` --> [[reaction.R00351|reaction.R00351]] `KEGG` `database` - C00158 + C00010 <=> C00024 + C00001 + C00036
- `is_product_of` --> [[reaction.R00354|reaction.R00354]] `KEGG` `database` - C00566 <=> C00024 + C00036
- `is_product_of` --> [[reaction.R00393|reaction.R00393]] `KEGG` `database` - C00040 + C00033 <=> C02403 + C00024
- `is_product_of` --> [[reaction.R00472|reaction.R00472]] `KEGG` `database` - C00149 + C00010 <=> C00024 + C00001 + C00048
- `is_product_of` --> [[reaction.R05506|reaction.R05506]] `KEGG` `database` - C07118 + C00010 <=> C00512 + C00024
- `is_product_of` --> [[reaction.R10866|reaction.R10866]] `KEGG` `database` - C00022 + C00010 + C02869 <=> C00024 + C00011 + C02745
- `is_product_of` --> [[reaction.ecocyc.ACECOATRANS-RXN|reaction.ecocyc.ACECOATRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ACETALD-DEHYDROG-RXN|reaction.ecocyc.ACETALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ACETATE--COA-LIGASE-RXN|reaction.ecocyc.ACETATE--COA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PYFLAVOXRE-RXN|reaction.ecocyc.PYFLAVOXRE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PYRUFLAVREDUCT-RXN|reaction.ecocyc.PYRUFLAVREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PYRUVDEH-RXN|reaction.ecocyc.PYRUVDEH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00212|reaction.R00212]] `KEGG` `database` - C00024 + C00058 <=> C00010 + C00022
- `is_substrate_of` --> [[reaction.R00230|reaction.R00230]] `KEGG` `database` - C00024 + C00009 <=> C00010 + C00227
- `is_substrate_of` --> [[reaction.R00238|reaction.R00238]] `KEGG` `database` - 2 C00024 <=> C00010 + C00332
- `is_substrate_of` --> [[reaction.R00259|reaction.R00259]] `KEGG` `database` - C00024 + C00025 <=> C00010 + C00624
- `is_substrate_of` --> [[reaction.R00371|reaction.R00371]] `KEGG` `database` - C00024 + C00037 <=> C00010 + C03508
- `is_substrate_of` --> [[reaction.R00391|reaction.R00391]] `KEGG` `database` - C00040 + C00024 <=> C00010 + C00264
- `is_substrate_of` --> [[reaction.R00586|reaction.R00586]] `KEGG` `database` - C00065 + C00024 <=> C00979 + C00010
- `is_substrate_of` --> [[reaction.R00693|reaction.R00693]] `KEGG` `database` - C00024 + C00079 <=> C00010 + C03519
- `is_substrate_of` --> [[reaction.R00742|reaction.R00742]] `KEGG` `database` - C00002 + C00024 + C00288 <=> C00008 + C00009 + C00083
- `is_substrate_of` --> [[reaction.R00829|reaction.R00829]] `KEGG` `database` - C00091 + C00024 <=> C00010 + C02232
- `is_substrate_of` --> [[reaction.R01154|reaction.R01154]] `KEGG` `database` - C00024 + C00134 <=> C00010 + C02714
- `is_substrate_of` --> [[reaction.R01323|reaction.R01323]] `KEGG` `database` - C00024 + C00158 <=> C00033 + C00566
- `is_substrate_of` --> [[reaction.R02616|reaction.R02616]] `KEGG` `database` - C00024 + C00602 <=> C00010 + C03773
- `is_substrate_of` --> [[reaction.R03778|reaction.R03778]] `KEGG` `database` - C01944 + C00024 <=> C00010 + C05265
- `is_substrate_of` --> [[reaction.R05332|reaction.R05332]] `KEGG` `database` - C00024 + C06156 <=> C00010 + C04501
- `is_substrate_of` --> [[reaction.R11479|reaction.R11479]] `KEGG` `database` - C00024 + C03557 <=> C21403 + C00010
- `is_substrate_of` --> [[reaction.ecocyc.2-ISOPROPYLMALATESYN-RXN|reaction.ecocyc.2-ISOPROPYLMALATESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2.3.1.118-RXN|reaction.ecocyc.2.3.1.118-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2.3.1.128-RXN|reaction.ecocyc.2.3.1.128-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2.3.1.157-RXN|reaction.ecocyc.2.3.1.157-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2.3.1.180-RXN|reaction.ecocyc.2.3.1.180-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN|reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ACETYL-COA-ACETYLTRANSFER-RXN|reaction.ecocyc.ACETYL-COA-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-RXN|reaction.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ACP-S-ACETYLTRANSFER-RXN|reaction.ecocyc.ACP-S-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.AKBLIG-RXN|reaction.ecocyc.AKBLIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ARYLAMINE-N-ACETYLTRANSFERASE-RXN|reaction.ecocyc.ARYLAMINE-N-ACETYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CITSYN-RXN|reaction.ecocyc.CITSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DIAMACTRANS-RXN|reaction.ecocyc.DIAMACTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DIHYDLIPACETRANS-RXN|reaction.ecocyc.DIHYDLIPACETRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GALACTOACETYLTRAN-RXN|reaction.ecocyc.GALACTOACETYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.KETOACYLCOATHIOL-RXN|reaction.ecocyc.KETOACYLCOATHIOL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MALSYN-RXN|reaction.ecocyc.MALSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MALTACETYLTRAN-RXN|reaction.ecocyc.MALTACETYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.N-ACETYLTRANSFER-RXN|reaction.ecocyc.N-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PHOSACETYLTRANS-RXN|reaction.ecocyc.PHOSACETYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PYRUVFORMLY-RXN|reaction.ecocyc.PYRUVFORMLY-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12565|reaction.ecocyc.RXN-12565]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13617|reaction.ecocyc.RXN-13617]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14274|reaction.ecocyc.RXN-14274]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14277|reaction.ecocyc.RXN-14277]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14394|reaction.ecocyc.RXN-14394]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15943|reaction.ecocyc.RXN-15943]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17778|reaction.ecocyc.RXN-17778]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17782|reaction.ecocyc.RXN-17782]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17787|reaction.ecocyc.RXN-17787]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17791|reaction.ecocyc.RXN-17791]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17795|reaction.ecocyc.RXN-17795]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17799|reaction.ecocyc.RXN-17799]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17960|reaction.ecocyc.RXN-17960]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17961|reaction.ecocyc.RXN-17961]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17962|reaction.ecocyc.RXN-17962]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18434|reaction.ecocyc.RXN-18434]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20154|reaction.ecocyc.RXN-20154]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20155|reaction.ecocyc.RXN-20155]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-3641|reaction.ecocyc.RXN-3641]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1133|reaction.ecocyc.RXN0-1133]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5055|reaction.ecocyc.RXN0-5055]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5231|reaction.ecocyc.RXN0-5231]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5418|reaction.ecocyc.RXN0-5418]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6512|reaction.ecocyc.RXN0-6512]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6948|reaction.ecocyc.RXN0-6948]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7014|reaction.ecocyc.RXN0-7014]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7075|reaction.ecocyc.RXN0-7075]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7160|reaction.ecocyc.RXN0-7160]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7165|reaction.ecocyc.RXN0-7165]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7342|reaction.ecocyc.RXN0-7342]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7345|reaction.ecocyc.RXN0-7345]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SERINE-O-ACETTRAN-RXN|reaction.ecocyc.SERINE-O-ACETTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SPERMACTRAN-RXN|reaction.ecocyc.SPERMACTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TDPFUCACTRANS-RXN|reaction.ecocyc.TDPFUCACTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.1.1.1.39-RXN|reaction.ecocyc.1.1.1.39-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN|reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.MALIC-NADP-RXN|reaction.ecocyc.MALIC-NADP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.MALONYL-COA-ACP-TRANSACYL-RXN|reaction.ecocyc.MALONYL-COA-ACP-TRANSACYL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PHOSPHOGLUCMUT-RXN|reaction.ecocyc.PHOSPHOGLUCMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-1382|reaction.ecocyc.RXN0-1382]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00024`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
