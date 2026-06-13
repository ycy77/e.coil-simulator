---
entity_id: "protein.P77402"
entity_type: "protein"
name: "ydiP"
source_database: "UniProt"
source_id: "P77402"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydiP b1696 JW1686"
---

# ydiP

`protein.P77402`

## Static

- Type: `protein`
- Source: `UniProt:P77402`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Uncharacterized HTH-type transcriptional regulator YdiP YdiP is an AraC-type transcription factor , involved in the cold shock response . It contains a helix-turn-helix motif to bind DNA in its C-terminal domain . YdiP DNA-binding activity was probed in vivo in glucose M9 minimal medium through chromatin immunoprecipitation assays (ChIP-exo) . It was predicted that this protein regulates genes related to metabolism . However, the effect of YdiP on the transcription of any gene has not yet been demonstrated . In LB medium, the YdiP protein abundance was increased after 2 h of shifting to cold shock at 15°C relative to activity at 37°C . At 15°C but not at 37°C, YdiP binds with CspA, CspB, CspE, CspG, and CspI proteins in rich medium and with CspE in minimal medium . A ydiP knockout mutant showed impaired growth at 15°C but not at 37°C compared to wild type . This defect was exacerbated when cspABEGI was also deleted . YdiP protein abundance was increased after adaptation to 10°C relative to that at 37°C . ydiP transcript level was increased 4 h after a shift to 15°C relative to abundance at 37°C . At 15°C but not at 37°C, a ydiP mutant grown in LB medium or M9 minimal medium formed long filamentous cells; ydiP overexpression in a ydiP mutant rescued the filamentous phenotype . Interconnectivity between ydiP gene and the gene encoding the TF CspA has been reported...

## Annotation

Uncharacterized HTH-type transcriptional regulator YdiP

## Outgoing Edges (2)

- `activates` --> [[gene.b0623|gene.b0623]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3556|gene.b3556]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b1696|gene.b1696]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77402`
- `KEGG:ecj:JW1686;eco:b1696;ecoc:C3026_09710;`
- `GeneID:945095;`
- `GO:GO:0000976; GO:0003700; GO:0006355`

## Notes

Uncharacterized HTH-type transcriptional regulator YdiP
