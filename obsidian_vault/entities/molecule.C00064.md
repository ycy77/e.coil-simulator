---
entity_id: "molecule.C00064"
entity_type: "small_molecule"
name: "L-Glutamine"
source_database: "KEGG"
source_id: "C00064"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Glutamine"
  - "L-2-Aminoglutaramic acid"
---

# L-Glutamine

`molecule.C00064`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00064`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Glutamine; L-2-Aminoglutaramic acid

## Biological Role

Consumed as substrate in 24 reaction(s). Produced in 9 reaction(s).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: L-Glutamine; L-2-Aminoglutaramic acid

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (39)

- `activates` --> [[reaction.ecocyc.GSADENYLATION-RXN|reaction.ecocyc.GSADENYLATION-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.URIDYLREM-RXN|reaction.ecocyc.URIDYLREM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_component_of` --> [[complex.ecocyc.CPLX0-10428|complex.ecocyc.CPLX0-10428]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00114|reaction.R00114]] `KEGG` `database` - 2 C00025 + C00006 <=> C00064 + C00026 + C00005 + C00080
- `is_product_of` --> [[reaction.R00253|reaction.R00253]] `KEGG` `database` - C00002 + C00025 + C00014 <=> C00008 + C00009 + C00064
- `is_product_of` --> [[reaction.ecocyc.ABC-12-RXN|reaction.ecocyc.ABC-12-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUTAMATESYN-RXN|reaction.ecocyc.GLUTAMATESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUTAMINESYN-RXN|reaction.ecocyc.GLUTAMINESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PRPPAMIDOTRANS-RXN|reaction.ecocyc.PRPPAMIDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6976|reaction.ecocyc.RXN0-6976]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6983|reaction.ecocyc.RXN0-6983]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-1549|reaction.ecocyc.TRANS-RXN-1549]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00256|reaction.R00256]] `KEGG` `database` - C00064 + C00001 <=> C00025 + C00014
- `is_substrate_of` --> [[reaction.R00573|reaction.R00573]] `KEGG` `database` - C00002 + C00075 + C00064 + C00001 <=> C00008 + C00009 + C00063 + C00025
- `is_substrate_of` --> [[reaction.R00575|reaction.R00575]] `KEGG` `database` - 2 C00002 + C00064 + C00288 + C00001 <=> 2 C00008 + C00009 + C00025 + C00169
- `is_substrate_of` --> [[reaction.R00578|reaction.R00578]] `KEGG` `database` - C00002 + C00049 + C00064 + C00001 <=> C00020 + C00013 + C00152 + C00025
- `is_substrate_of` --> [[reaction.R00579|reaction.R00579]] `KEGG` `database` - C00064 <=> C00819
- `is_substrate_of` --> [[reaction.R00768|reaction.R00768]] `KEGG` `database` - C00064 + C00085 <=> C00025 + C00352
- `is_substrate_of` --> [[reaction.R00986|reaction.R00986]] `KEGG` `database` - C00251 + C00064 <=> C00108 + C00022 + C00025
- `is_substrate_of` --> [[reaction.ecocyc.ABC-12-RXN|reaction.ecocyc.ABC-12-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ANTHRANSYN-RXN|reaction.ecocyc.ANTHRANSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ASNSYNB-RXN|reaction.ecocyc.ASNSYNB-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CARBPSYN-RXN|reaction.ecocyc.CARBPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CTPSYN-RXN|reaction.ecocyc.CTPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.FGAMSYN-RXN|reaction.ecocyc.FGAMSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTAMIDOTRANS-RXN|reaction.ecocyc.GLUTAMIDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTAMIN-RXN|reaction.ecocyc.GLUTAMIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTAMINE--TRNA-LIGASE-RXN|reaction.ecocyc.GLUTAMINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GMP-SYN-GLUT-RXN|reaction.ecocyc.GMP-SYN-GLUT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-RXN|reaction.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.NAD-SYNTH-GLN-RXN|reaction.ecocyc.NAD-SYNTH-GLN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PABASYN-RXN|reaction.ecocyc.PABASYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22790|reaction.ecocyc.RXN-22790]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23894|reaction.ecocyc.RXN-23894]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7449|reaction.ecocyc.RXN0-7449]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-1549|reaction.ecocyc.TRANS-RXN-1549]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLUTDEHYD-RXN|reaction.ecocyc.GLUTDEHYD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GSDEADENYLATION-RXN|reaction.ecocyc.GSDEADENYLATION-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-7378|reaction.ecocyc.RXN0-7378]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.ABC-12-CPLX|complex.ecocyc.ABC-12-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P63235|protein.P63235]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00064`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
