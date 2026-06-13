---
entity_id: "protein.ecocyc.PHOSPHO-TORR"
entity_type: "complex"
name: "DNA-binding transcriptional dual regulator TorR-phosphorylated"
source_database: "EcoCyc"
source_id: "PHOSPHO-TORR"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "TorR"
  - "TorR response regulator - phosphorylated"
  - "TorR-P<SUP>asp53</SUP>"
---

# DNA-binding transcriptional dual regulator TorR-phosphorylated

`protein.ecocyc.PHOSPHO-TORR`

## Static

- Type: `complex`
- Source: `EcoCyc:PHOSPHO-TORR`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `regulatory`
- Components: [[protein.P38684|protein.P38684]]

## Enriched Summary

TorR is a transcriptional DNA-binding dual regulator , as a positive regulator for genes related to TMAO (trimethylamine N-oxide) induction and the enzymes of tryptophan metabolism and as a negative regulator of glutamate decarboxylase genes and of its own expression . TorR could mediate anaerobic regulation . TorR is involved in alkaline and acid stress responses . Under extreme acidic environments, phosporylated TorR directly activates transcription of rpoS and various acid resistance genes . TorR is a response regulator of a two-component regulatory system , and torS encodes the sensor partner of TorR . In the presence of TMAO, TorS is an unorthodox sensor that autophosphorylates, and the phosphoryl group is transferred to TorR via a four-step phosphorelay, His443-Asp723-His850-Asp(TorR) which, in turn, activates transcription of torCAD . There is strong experimental evidence that TorR is dephosphorylated by TorS, using only the His850 and Asp723 residues of TorS . The TorR protein can be phosphorylated by TorS and by other kinases (probably by a Hanks model Ser/Thr kinase) . The autoregulation of TorR occurs in its phosphorylated and also its unphosphorylated form . In addition, it is TMAO independent and still occurs in a torS mutant . torR negative autoregulation likely maintains the TorR concentration at a low level, whatever the growth conditions...

## Annotation

TorR is a transcriptional DNA-binding dual regulator , as a positive regulator for genes related to TMAO (trimethylamine N-oxide) induction and the enzymes of tryptophan metabolism and as a negative regulator of glutamate decarboxylase genes and of its own expression . TorR could mediate anaerobic regulation . TorR is involved in alkaline and acid stress responses . Under extreme acidic environments, phosporylated TorR directly activates transcription of rpoS and various acid resistance genes . TorR is a response regulator of a two-component regulatory system , and torS encodes the sensor partner of TorR . In the presence of TMAO, TorS is an unorthodox sensor that autophosphorylates, and the phosphoryl group is transferred to TorR via a four-step phosphorelay, His443-Asp723-His850-Asp(TorR) which, in turn, activates transcription of torCAD . There is strong experimental evidence that TorR is dephosphorylated by TorS, using only the His850 and Asp723 residues of TorS . The TorR protein can be phosphorylated by TorS and by other kinases (probably by a Hanks model Ser/Thr kinase) . The autoregulation of TorR occurs in its phosphorylated and also its unphosphorylated form . In addition, it is TMAO independent and still occurs in a torS mutant . torR negative autoregulation likely maintains the TorR concentration at a low level, whatever the growth conditions . Furthermore, using a DNA array technology, seven new transcriptional units involved in alkaline stress and whose expression is under positive and negative control by the TorS/TorR phosphorelay system have been identified . Based on its C terminal, TorR has been recognized as a member of the PhoB-OmpR subfamily of response regulators, which includes numerous members in E. coli that regulate transcription of specific ta

## Outgoing Edges (11)

- `activates` --> [[gene.b1492|gene.b1492]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1493|gene.b1493]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2741|gene.b2741]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3506|gene.b3506]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3512|gene.b3512]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3513|gene.b3513]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3514|gene.b3514]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3516|gene.b3516]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3517|gene.b3517]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4115|gene.b4115]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4117|gene.b4117]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P38684|protein.P38684]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PHOSPHO-TORR`
- `PRODB:PRO_000025452`

## Notes

2*protein.P38684
