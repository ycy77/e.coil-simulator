---
entity_id: "molecule.C00051"
entity_type: "small_molecule"
name: "Glutathione"
source_database: "KEGG"
source_id: "C00051"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Glutathione"
  - "5-L-Glutamyl-L-cysteinylglycine"
  - "N-(N-gamma-L-Glutamyl-L-cysteinyl)glycine"
  - "gamma-L-Glutamyl-L-cysteinyl-glycine"
  - "GSH"
  - "Reduced glutathione"
---

# Glutathione

`molecule.C00051`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00051`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Glutathione; 5-L-Glutamyl-L-cysteinylglycine; N-(N-gamma-L-Glutamyl-L-cysteinyl)glycine; gamma-L-Glutamyl-L-cysteinyl-glycine; GSH; Reduced glutathione Thiols play a major role in the detoxification of stress-inducing factors such as reactive oxygen species, free radicals, peroxides, lipid peroxides, and heavy metals. In mammals, the major thiol is the tripeptide GLUTATHIONE (γ-Glu-Cys-Gly, known as GSH). Toxins are conjugated to GSH in the liver by a dedicated enzyme, resulting in a S-Substituted-L-Cysteines "cysteine-toxin conjugate". The conjugate is acetylated in the kidney to form Mercapturates, and is then excreted (see PWY-4061). In addition to oxidative stress management, low molecular weight thiols have been found to be involved in critical cellular processes including DNA synthesis and formaldehyde reduction . Gluathione is the major thiol not only in eukaryotic organisms but also in Gram negative bacteria and in the majority of Gram positive bacteria. Pathogenic bacteria live in a particularly hostile environment, in which the host deliberately generates toxins, including reactive oxygen species, to destroy the invading organism, thus thiols are particularly important for the survival of these organisms. Despite the ubiquity of GSH, it is not universal. In many organisms, including some eukaryotes, other thiols have taken its role...

## Biological Role

Consumed as substrate in 34 reaction(s). Produced in 12 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Glutathione; 5-L-Glutamyl-L-cysteinylglycine; N-(N-gamma-L-Glutamyl-L-cysteinyl)glycine; gamma-L-Glutamyl-L-cysteinyl-glycine; GSH; Reduced glutathione

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (52)

- `activates` --> [[reaction.ecocyc.1.1.1.283-RXN|reaction.ecocyc.1.1.1.283-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.ACETYLORNDEACET-RXN|reaction.ecocyc.ACETYLORNDEACET-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.LYXK-RXN|reaction.ecocyc.LYXK-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00497|reaction.R00497]] `KEGG` `database` - C00002 + C00669 + C00037 <=> C00008 + C00009 + C00051
- `is_product_of` --> [[reaction.R00527|reaction.R00527]] `KEGG` `database` - C01031 + C00001 <=> C00058 + C00051
- `is_product_of` --> [[reaction.R01736|reaction.R01736]] `KEGG` `database` - C03451 + C00001 <=> C00051 + C00256
- `is_product_of` --> [[reaction.ecocyc.GLUTATHIONE-SYN-RXN|reaction.ecocyc.GLUTATHIONE-SYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLYOXI-RXN|reaction.ecocyc.GLYOXI-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLYOXII-RXN|reaction.ecocyc.GLYOXII-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GSPAMID-RXN|reaction.ecocyc.GSPAMID-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-24129|reaction.ecocyc.RXN-24129]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-2961|reaction.ecocyc.RXN-2961]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-11|reaction.ecocyc.RXN0-11]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-21|reaction.ecocyc.RXN0-21]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.S-FORMYLGLUTATHIONE-HYDROLASE-RXN|reaction.ecocyc.S-FORMYLGLUTATHIONE-HYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00094|reaction.R00094]] `KEGG` `database` - 2 C00051 + C00003 <=> C00127 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00115|reaction.R00115]] `KEGG` `database` - 2 C00051 + C00006 <=> C00127 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00274|reaction.R00274]] `KEGG` `database` - C00027 + 2 C00051 <=> C00127 + 2 C00001
- `is_substrate_of` --> [[reaction.R00494|reaction.R00494]] `KEGG` `database` - C00051 + C00001 <=> C01419 + C00025
- `is_substrate_of` --> [[reaction.ecocyc.1.8.4.4-RXN|reaction.ecocyc.1.8.4.4-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTATHIONE-PEROXIDASE-RXN|reaction.ecocyc.GLUTATHIONE-PEROXIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTATHIONE-REDUCT-NADPH-RXN|reaction.ecocyc.GLUTATHIONE-REDUCT-NADPH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GSPSYN-RXN|reaction.ecocyc.GSPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GST-RXN|reaction.ecocyc.GST-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PRODISULFREDUCT-A-RXN|reaction.ecocyc.PRODISULFREDUCT-A-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PRODISULFREDUCT-RXN|reaction.ecocyc.PRODISULFREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12618|reaction.ecocyc.RXN-12618]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12864|reaction.ecocyc.RXN-12864]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14497|reaction.ecocyc.RXN-14497]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15348|reaction.ecocyc.RXN-15348]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17886|reaction.ecocyc.RXN-17886]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17887|reaction.ecocyc.RXN-17887]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18092|reaction.ecocyc.RXN-18092]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19024|reaction.ecocyc.RXN-19024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19033|reaction.ecocyc.RXN-19033]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19573|reaction.ecocyc.RXN-19573]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19629|reaction.ecocyc.RXN-19629]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19922|reaction.ecocyc.RXN-19922]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21019|reaction.ecocyc.RXN-21019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21025|reaction.ecocyc.RXN-21025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22643|reaction.ecocyc.RXN-22643]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-25117|reaction.ecocyc.RXN-25117]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-982|reaction.ecocyc.RXN-982]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-11|reaction.ecocyc.RXN0-11]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-21|reaction.ecocyc.RXN0-21]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6256|reaction.ecocyc.RXN0-6256]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6549|reaction.ecocyc.RXN0-6549]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7010|reaction.ecocyc.RXN0-7010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.THIOSULFATE--THIOL-SULFURTRANSFERASE-RXN|reaction.ecocyc.THIOSULFATE--THIOL-SULFURTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.AKBLIG-RXN|reaction.ecocyc.AKBLIG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN|reaction.ecocyc.ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUTCYSLIG-RXN|reaction.ecocyc.GLUTCYSLIG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.ABC-49-CPLX|complex.ecocyc.ABC-49-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[complex.ecocyc.ABC-6-CPLX|complex.ecocyc.ABC-6-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00051`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
