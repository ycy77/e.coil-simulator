---
entity_id: "molecule.C00026"
entity_type: "small_molecule"
name: "2-Oxoglutarate"
source_database: "KEGG"
source_id: "C00026"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Oxoglutarate"
  - "Oxoglutaric acid"
  - "2-Ketoglutaric acid"
  - "alpha-Ketoglutaric acid"
---

# 2-Oxoglutarate

`molecule.C00026`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00026`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Oxoglutarate; Oxoglutaric acid; 2-Ketoglutaric acid; alpha-Ketoglutaric acid

## Biological Role

Consumed as substrate in 54 reaction(s). Produced in 19 reaction(s).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00340` Histidine metabolism (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Annotation

KEGG compound: 2-Oxoglutarate; Oxoglutaric acid; 2-Ketoglutaric acid; alpha-Ketoglutaric acid

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00340` Histidine metabolism (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Outgoing Edges (85)

- `activates` --> [[reaction.ecocyc.DEPHOSICITDEHASE-RXN|reaction.ecocyc.DEPHOSICITDEHASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.GSDEADENYLATION-RXN|reaction.ecocyc.GSDEADENYLATION-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00114|reaction.R00114]] `KEGG` `database` - 2 C00025 + C00006 <=> C00064 + C00026 + C00005 + C00080
- `is_product_of` --> [[reaction.R00248|reaction.R00248]] `KEGG` `database` - C00025 + C00006 + C00001 <=> C00026 + C00014 + C00005 + C00080
- `is_product_of` --> [[reaction.R00267|reaction.R00267]] `KEGG` `database` - C00311 + C00006 <=> C00026 + C00011 + C00005 + C00080
- `is_product_of` --> [[reaction.R00268|reaction.R00268]] `KEGG` `database` - C05379 <=> C00026 + C00011
- `is_product_of` --> [[reaction.R00269|reaction.R00269]] `KEGG` `database` - C00940 + C00001 <=> C00026 + C00014
- `is_product_of` --> [[reaction.R08198|reaction.R08198]] `KEGG` `database` - C02630 + C00003 <=> C00026 + C00004 + C00080
- `is_product_of` --> [[reaction.R11337|reaction.R11337]] `KEGG` `database` - C01087 + C00003 <=> C00026 + C00004 + C00080
- `is_product_of` --> [[reaction.ecocyc.25-DIOXOVALERATE-DEHYDROGENASE-RXN|reaction.ecocyc.25-DIOXOVALERATE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUTAMATESYN-RXN|reaction.ecocyc.GLUTAMATESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUTDEHYD-RXN|reaction.ecocyc.GLUTDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ISOCITDEH-RXN|reaction.ecocyc.ISOCITDEH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.KETOGLUTREDUCT-RXN|reaction.ecocyc.KETOGLUTREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-13072|reaction.ecocyc.RXN-13072]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14932|reaction.ecocyc.RXN-14932]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16701|reaction.ecocyc.RXN-16701]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-20084|reaction.ecocyc.RXN-20084]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-8642|reaction.ecocyc.RXN-8642]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7319|reaction.ecocyc.RXN0-7319]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-23|reaction.ecocyc.TRANS-RXN-23]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00258|reaction.R00258]] `KEGG` `database` - C00041 + C00026 <=> C00022 + C00025
- `is_substrate_of` --> [[reaction.R00355|reaction.R00355]] `KEGG` `database` - C00049 + C00026 <=> C00036 + C00025
- `is_substrate_of` --> [[reaction.R00621|reaction.R00621]] `KEGG` `database` - C00026 + C00068 <=> C05381 + C00011
- `is_substrate_of` --> [[reaction.R00694|reaction.R00694]] `KEGG` `database` - C00079 + C00026 <=> C00166 + C00025
- `is_substrate_of` --> [[reaction.R00734|reaction.R00734]] `KEGG` `database` - C00082 + C00026 <=> C01179 + C00025
- `is_substrate_of` --> [[reaction.R01155|reaction.R01155]] `KEGG` `database` - C00134 + C00026 <=> C00555 + C00025
- `is_substrate_of` --> [[reaction.R02619|reaction.R02619]] `KEGG` `database` - C00606 + C00026 <=> C05527 + C00025
- `is_substrate_of` --> [[reaction.R04438|reaction.R04438]] `KEGG` `database` - C04346 + C00026 <=> C11907 + C00025
- `is_substrate_of` --> [[reaction.R05320|reaction.R05320]] `KEGG` `database` - C00245 + C00026 + C00007 <=> C00094 + C06735 + C00042 + C00011
- `is_substrate_of` --> [[reaction.ecocyc.2.5.1.64-RXN|reaction.ecocyc.2.5.1.64-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2.6.1.57-RXN|reaction.ecocyc.2.6.1.57-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2.6.1.7-RXN|reaction.ecocyc.2.6.1.7-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2.6.1.82-RXN|reaction.ecocyc.2.6.1.82-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2OXOGLUTARATEDEH-RXN|reaction.ecocyc.2OXOGLUTARATEDEH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2OXOGLUTDECARB-RXN|reaction.ecocyc.2OXOGLUTDECARB-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ACETYLORNTRANSAM-RXN|reaction.ecocyc.ACETYLORNTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ALANINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.ALANINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ASPAMINOTRANS-RXN|reaction.ecocyc.ASPAMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERILEU-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERILEU-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERVAL-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERVAL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CYSTEINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.CYSTEINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DIAMTRANSAM-RXN|reaction.ecocyc.DIAMTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GABATRANSAM-RXN|reaction.ecocyc.GABATRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.HISTAMINOTRANS-RXN|reaction.ecocyc.HISTAMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PSERTRANSAM-RXN|reaction.ecocyc.PSERTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PSERTRANSAMPYR-RXN|reaction.ecocyc.PSERTRANSAMPYR-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PUTTRANSAM-RXN|reaction.ecocyc.PUTTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RFFTRANS-RXN|reaction.ecocyc.RFFTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10814|reaction.ecocyc.RXN-10814]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12353|reaction.ecocyc.RXN-12353]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18737|reaction.ecocyc.RXN-18737]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18738|reaction.ecocyc.RXN-18738]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18739|reaction.ecocyc.RXN-18739]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21233|reaction.ecocyc.RXN-21233]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21235|reaction.ecocyc.RXN-21235]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21236|reaction.ecocyc.RXN-21236]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21858|reaction.ecocyc.RXN-21858]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1144|reaction.ecocyc.RXN0-1144]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1863|reaction.ecocyc.RXN0-1863]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-299|reaction.ecocyc.RXN0-299]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7090|reaction.ecocyc.RXN0-7090]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7275|reaction.ecocyc.RXN0-7275]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7280|reaction.ecocyc.RXN0-7280]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7316|reaction.ecocyc.RXN0-7316]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7317|reaction.ecocyc.RXN0-7317]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7484|reaction.ecocyc.RXN0-7484]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-984|reaction.ecocyc.RXN0-984]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-986|reaction.ecocyc.RXN0-986]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SUCCINYLDIAMINOPIMTRANS-RXN|reaction.ecocyc.SUCCINYLDIAMINOPIMTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SUCCORNTRANSAM-RXN|reaction.ecocyc.SUCCORNTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-23|reaction.ecocyc.TRANS-RXN-23]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.VAGL-RXN|reaction.ecocyc.VAGL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.1.1.1.39-RXN|reaction.ecocyc.1.1.1.39-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.2.7.3.9-RXN|reaction.ecocyc.2.7.3.9-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.CITSYN-RXN|reaction.ecocyc.CITSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GSADENYLATION-RXN|reaction.ecocyc.GSADENYLATION-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ISOCIT-CLEAV-RXN|reaction.ecocyc.ISOCIT-CLEAV-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.KETOGLUTREDUCT-RXN|reaction.ecocyc.KETOGLUTREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PEPSYNTH-RXN|reaction.ecocyc.PEPSYNTH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PHOSICITDEHASE-RXN|reaction.ecocyc.PHOSICITDEHASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-16701|reaction.ecocyc.RXN-16701]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.SUCCINYLDIAMINOPIMTRANS-RXN|reaction.ecocyc.SUCCINYLDIAMINOPIMTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P0AEX3|protein.P0AEX3]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00026`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
