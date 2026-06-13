---
entity_id: "molecule.C00074"
entity_type: "small_molecule"
name: "Phosphoenolpyruvate"
source_database: "KEGG"
source_id: "C00074"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phosphoenolpyruvate"
  - "Phosphoenolpyruvic acid"
  - "PEP"
---

# Phosphoenolpyruvate

`molecule.C00074`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00074`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phosphoenolpyruvate; Phosphoenolpyruvic acid; PEP

## Biological Role

Consumed as substrate in 15 reaction(s). Produced in 15 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: Phosphoenolpyruvate; Phosphoenolpyruvic acid; PEP

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (48)

- `activates` --> [[reaction.ecocyc.2.5.1.19-RXN|reaction.ecocyc.2.5.1.19-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.DEPHOSICITDEHASE-RXN|reaction.ecocyc.DEPHOSICITDEHASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.F16BDEPHOS-RXN|reaction.ecocyc.F16BDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.PHOSACETYLTRANS-RXN|reaction.ecocyc.PHOSACETYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00199|reaction.R00199]] `KEGG` `database` - C00002 + C00022 + C00001 <=> C00020 + C00074 + C00009
- `is_product_of` --> [[reaction.R00200|reaction.R00200]] `KEGG` `database` - C00002 + C00022 <=> C00008 + C00074
- `is_product_of` --> [[reaction.R00341|reaction.R00341]] `KEGG` `database` - C00002 + C00036 <=> C00008 + C00074 + C00011
- `is_product_of` --> [[reaction.R00345|reaction.R00345]] `KEGG` `database` - C00009 + C00036 <=> C00001 + C00074 + C00011
- `is_product_of` --> [[reaction.R00430|reaction.R00430]] `KEGG` `database` - C00044 + C00022 <=> C00035 + C00074
- `is_product_of` --> [[reaction.R00572|reaction.R00572]] `KEGG` `database` - C00063 + C00022 <=> C00112 + C00074
- `is_product_of` --> [[reaction.R00658|reaction.R00658]] `KEGG` `database` - C00631 <=> C00074 + C00001
- `is_product_of` --> [[reaction.R00659|reaction.R00659]] `KEGG` `database` - C00075 + C00022 <=> C00015 + C00074
- `is_product_of` --> [[reaction.R00724|reaction.R00724]] `KEGG` `database` - C00081 + C00022 <=> C00104 + C00074
- `is_product_of` --> [[reaction.R01138|reaction.R01138]] `KEGG` `database` - C00131 + C00022 <=> C00206 + C00074
- `is_product_of` --> [[reaction.ecocyc.2PGADEHYDRAT-RXN|reaction.ecocyc.2PGADEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PEPCARBOX-RXN|reaction.ecocyc.PEPCARBOX-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PEPCARBOXYKIN-RXN|reaction.ecocyc.PEPCARBOXYKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PEPDEPHOS-RXN|reaction.ecocyc.PEPDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PEPSYNTH-RXN|reaction.ecocyc.PEPSYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00660|reaction.R00660]] `KEGG` `database` - C00074 + C00043 <=> C04631 + C00009
- `is_substrate_of` --> [[reaction.R01012|reaction.R01012]] `KEGG` `database` - C00074 + C00184 <=> C00022 + C00111
- `is_substrate_of` --> [[reaction.ecocyc.2.5.1.19-RXN|reaction.ecocyc.2.5.1.19-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2.7.1.121-RXN|reaction.ecocyc.2.7.1.121-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2.7.3.9-RXN|reaction.ecocyc.2.7.3.9-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DAHPSYN-RXN|reaction.ecocyc.DAHPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.KDO-8PSYNTH-RXN|reaction.ecocyc.KDO-8PSYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PHOSPHOENOLPYRUVATE-PHOSPHATASE-RXN|reaction.ecocyc.PHOSPHOENOLPYRUVATE-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17354|reaction.ecocyc.RXN-17354]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21080|reaction.ecocyc.RXN-21080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22214|reaction.ecocyc.RXN-22214]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6717|reaction.ecocyc.RXN0-6717]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7047|reaction.ecocyc.RXN0-7047]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7166|reaction.ecocyc.RXN0-7166]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN|reaction.ecocyc.UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.6PFRUCTPHOS-RXN|reaction.ecocyc.6PFRUCTPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.F16BDEPHOS-RXN|reaction.ecocyc.F16BDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUCOKIN-RXN|reaction.ecocyc.GLUCOKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GSADENYLATION-RXN|reaction.ecocyc.GSADENYLATION-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ISOCIT-CLEAV-RXN|reaction.ecocyc.ISOCIT-CLEAV-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ISOCITDEH-RXN|reaction.ecocyc.ISOCITDEH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.METHGLYSYN-RXN|reaction.ecocyc.METHGLYSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PEPCARBOXYKIN-RXN|reaction.ecocyc.PEPCARBOXYKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PEPSYNTH-RXN|reaction.ecocyc.PEPSYNTH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PGLUCISOM-RXN|reaction.ecocyc.PGLUCISOM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PHOSACETYLTRANS-RXN|reaction.ecocyc.PHOSACETYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PHOSICITDEHASE-RXN|reaction.ecocyc.PHOSICITDEHASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5260|reaction.ecocyc.RXN0-5260]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.THI-P-SYN-RXN|reaction.ecocyc.THI-P-SYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00074`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
