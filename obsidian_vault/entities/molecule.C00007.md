---
entity_id: "molecule.C00007"
entity_type: "small_molecule"
name: "Oxygen"
source_database: "KEGG"
source_id: "C00007"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Oxygen"
  - "O2"
---

# Oxygen

`molecule.C00007`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00007`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Oxygen; O2 EcoCyc common name: dioxygen.

## Biological Role

Consumed as substrate in 89 reaction(s). Produced in 8 reaction(s).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

KEGG compound: Oxygen; O2

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (103)

- `is_product_of` --> [[reaction.R00009|reaction.R00009]] `KEGG` `database` - 2 C00027 <=> C00007 + 2 C00001
- `is_product_of` --> [[reaction.R00275|reaction.R00275]] `KEGG` `database` - 2 C00704 + 2 C00080 <=> C00027 + C00007
- `is_product_of` --> [[reaction.ecocyc.CATAL-RXN|reaction.ecocyc.CATAL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12541|reaction.ecocyc.RXN-12541]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-25639|reaction.ecocyc.RXN-25639]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-25748|reaction.ecocyc.RXN-25748]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SUPEROX-DISMUT-RXN|reaction.ecocyc.SUPEROX-DISMUT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-474|reaction.ecocyc.TRANS-RXN0-474]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00078|reaction.R00078]] `KEGG` `database` - C00007 + 4 C14818 + 4 C00080 <=> 4 C14819 + 2 C00001
- `is_substrate_of` --> [[reaction.R00277|reaction.R00277]] `KEGG` `database` - C00647 + C00001 + C00007 <=> C00018 + C00014 + C00027
- `is_substrate_of` --> [[reaction.R00278|reaction.R00278]] `KEGG` `database` - C00627 + C00007 <=> C00027 + C00018
- `is_substrate_of` --> [[reaction.R00357|reaction.R00357]] `KEGG` `database` - C00049 + C00001 + C00007 <=> C00036 + C00014 + C00027
- `is_substrate_of` --> [[reaction.R00360|reaction.R00360]] `KEGG` `database` - C00149 + C00007 <=> C00036 + C00027
- `is_substrate_of` --> [[reaction.R00481|reaction.R00481]] `KEGG` `database` - C00049 + C00007 <=> C05840 + C00027
- `is_substrate_of` --> [[reaction.R00698|reaction.R00698]] `KEGG` `database` - C00079 + C00007 <=> C02505 + C00011
- `is_substrate_of` --> [[reaction.R02382|reaction.R02382]] `KEGG` `database` - C00483 + C00001 + C00007 <=> C03765 + C00014 + C00027
- `is_substrate_of` --> [[reaction.R02613|reaction.R02613]] `KEGG` `database` - C05332 + C00007 + C00001 <=> C00601 + C00014 + C00027
- `is_substrate_of` --> [[reaction.R03139|reaction.R03139]] `KEGG` `database` - C00986 + C00007 + C00001 <=> C05665 + C00014 + C00027
- `is_substrate_of` --> [[reaction.R05320|reaction.R05320]] `KEGG` `database` - C00245 + C00026 + C00007 <=> C00094 + C06735 + C00042 + C00011
- `is_substrate_of` --> [[reaction.R05724|reaction.R05724]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00004 + C00080 <=> 2 C00244 + C00003
- `is_substrate_of` --> [[reaction.R05725|reaction.R05725]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00005 + C00080 <=> 2 C00244 + C00006
- `is_substrate_of` --> [[reaction.R11335|reaction.R11335]] `KEGG` `database` - 2 C00390 + C00007 + 8 C00080 <=> 2 C00399 + 2 C00001 + 8 C00080
- `is_substrate_of` --> [[reaction.R11911|reaction.R11911]] `KEGG` `database` - C00318 + C00005 + C00080 + C00007 <=> C21761 + C00565 + C00006 + C00001
- `is_substrate_of` --> [[reaction.R12067|reaction.R12067]] `KEGG` `database` - C19859 + C00030 + C00007 <=> C21860 + C00028 + C00001
- `is_substrate_of` --> [[reaction.R13011|reaction.R13011]] `KEGG` `database` - C00322 + C00007 <=> C01087 + C00011
- `is_substrate_of` --> [[reaction.ecocyc.1.13.11.16-RXN|reaction.ecocyc.1.13.11.16-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2-OCTAPRENYL-6-METHOXYPHENOL-HYDROX-RXN|reaction.ecocyc.2-OCTAPRENYL-6-METHOXYPHENOL-HYDROX-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2-OCTAPRENYLPHENOL-HYDROX-RXN|reaction.ecocyc.2-OCTAPRENYLPHENOL-HYDROX-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.AMACETOXID-RXN|reaction.ecocyc.AMACETOXID-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.AMINEOXID-RXN|reaction.ecocyc.AMINEOXID-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.HCAMULTI-RXN|reaction.ecocyc.HCAMULTI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.L-ASPARTATE-OXID-RXN|reaction.ecocyc.L-ASPARTATE-OXID-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MHPHYDROXY-RXN|reaction.ecocyc.MHPHYDROXY-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.OCTAPRENYL-METHYL-METHOXY-BENZOQ-OH-RXN|reaction.ecocyc.OCTAPRENYL-METHYL-METHOXY-BENZOQ-OH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PMPOXI-RXN|reaction.ecocyc.PMPOXI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PNPOXI-RXN|reaction.ecocyc.PNPOXI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PROTOPORGENOXI-RXN|reaction.ecocyc.PROTOPORGENOXI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.QUERCETIN-23-DIOXYGENASE-RXN|reaction.ecocyc.QUERCETIN-23-DIOXYGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.R621-RXN|reaction.ecocyc.R621-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10040|reaction.ecocyc.RXN-10040]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10745|reaction.ecocyc.RXN-10745]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10745-1|reaction.ecocyc.RXN-10745-1]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10817|reaction.ecocyc.RXN-10817]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12072|reaction.ecocyc.RXN-12072]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12073|reaction.ecocyc.RXN-12073]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12353|reaction.ecocyc.RXN-12353]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12869|reaction.ecocyc.RXN-12869]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12886|reaction.ecocyc.RXN-12886]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13418|reaction.ecocyc.RXN-13418]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15292|reaction.ecocyc.RXN-15292]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15294|reaction.ecocyc.RXN-15294]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15341|reaction.ecocyc.RXN-15341]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16312|reaction.ecocyc.RXN-16312]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16420|reaction.ecocyc.RXN-16420]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16454|reaction.ecocyc.RXN-16454]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17944|reaction.ecocyc.RXN-17944]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18258|reaction.ecocyc.RXN-18258]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18376|reaction.ecocyc.RXN-18376]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18737|reaction.ecocyc.RXN-18737]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18738|reaction.ecocyc.RXN-18738]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18739|reaction.ecocyc.RXN-18739]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20148|reaction.ecocyc.RXN-20148]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20149|reaction.ecocyc.RXN-20149]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21233|reaction.ecocyc.RXN-21233]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21235|reaction.ecocyc.RXN-21235]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21236|reaction.ecocyc.RXN-21236]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22443|reaction.ecocyc.RXN-22443]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-5921|reaction.ecocyc.RXN-5921]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8460|reaction.ecocyc.RXN-8460]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9597|reaction.ecocyc.RXN-9597]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1461|reaction.ecocyc.RXN0-1461]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1483|reaction.ecocyc.RXN0-1483]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2042|reaction.ecocyc.RXN0-2042]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-280|reaction.ecocyc.RXN0-280]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2943|reaction.ecocyc.RXN0-2943]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2945|reaction.ecocyc.RXN0-2945]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-299|reaction.ecocyc.RXN0-299]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-301|reaction.ecocyc.RXN0-301]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-3381|reaction.ecocyc.RXN0-3381]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-3921|reaction.ecocyc.RXN0-3921]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5265|reaction.ecocyc.RXN0-5265]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5266|reaction.ecocyc.RXN0-5266]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5268|reaction.ecocyc.RXN0-5268]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6444|reaction.ecocyc.RXN0-6444]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6973|reaction.ecocyc.RXN0-6973]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7000|reaction.ecocyc.RXN0-7000]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7090|reaction.ecocyc.RXN0-7090]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7275|reaction.ecocyc.RXN0-7275]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7280|reaction.ecocyc.RXN0-7280]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7316|reaction.ecocyc.RXN0-7316]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7349|reaction.ecocyc.RXN0-7349]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7363|reaction.ecocyc.RXN0-7363]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7427|reaction.ecocyc.RXN0-7427]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7484|reaction.ecocyc.RXN0-7484]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-984|reaction.ecocyc.RXN0-984]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-986|reaction.ecocyc.RXN0-986]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-474|reaction.ecocyc.TRANS-RXN0-474]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.FORMATEDEHYDROG-RXN|reaction.ecocyc.FORMATEDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.HYDROXYLAMINE-REDUCTASE-RXN|reaction.ecocyc.HYDROXYLAMINE-REDUCTASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PYRUVFORMLY-RXN|reaction.ecocyc.PYRUVFORMLY-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.QUINOLINATE-SYNTHA-RXN|reaction.ecocyc.QUINOLINATE-SYNTHA-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-3281|reaction.ecocyc.RXN0-3281]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-7399|reaction.ecocyc.RXN0-7399]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00007`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
