---
entity_id: "molecule.C00075"
entity_type: "small_molecule"
name: "UTP"
source_database: "KEGG"
source_id: "C00075"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "UTP"
  - "Uridine 5'-triphosphate"
  - "Uridine triphosphate"
---

# UTP

`molecule.C00075`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00075`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: UTP; Uridine 5'-triphosphate; Uridine triphosphate

## Biological Role

Consumed as substrate in 18 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: UTP; Uridine 5'-triphosphate; Uridine triphosphate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (28)

- `activates` --> [[reaction.ecocyc.GSDEADENYLATION-RXN|reaction.ecocyc.GSDEADENYLATION-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN0-5359|reaction.ecocyc.RXN0-5359]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00156|reaction.R00156]] `KEGG` `database` - C00002 + C00015 <=> C00008 + C00075
- `is_product_of` --> [[reaction.ecocyc.UDPKIN-RXN|reaction.ecocyc.UDPKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00289|reaction.R00289]] `KEGG` `database` - C00075 + C00103 <=> C00013 + C00029
- `is_substrate_of` --> [[reaction.R00416|reaction.R00416]] `KEGG` `database` - C00075 + C04501 <=> C00013 + C00043
- `is_substrate_of` --> [[reaction.R00443|reaction.R00443]] `KEGG` `database` - C00075 + C00046 <=> C00013 + C00046
- `is_substrate_of` --> [[reaction.R00571|reaction.R00571]] `KEGG` `database` - C00002 + C00075 + C00014 <=> C00008 + C00009 + C00063
- `is_substrate_of` --> [[reaction.R00573|reaction.R00573]] `KEGG` `database` - C00002 + C00075 + C00064 + C00001 <=> C00008 + C00009 + C00063 + C00025
- `is_substrate_of` --> [[reaction.R00659|reaction.R00659]] `KEGG` `database` - C00075 + C00022 <=> C00015 + C00074
- `is_substrate_of` --> [[reaction.R00662|reaction.R00662]] `KEGG` `database` - C00075 + C00001 <=> C00105 + C00013
- `is_substrate_of` --> [[reaction.R00769|reaction.R00769]] `KEGG` `database` - C00075 + C00085 <=> C00015 + C00354
- `is_substrate_of` --> [[reaction.R04733|reaction.R04733]] `KEGG` `database` - C00075 + C05250 <=> C00013 + C05326
- `is_substrate_of` --> [[reaction.ecocyc.CTPSYN-RXN|reaction.ecocyc.CTPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUC1PURIDYLTRANS-RXN|reaction.ecocyc.GLUC1PURIDYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.NAG1P-URIDYLTRANS-RXN|reaction.ecocyc.NAG1P-URIDYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14139|reaction.ecocyc.RXN-14139]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14325|reaction.ecocyc.RXN-14325]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-724|reaction.ecocyc.RXN0-724]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7378|reaction.ecocyc.RXN0-7378]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-801|reaction.ecocyc.RXN0-801]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.URITRANS-RXN|reaction.ecocyc.URITRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.CYTIDINEKIN-RXN|reaction.ecocyc.CYTIDINEKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN|reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-12002|reaction.ecocyc.RXN-12002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-7079|reaction.ecocyc.RXN0-7079]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.THI-P-SYN-RXN|reaction.ecocyc.THI-P-SYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.URKI-RXN|reaction.ecocyc.URKI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00075`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
