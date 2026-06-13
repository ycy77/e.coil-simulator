---
entity_id: "molecule.C00010"
entity_type: "small_molecule"
name: "CoA"
source_database: "KEGG"
source_id: "C00010"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "CoA"
  - "Coenzyme A"
  - "CoA-SH"
---

# CoA

`molecule.C00010`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00010`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: CoA; Coenzyme A; CoA-SH EcoCyc common name: coenzyme A. Coenzyme A (CoA) is a ubiquitous compound found in archaea, bacteria, plants, and animals. It is a common acyl carrier in prokaryotic and eukaryotic cells, and is required for a multitude of reactions for both biosynthetic and degradative pathways, including the oxidation of fatty acids, carbohydrates, and amino acids . While the name "coenzyme A" is well established, the correct name for the function of the compound in enzymatic reactions is "cosubstrate".

## Biological Role

Consumed as substrate in 35 reaction(s). Produced in 104 reaction(s).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Annotation

KEGG compound: CoA; Coenzyme A; CoA-SH

## Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Outgoing Edges (155)

- `is_product_of` --> [[reaction.R00130|reaction.R00130]] `KEGG` `database` - C00002 + C00882 <=> C00008 + C00010
- `is_product_of` --> [[reaction.R00212|reaction.R00212]] `KEGG` `database` - C00024 + C00058 <=> C00010 + C00022
- `is_product_of` --> [[reaction.R00230|reaction.R00230]] `KEGG` `database` - C00024 + C00009 <=> C00010 + C00227
- `is_product_of` --> [[reaction.R00238|reaction.R00238]] `KEGG` `database` - 2 C00024 <=> C00010 + C00332
- `is_product_of` --> [[reaction.R00259|reaction.R00259]] `KEGG` `database` - C00024 + C00025 <=> C00010 + C00624
- `is_product_of` --> [[reaction.R00371|reaction.R00371]] `KEGG` `database` - C00024 + C00037 <=> C00010 + C03508
- `is_product_of` --> [[reaction.R00383|reaction.R00383]] `KEGG` `database` - C00040 + C00001 <=> C00010 + C00060
- `is_product_of` --> [[reaction.R00391|reaction.R00391]] `KEGG` `database` - C00040 + C00024 <=> C00010 + C00264
- `is_product_of` --> [[reaction.R00586|reaction.R00586]] `KEGG` `database` - C00065 + C00024 <=> C00979 + C00010
- `is_product_of` --> [[reaction.R00693|reaction.R00693]] `KEGG` `database` - C00024 + C00079 <=> C00010 + C03519
- `is_product_of` --> [[reaction.R00829|reaction.R00829]] `KEGG` `database` - C00091 + C00024 <=> C00010 + C02232
- `is_product_of` --> [[reaction.R00832|reaction.R00832]] `KEGG` `database` - C00091 + C00062 <=> C00010 + C03296
- `is_product_of` --> [[reaction.R01154|reaction.R01154]] `KEGG` `database` - C00024 + C00134 <=> C00010 + C02714
- `is_product_of` --> [[reaction.R02616|reaction.R02616]] `KEGG` `database` - C00024 + C00602 <=> C00010 + C03773
- `is_product_of` --> [[reaction.R02617|reaction.R02617]] `KEGG` `database` - C00605 + C00093 <=> C00010 + C00681
- `is_product_of` --> [[reaction.R03778|reaction.R03778]] `KEGG` `database` - C01944 + C00024 <=> C00010 + C05265
- `is_product_of` --> [[reaction.R04150|reaction.R04150]] `KEGG` `database` - C03160 <=> C03657 + C00010
- `is_product_of` --> [[reaction.R05332|reaction.R05332]] `KEGG` `database` - C00024 + C06156 <=> C00010 + C04501
- `is_product_of` --> [[reaction.R08183|reaction.R08183]] `KEGG` `database` - C02249 + C00001 <=> C00010 + C00219
- `is_product_of` --> [[reaction.R11479|reaction.R11479]] `KEGG` `database` - C00024 + C03557 <=> C21403 + C00010
- `is_product_of` --> [[reaction.ecocyc.2-ISOPROPYLMALATESYN-RXN|reaction.ecocyc.2-ISOPROPYLMALATESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.2-METHYLCITRATE-SYNTHASE-RXN|reaction.ecocyc.2-METHYLCITRATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.2.3.1.118-RXN|reaction.ecocyc.2.3.1.118-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.2.3.1.128-RXN|reaction.ecocyc.2.3.1.128-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.2.3.1.157-RXN|reaction.ecocyc.2.3.1.157-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.2.3.1.180-RXN|reaction.ecocyc.2.3.1.180-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.7KAPSYN-RXN|reaction.ecocyc.7KAPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ACETYL-COA-ACETYLTRANSFER-RXN|reaction.ecocyc.ACETYL-COA-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ACP-S-ACETYLTRANSFER-RXN|reaction.ecocyc.ACP-S-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ACYL-COA-HYDROLASE-RXN|reaction.ecocyc.ACYL-COA-HYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.AKBLIG-RXN|reaction.ecocyc.AKBLIG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ARGININE-N-SUCCINYLTRANSFERASE-RXN|reaction.ecocyc.ARGININE-N-SUCCINYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ARYLAMINE-N-ACETYLTRANSFERASE-RXN|reaction.ecocyc.ARYLAMINE-N-ACETYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.CITSYN-RXN|reaction.ecocyc.CITSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DEPHOSPHOCOAKIN-RXN|reaction.ecocyc.DEPHOSPHOCOAKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DIAMACTRANS-RXN|reaction.ecocyc.DIAMACTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DIHYDLIPACETRANS-RXN|reaction.ecocyc.DIHYDLIPACETRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GALACTOACETYLTRAN-RXN|reaction.ecocyc.GALACTOACETYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.HOMSUCTRAN-RXN|reaction.ecocyc.HOMSUCTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.HYDGLUTSYN-RXN|reaction.ecocyc.HYDGLUTSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.KETOACYLCOATHIOL-RXN|reaction.ecocyc.KETOACYLCOATHIOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.KETOBUTFORMLY-RXN|reaction.ecocyc.KETOBUTFORMLY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MALONYL-COA-ACP-TRANSACYL-RXN|reaction.ecocyc.MALONYL-COA-ACP-TRANSACYL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MALSYN-RXN|reaction.ecocyc.MALSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MALTACETYLTRAN-RXN|reaction.ecocyc.MALTACETYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.N-ACETYLTRANSFER-RXN|reaction.ecocyc.N-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PALMITOYL-COA-HYDROLASE-RXN|reaction.ecocyc.PALMITOYL-COA-HYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PHOSACETYLTRANS-RXN|reaction.ecocyc.PHOSACETYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PTAALT-RXN|reaction.ecocyc.PTAALT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PYRUVFORMLY-RXN|reaction.ecocyc.PYRUVFORMLY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12565|reaction.ecocyc.RXN-12565]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-13617|reaction.ecocyc.RXN-13617]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-1381|reaction.ecocyc.RXN-1381]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14251|reaction.ecocyc.RXN-14251]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14255|reaction.ecocyc.RXN-14255]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14274|reaction.ecocyc.RXN-14274]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14277|reaction.ecocyc.RXN-14277]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14394|reaction.ecocyc.RXN-14394]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15943|reaction.ecocyc.RXN-15943]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-1623|reaction.ecocyc.RXN-1623]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17008|reaction.ecocyc.RXN-17008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17009|reaction.ecocyc.RXN-17009]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17010|reaction.ecocyc.RXN-17010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17011|reaction.ecocyc.RXN-17011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17019|reaction.ecocyc.RXN-17019]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17021|reaction.ecocyc.RXN-17021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17023|reaction.ecocyc.RXN-17023]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17778|reaction.ecocyc.RXN-17778]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17782|reaction.ecocyc.RXN-17782]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17787|reaction.ecocyc.RXN-17787]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17791|reaction.ecocyc.RXN-17791]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17795|reaction.ecocyc.RXN-17795]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17799|reaction.ecocyc.RXN-17799]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17960|reaction.ecocyc.RXN-17960]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17961|reaction.ecocyc.RXN-17961]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17962|reaction.ecocyc.RXN-17962]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18434|reaction.ecocyc.RXN-18434]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-20154|reaction.ecocyc.RXN-20154]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-25385|reaction.ecocyc.RXN-25385]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-3641|reaction.ecocyc.RXN-3641]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-9311|reaction.ecocyc.RXN-9311]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-9628|reaction.ecocyc.RXN-9628]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1133|reaction.ecocyc.RXN0-1133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1147|reaction.ecocyc.RXN0-1147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5065|reaction.ecocyc.RXN0-5065]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5231|reaction.ecocyc.RXN0-5231]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5390|reaction.ecocyc.RXN0-5390]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5418|reaction.ecocyc.RXN0-5418]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6512|reaction.ecocyc.RXN0-6512]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6948|reaction.ecocyc.RXN0-6948]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7014|reaction.ecocyc.RXN0-7014]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7046|reaction.ecocyc.RXN0-7046]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7103|reaction.ecocyc.RXN0-7103]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7104|reaction.ecocyc.RXN0-7104]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7160|reaction.ecocyc.RXN0-7160]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7165|reaction.ecocyc.RXN0-7165]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7342|reaction.ecocyc.RXN0-7342]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7345|reaction.ecocyc.RXN0-7345]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN1-42|reaction.ecocyc.RXN1-42]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SERINE-O-ACETTRAN-RXN|reaction.ecocyc.SERINE-O-ACETTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SPERMACTRAN-RXN|reaction.ecocyc.SPERMACTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TDPFUCACTRANS-RXN|reaction.ecocyc.TDPFUCACTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TETHYDPICSUCC-RXN|reaction.ecocyc.TETHYDPICSUCC-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.THIOESTER-RXN|reaction.ecocyc.THIOESTER-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00228|reaction.R00228]] `KEGG` `database` - C00084 + C00010 + C00003 <=> C00024 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00235|reaction.R00235]] `KEGG` `database` - C00002 + C00033 + C00010 <=> C00020 + C00013 + C00024
- `is_substrate_of` --> [[reaction.R00236|reaction.R00236]] `KEGG` `database` - C05993 + C00010 <=> C00020 + C00024
- `is_substrate_of` --> [[reaction.R00351|reaction.R00351]] `KEGG` `database` - C00158 + C00010 <=> C00024 + C00001 + C00036
- `is_substrate_of` --> [[reaction.R00390|reaction.R00390]] `KEGG` `database` - C00002 + C00638 + C00010 <=> C00020 + C00013 + C02843
- `is_substrate_of` --> [[reaction.R00405|reaction.R00405]] `KEGG` `database` - C00002 + C00042 + C00010 <=> C00008 + C00009 + C00091
- `is_substrate_of` --> [[reaction.R00472|reaction.R00472]] `KEGG` `database` - C00149 + C00010 <=> C00024 + C00001 + C00048
- `is_substrate_of` --> [[reaction.R02404|reaction.R02404]] `KEGG` `database` - C00002 + C00490 + C00010 <=> C00008 + C00009 + C00531
- `is_substrate_of` --> [[reaction.R05506|reaction.R05506]] `KEGG` `database` - C07118 + C00010 <=> C00512 + C00024
- `is_substrate_of` --> [[reaction.R06987|reaction.R06987]] `KEGG` `database` - C00109 + C00010 <=> C00100 + C00058
- `is_substrate_of` --> [[reaction.R10866|reaction.R10866]] `KEGG` `database` - C00022 + C00010 + C02869 <=> C00024 + C00011 + C02745
- `is_substrate_of` --> [[reaction.ecocyc.2OXOGLUTARATEDEH-RXN|reaction.ecocyc.2OXOGLUTARATEDEH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ACETALD-DEHYDROG-RXN|reaction.ecocyc.ACETALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ACETATE--COA-LIGASE-RXN|reaction.ecocyc.ACETATE--COA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ACYLCOASYN-RXN|reaction.ecocyc.ACYLCOASYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ENTDB-RXN|reaction.ecocyc.ENTDB-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.HOLO-ACP-SYNTH-RXN|reaction.ecocyc.HOLO-ACP-SYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.LCARNCOALIG-RXN|reaction.ecocyc.LCARNCOALIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.O-SUCCINYLBENZOATE-COA-LIG-RXN|reaction.ecocyc.O-SUCCINYLBENZOATE-COA-LIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PROPIONATE--COA-LIGASE-RXN|reaction.ecocyc.PROPIONATE--COA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PYFLAVOXRE-RXN|reaction.ecocyc.PYFLAVOXRE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PYRUFLAVREDUCT-RXN|reaction.ecocyc.PYRUFLAVREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PYRUVDEH-RXN|reaction.ecocyc.PYRUVDEH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10819|reaction.ecocyc.RXN-10819]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15889|reaction.ecocyc.RXN-15889]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16393|reaction.ecocyc.RXN-16393]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19959|reaction.ecocyc.RXN-19959]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19960|reaction.ecocyc.RXN-19960]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9623|reaction.ecocyc.RXN-9623]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9644|reaction.ecocyc.RXN-9644]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7238|reaction.ecocyc.RXN0-7238]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7239|reaction.ecocyc.RXN0-7239]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7248|reaction.ecocyc.RXN0-7248]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SUCCCOASYN-RXN|reaction.ecocyc.SUCCCOASYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-623|reaction.ecocyc.TRANS-RXN0-623]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.1.1.1.39-RXN|reaction.ecocyc.1.1.1.39-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN|reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN|reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ACP-S-ACETYLTRANSFER-RXN|reaction.ecocyc.ACP-S-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ACYL-COA-HYDROLASE-RXN|reaction.ecocyc.ACYL-COA-HYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.AKBLIG-RXN|reaction.ecocyc.AKBLIG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GALACTOACETYLTRAN-RXN|reaction.ecocyc.GALACTOACETYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GSADENYLATION-RXN|reaction.ecocyc.GSADENYLATION-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.MALONYL-COA-ACP-TRANSACYL-RXN|reaction.ecocyc.MALONYL-COA-ACP-TRANSACYL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.MALTACETYLTRAN-RXN|reaction.ecocyc.MALTACETYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.OXALYL-COA-DECARBOXYLASE-RXN|reaction.ecocyc.OXALYL-COA-DECARBOXYLASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PANTEPADENYLYLTRAN-RXN|reaction.ecocyc.PANTEPADENYLYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PANTOTHENATE-KIN-RXN|reaction.ecocyc.PANTOTHENATE-KIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PHOSPHOGLUCMUT-RXN|reaction.ecocyc.PHOSPHOGLUCMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-1381|reaction.ecocyc.RXN-1381]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-1382|reaction.ecocyc.RXN0-1382]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00010`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
