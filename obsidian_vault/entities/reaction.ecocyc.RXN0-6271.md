---
entity_id: "reaction.ecocyc.RXN0-6271"
entity_type: "reaction"
name: "RXN0-6271"
source_database: "EcoCyc"
source_id: "RXN0-6271"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6271

`reaction.ecocyc.RXN0-6271`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6271`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this reaction the sensor kinase phosphotransferase DpiB is autophosphorylated. Based on analogy to other sensor proteins the phosphorylation site is shown as a histidine residue. Sensor kinase phosphotransferase DpiB is a member of the DpiA/DpiB two component signal transduction pathway. The DpiA/DpiB system is involved in the transcriptional regulation of the genes for anaerobic citrate catabolism . EcoCyc reaction equation: ATP + G6345-MONOMER -> ADP + PHOSPHO-DPIB; direction=LEFT-TO-RIGHT. In this reaction the sensor kinase phosphotransferase DpiB is autophosphorylated. Based on analogy to other sensor proteins the phosphorylation site is shown as a histidine residue. Sensor kinase phosphotransferase DpiB is a member of the DpiA/DpiB two component signal transduction pathway. The DpiA/DpiB system is involved in the transcriptional regulation of the genes for anaerobic citrate catabolism .

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1499` DpiBA Two-Component Signal Transduction System (EcoCyc)

## Annotation

In this reaction the sensor kinase phosphotransferase DpiB is autophosphorylated. Based on analogy to other sensor proteins the phosphorylation site is shown as a histidine residue. Sensor kinase phosphotransferase DpiB is a member of the DpiA/DpiB two component signal transduction pathway. The DpiA/DpiB system is involved in the transcriptional regulation of the genes for anaerobic citrate catabolism .

## Pathways

- `ecocyc.PWY0-1499` DpiBA Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `activates` <-- [[molecule.C00158|molecule.C00158]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6271`

## Notes

ATP + G6345-MONOMER -> ADP + PHOSPHO-DPIB; direction=LEFT-TO-RIGHT
