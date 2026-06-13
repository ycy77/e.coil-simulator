---
entity_id: "complex.ecocyc.CPLX0-10428"
entity_type: "complex"
name: "DNA-binding transcriptional regulator PtrR-L-glutamine"
source_database: "EcoCyc"
source_id: "CPLX0-10428"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "PtrR-L-glutamine"
  - "PtrR-gln"
---

# DNA-binding transcriptional regulator PtrR-L-glutamine

`complex.ecocyc.CPLX0-10428`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-10428`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P77309|protein.P77309]], [[molecule.C00064|molecule.C00064]]

## Enriched Summary

The LysR-type transcriptional regulator PtrR, putrescine utilization regulator, is involved in L-glutamate and putrescine metabolism and in resistance to the tetracycline group of antibiotics . Additionally, was predicted to regulate genes related to iron and succinate oxidation . PtrR contains a helix-turn-helix motif for DNA binding in its N-terminal domain . In systematic studies of oligomerization, it was shown that some members of the LysR family, like PtrR, interact with other members of the family to form heterodimers, but the physiological significance of this is unknown . The efficiency of PtrR binding to DNA was found to be more robust in the presence of Gln than Glu or putrescine . Genome-wide PtrR binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium and by ChIP-seq in M9 minimal medium with putrescine and with tryptone . The transcriptional response to the deletion of PtrR was characterized by RNA-seq in M9 minimal medium with Ptr and/or Glu as nitrogen source . By the integrative analysis of ChIP-exo and RNA-seq data, it was determined that PtrR directly represses the transcription of the sad gene (encoding the succinate-semialdehyde dehydrogenase) and probably fnrS]|...

## Annotation

The LysR-type transcriptional regulator PtrR, putrescine utilization regulator, is involved in L-glutamate and putrescine metabolism and in resistance to the tetracycline group of antibiotics . Additionally, was predicted to regulate genes related to iron and succinate oxidation . PtrR contains a helix-turn-helix motif for DNA binding in its N-terminal domain . In systematic studies of oligomerization, it was shown that some members of the LysR family, like PtrR, interact with other members of the family to form heterodimers, but the physiological significance of this is unknown . The efficiency of PtrR binding to DNA was found to be more robust in the presence of Gln than Glu or putrescine . Genome-wide PtrR binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium and by ChIP-seq in M9 minimal medium with putrescine and with tryptone . The transcriptional response to the deletion of PtrR was characterized by RNA-seq in M9 minimal medium with Ptr and/or Glu as nitrogen source . By the integrative analysis of ChIP-exo and RNA-seq data, it was determined that PtrR directly represses the transcription of the sad gene (encoding the succinate-semialdehyde dehydrogenase) and probably fnrS]|. In presence of γ-aminobutyric acid (GABA), PtrR unbinds, derepressing sad and fnrS genes . A knockout mutant for the ptrR gene showed deficiency in growth with L-glutamate and putrescine as nitrogen and energy sources; it was concluded that PtrR has an important role in regulation for putrescine utilization as an energy source . The ptrR mutant showed defects in growth with glycine, l-ornithine, or gamma-hydroxybutyrate in M9 medium with l-glutamate as the sole nitrogen source . The

## Outgoing Edges (4)

- `activates` --> [[gene.b2661|gene.b2661]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1297|gene.b1297]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1493|gene.b1493]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3517|gene.b3517]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (2)

- `is_component_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P77309|protein.P77309]] `EcoCyc` `database` - EcoCyc component coefficient=

## External IDs

- `EcoCyc:CPLX0-10428`

## Notes

protein.P77309|molecule.C00064
