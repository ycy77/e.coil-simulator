---
entity_id: "molecule.C04494"
entity_type: "small_molecule"
name: "Guanosine 3'-diphosphate 5'-triphosphate"
source_database: "KEGG"
source_id: "C04494"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Guanosine 3'-diphosphate 5'-triphosphate"
  - "Guanosine 5'-triphosphate,3'-diphosphate"
---

# Guanosine 3'-diphosphate 5'-triphosphate

`molecule.C04494`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04494`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Guanosine 3'-diphosphate 5'-triphosphate; Guanosine 5'-triphosphate,3'-diphosphate EcoCyc common name: pppGpp. The nucleotides GUANOSINE-5DP-3DP (guanosine 3'-diphosphate 5'-diphosphate) and GDP-TP (guanosine 3'-diphosphate 5'-triphosphate), referred to collectively as (p)ppGpp, have been shown to regulate gene expression during the stringent response in some bacteria. Their levels become elevated during this response and they are key indicators and regulators of it. The stringent response is a global regulatory system that operates under conditions of nutrient or energy starvation or other environmental stress. It has varying effects on gene expression and metabolism. In addition to bacteria, there is evidence that (p)ppGpp may regulate transcription by plastid-encoded RNA polymerase in plant chloroplasts . Due to its role as an effector molecule in the stringent response in bacteria, (p)ppGpp has been described as a bacterial alarmone. It can contribute to the regulation of various cellular processes that are affected by nutritional stress such as growth, cell division, motility, adaptation and virulence. Its effect on the pathogenicity of some bacteria has led to the development of ppGpp analogs as possible antibacterial compounds and new in vitro synthesis and detection methods for ppGpp...

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

KEGG compound: Guanosine 3'-diphosphate 5'-triphosphate; Guanosine 5'-triphosphate,3'-diphosphate

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (12)

- `activates` --> [[reaction.ecocyc.ORNDECARBOX-RXN|reaction.ecocyc.ORNDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN0-7352|reaction.ecocyc.RXN0-7352]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00429|reaction.R00429]] `KEGG` `database` - C00002 + C00044 <=> C00020 + C04494
- `is_product_of` --> [[reaction.ecocyc.GTPPYPHOSKIN-RXN|reaction.ecocyc.GTPPYPHOSKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R03409|reaction.R03409]] `KEGG` `database` - C04494 + C00001 <=> C01228 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.PPPGPPHYDRO-RXN|reaction.ecocyc.PPPGPPHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6427|reaction.ecocyc.RXN0-6427]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.3.6.1.41-RXN|reaction.ecocyc.3.6.1.41-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.EXOPOLYPHOSPHATASE-RXN|reaction.ecocyc.EXOPOLYPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.LYSDECARBOX-RXN|reaction.ecocyc.LYSDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5510|reaction.ecocyc.RXN0-5510]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-7283|reaction.ecocyc.RXN0-7283]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04494`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
