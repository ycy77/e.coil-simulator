---
entity_id: "protein.Q47150"
entity_type: "protein"
name: "dinJ"
source_database: "UniProt"
source_id: "Q47150"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dinJ b0226 JW0216"
---

# dinJ

`protein.Q47150`

## Static

- Type: `protein`
- Source: `UniProt:Q47150`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system (PubMed:17263853). A labile antitoxin that counteracts the effect of cognate toxin YafQ (PubMed:17263853). YafQ and DinJ together bind their own promoter, and repress its expression (PubMed:24898247). There are 2 operators with imperfect inverted repeats (IR) in the dinJ promoter, YafQ-(DinJ)2-YafQ only binds to the first (most upstream) of them to repress transcription; binding to a single IR is sufficient for activity in vivo and in vitro (PubMed:24898247). DinJ alone is as potent a transcriptional repressor as the heterotetramer and also only needs to bind 1 IR to act (PubMed:24898247). {ECO:0000269|PubMed:17263853, ECO:0000269|PubMed:24898247}.; FUNCTION: Cell death governed by the MazE-MazF and DinJ-YafQ TA systems seems to play a role in biofilm formation (PubMed:19707553). {ECO:0000269|PubMed:19707553}. DinJ acts as the antitoxin of the YafQ toxin by binding to YafQ and abolishing its RNase activity. DinJ can be specifically degraded by the Lon and ClpXP proteases . DinJ belongs to the ribbon-helix-helix (RHH) family of transcription factors . DinJ influences the RpoS-regulated general stress response by repressing transcription of cspE . The dinJ gene was first identified as a chromosomal locus containing a predicted high affinity operator site for the LexA repressor...

## Biological Role

Component of DinJ-YafQ antitoxin/toxin complex / DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-7787), DinJ-YafQ-phosphate (complex.ecocyc.CPLX0-8580).

## Annotation

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system (PubMed:17263853). A labile antitoxin that counteracts the effect of cognate toxin YafQ (PubMed:17263853). YafQ and DinJ together bind their own promoter, and repress its expression (PubMed:24898247). There are 2 operators with imperfect inverted repeats (IR) in the dinJ promoter, YafQ-(DinJ)2-YafQ only binds to the first (most upstream) of them to repress transcription; binding to a single IR is sufficient for activity in vivo and in vitro (PubMed:24898247). DinJ alone is as potent a transcriptional repressor as the heterotetramer and also only needs to bind 1 IR to act (PubMed:24898247). {ECO:0000269|PubMed:17263853, ECO:0000269|PubMed:24898247}.; FUNCTION: Cell death governed by the MazE-MazF and DinJ-YafQ TA systems seems to play a role in biofilm formation (PubMed:19707553). {ECO:0000269|PubMed:19707553}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7787|complex.ecocyc.CPLX0-7787]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8580|complex.ecocyc.CPLX0-8580]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0226|gene.b0226]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47150`
- `KEGG:ecj:JW0216;eco:b0226;ecoc:C3026_01070;ecoc:C3026_23810;`
- `GeneID:944914;`
- `GO:GO:0000987; GO:0003677; GO:0006351; GO:0015643; GO:0040008; GO:0042803; GO:0044010; GO:0045892; GO:0097532; GO:0110001; GO:2000143`

## Notes

Antitoxin DinJ
