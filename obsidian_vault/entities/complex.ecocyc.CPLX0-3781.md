---
entity_id: "complex.ecocyc.CPLX0-3781"
entity_type: "complex"
name: "YefM-YoeB antitoxin/toxin complex / DNA-binding transcriptional repressor"
source_database: "EcoCyc"
source_id: "CPLX0-3781"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "YefMB"
  - "YefM-YoeB"
---

# YefM-YoeB antitoxin/toxin complex / DNA-binding transcriptional repressor

`complex.ecocyc.CPLX0-3781`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3781`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P69348|protein.P69348]], [[protein.P69346|protein.P69346]]

## Enriched Summary

YefM is a transcriptional DNA-binding autorepressor for the yefM-yoeB operon. In addition, YefM also functions as an antitoxin to form a complex with YoeB, which is a toxin that is counteracted by YefM antitoxin . YefM can bind alone with low affinity to the yefM-yoeB operator, but together with YoeB it has an enhanced DNA-binding affinity compared to free YefM . YoeB enhances the interaction with YefM by affecting the YefM conformation to one that is more favorable for DNA binding and/or by stabilizing the nucleoprotein complex at the operator site and reducing basal expression of the yefM-yoeB operon . The yefM gene is upregulated during growth in biofilms and yefM-yoeB is upregulated in persister cells ; it is probable that derepression of yefM-yoeB autoregulation occurs in these circumstances in response to an as-yet-unknown environmental or cell cycle signal(s) that interferes with the YefM-YoeB-operator interaction . The operator site 5' of yefM-yoeB comprises adjacent long (L) and short (S) palindromes with core 5'-TGTACA-3' motifs with a center-to-center distance of 12 bp , which was suggested to be crucial for the correct stable positioning of YefM-YoeB at the two repeats...

## Annotation

YefM is a transcriptional DNA-binding autorepressor for the yefM-yoeB operon. In addition, YefM also functions as an antitoxin to form a complex with YoeB, which is a toxin that is counteracted by YefM antitoxin . YefM can bind alone with low affinity to the yefM-yoeB operator, but together with YoeB it has an enhanced DNA-binding affinity compared to free YefM . YoeB enhances the interaction with YefM by affecting the YefM conformation to one that is more favorable for DNA binding and/or by stabilizing the nucleoprotein complex at the operator site and reducing basal expression of the yefM-yoeB operon . The yefM gene is upregulated during growth in biofilms and yefM-yoeB is upregulated in persister cells ; it is probable that derepression of yefM-yoeB autoregulation occurs in these circumstances in response to an as-yet-unknown environmental or cell cycle signal(s) that interferes with the YefM-YoeB-operator interaction . The operator site 5' of yefM-yoeB comprises adjacent long (L) and short (S) palindromes with core 5'-TGTACA-3' motifs with a center-to-center distance of 12 bp , which was suggested to be crucial for the correct stable positioning of YefM-YoeB at the two repeats . The palindrome L covers the whole -10 box and the S palindrome surrounds the transcription start site; because of these placements, the YoeB-YefM complex specifically represses the transcription of the system by blocking RNA polymerase binding .This sequence organization is common in yefM-yoeB regulatory regions in diverse genomes, suggesting that interaction of YefM-YoeB with these motifs is a conserved mechanism of operon autoregulation . The -35 region of the yefM-yoeB promoter does not have the conserved motif of σ70 promoters, and this results in a low transcriptional activity relative

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P69346|protein.P69346]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P69348|protein.P69348]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-3781`
- `PDB:2A6Q`
- `QSPROTEOME:QS00178061`

## Notes

1*protein.P69348|2*protein.P69346
