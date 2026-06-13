---
entity_id: "molecule.C01228"
entity_type: "small_molecule"
name: "Guanosine 3',5'-bis(diphosphate)"
source_database: "KEGG"
source_id: "C01228"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Guanosine 3',5'-bis(diphosphate)"
  - "Guanosine 3'-diphosphate 5'-diphosphate"
  - "Guanosine 5'-diphosphate,3'-diphosphate"
---

# Guanosine 3',5'-bis(diphosphate)

`molecule.C01228`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01228`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Guanosine 3',5'-bis(diphosphate); Guanosine 3'-diphosphate 5'-diphosphate; Guanosine 5'-diphosphate,3'-diphosphate EcoCyc common name: ppGpp. The nucleotides GUANOSINE-5DP-3DP (guanosine 3'-diphosphate 5'-diphosphate) and GDP-TP (guanosine 3'-diphosphate 5'-triphosphate), referred to collectively as (p)ppGpp, have been shown to regulate gene expression during the stringent response in some bacteria. Their levels become elevated during this response and they are key indicators and regulators of it. The stringent response is a global regulatory system that operates under conditions of nutrient or energy starvation or other environmental stress. It has varying effects on gene expression and metabolism. In addition to bacteria, there is evidence that (p)ppGpp may regulate transcription by plastid-encoded RNA polymerase in plant chloroplasts . Due to its role as an effector molecule in the stringent response in bacteria, (p)ppGpp has been described as a bacterial alarmone. It can contribute to the regulation of various cellular processes that are affected by nutritional stress such as growth, cell division, motility, adaptation and virulence. The deficiency of (p)ppGpp causes a growth defect under conditions that decrease the ratio of unsaturated fatty acids (UFA) to saturated fatty acids (SFA) in the membrane...

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

KEGG compound: Guanosine 3',5'-bis(diphosphate); Guanosine 3'-diphosphate 5'-diphosphate; Guanosine 5'-diphosphate,3'-diphosphate

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (26)

- `activates` --> [[reaction.ecocyc.ORNDECARBOX-RXN|reaction.ecocyc.ORNDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.PEPCARBOX-RXN|reaction.ecocyc.PEPCARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN0-7352|reaction.ecocyc.RXN0-7352]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.URACIL-PRIBOSYLTRANS-RXN|reaction.ecocyc.URACIL-PRIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_component_of` --> [[complex.ecocyc.CPLX0-8070|complex.ecocyc.CPLX0-8070]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R03409|reaction.R03409]] `KEGG` `database` - C04494 + C00001 <=> C01228 + C00009
- `is_product_of` --> [[reaction.ecocyc.GDPPYPHOSKIN-RXN|reaction.ecocyc.GDPPYPHOSKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PPPGPPHYDRO-RXN|reaction.ecocyc.PPPGPPHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00336|reaction.R00336]] `KEGG` `database` - C01228 + C00001 <=> C00035 + C00013
- `is_substrate_of` --> [[reaction.ecocyc.PPGPPSYN-RXN|reaction.ecocyc.PPGPPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6707|reaction.ecocyc.RXN0-6707]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7291|reaction.ecocyc.RXN0-7291]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.3.6.1.41-RXN|reaction.ecocyc.3.6.1.41-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ADENPRIBOSYLTRAN-RXN|reaction.ecocyc.ADENPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN|reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.EXOPOLYPHOSPHATASE-RXN|reaction.ecocyc.EXOPOLYPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GDPPYPHOSKIN-RXN|reaction.ecocyc.GDPPYPHOSKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GUANPRIBOSYLTRAN-RXN|reaction.ecocyc.GUANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN|reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.IMP-DEHYDROG-RXN|reaction.ecocyc.IMP-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.LYSDECARBOX-RXN|reaction.ecocyc.LYSDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ORNDECARBOX-RXN|reaction.ecocyc.ORNDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PPPGPPHYDRO-RXN|reaction.ecocyc.PPPGPPHYDRO-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PRPPAMIDOTRANS-RXN|reaction.ecocyc.PRPPAMIDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5510|reaction.ecocyc.RXN0-5510]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-7283|reaction.ecocyc.RXN0-7283]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01228`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
