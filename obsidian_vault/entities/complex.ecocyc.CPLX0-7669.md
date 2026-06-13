---
entity_id: "complex.ecocyc.CPLX0-7669"
entity_type: "complex"
name: "DNA-binding transcriptional dual regulator ArgP"
source_database: "EcoCyc"
source_id: "CPLX0-7669"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA-binding transcriptional dual regulator ArgP

`complex.ecocyc.CPLX0-7669`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7669`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A8S1|protein.P0A8S1]]

## Enriched Summary

ArgP, for "arginine protein," controls the transcription of genes involved in the arginine transport system and genes involved in DNA replication. DNA replication is also regulated directly by ArgP when the protein binds to three 13-mers located in the origin of replication (OriC), which blocks the DNA opening by DnaA and inhibits this cellular process . DNA binding by ArgP is prevented when the serine protease Do (DegP) hydrolyzes this transcriptional regulator . ArgP was first identified as an inhibitor of oriC-initiated DNA replication in vitro. It has also subsequently been described as a nucleoid-associated protein that shows apparently sequence-nonspecific DNA-binding activity . ArgP is a noncanonical regulator, as it binds to a number of additional sites in the genome without an apparent direct regulatory effect, exhibiting low-affinity binding to these additional sites . To activate transcription, ArgP recognizes AT-rich DNA-binding sites, but no consensus sequence has been identified. However, recent studies showed that the operator for ArgP consists of two subsites, each one being most likely contacted by two ArgP subunits, and there is sequence specificity of ArgP binding, with a half-site consensus sequence, 5-CTTAT-, involved in effector-free ArgP binding...

## Biological Role

Component of ArgP-L-lysine (complex.ecocyc.CPLX0-7670), ArgP-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7671).

## Annotation

ArgP, for "arginine protein," controls the transcription of genes involved in the arginine transport system and genes involved in DNA replication. DNA replication is also regulated directly by ArgP when the protein binds to three 13-mers located in the origin of replication (OriC), which blocks the DNA opening by DnaA and inhibits this cellular process . DNA binding by ArgP is prevented when the serine protease Do (DegP) hydrolyzes this transcriptional regulator . ArgP was first identified as an inhibitor of oriC-initiated DNA replication in vitro. It has also subsequently been described as a nucleoid-associated protein that shows apparently sequence-nonspecific DNA-binding activity . ArgP is a noncanonical regulator, as it binds to a number of additional sites in the genome without an apparent direct regulatory effect, exhibiting low-affinity binding to these additional sites . To activate transcription, ArgP recognizes AT-rich DNA-binding sites, but no consensus sequence has been identified. However, recent studies showed that the operator for ArgP consists of two subsites, each one being most likely contacted by two ArgP subunits, and there is sequence specificity of ArgP binding, with a half-site consensus sequence, 5-CTTAT-, involved in effector-free ArgP binding . On the other hand, the alternative binding site (ABS'; T-N11-A from 47 to 37) in the argO operator is preferentially bound in the presence of arginine and it is crucial for transcription activation . ArgP induces bending on argO and lysP operators with angles of approximately 60 and 56 , respectively, and without significant differences in the absence versus presence of arginine or lysine . When this protein activates genes involved in replication, it appears to bind to their regulatory regions without a

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7670|complex.ecocyc.CPLX0-7670]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-7671|complex.ecocyc.CPLX0-7671]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A8S1|protein.P0A8S1]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7669`
- `QSPROTEOME:QS00049634`

## Notes

2*protein.P0A8S1
