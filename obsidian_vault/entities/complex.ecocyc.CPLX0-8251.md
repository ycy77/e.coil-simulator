---
entity_id: "complex.ecocyc.CPLX0-8251"
entity_type: "complex"
name: "amino acid racemase YgeA"
source_database: "EcoCyc"
source_id: "CPLX0-8251"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# amino acid racemase YgeA

`complex.ecocyc.CPLX0-8251`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8251`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P03813|protein.P03813]]

## Enriched Summary

YgeA was reported to be an amino acid racemase with broad substrate specificity, but low catalytic activity. The preferred substrate for YgeA is homoserine . Conversely, reported crystal structures and enzymatic activity for an enzyme that differs in only one amino acid residue, 178 (Cys in K-12 MG1655, Tyr in BL21(DE3)). The BL21(DE3) enzyme is reported to catalyze only unidirectional racemase activity from L-Glu/Asp to D-Glu/Asp. Changing the T83 residue within the active site (shared between the two enzymes) to C (observed in bidirectional amino acid racemases) increased the D-to-L activity of the enzyme . Crystal structures of the enzyme from E. coli O157:H7 str. SS52, whose sequence is identical to that of E. coli BL21(DE3), provide a potential explanation for the unidirectional catalytic activity of that enzyme . YgeA was predicted to be an amino acid racemase by . YgeA was reported to be an amino acid racemase with broad substrate specificity, but low catalytic activity. The preferred substrate for YgeA is homoserine . Conversely, reported crystal structures and enzymatic activity for an enzyme that differs in only one amino acid residue, 178 (Cys in K-12 MG1655, Tyr in BL21(DE3)). The BL21(DE3) enzyme is reported to catalyze only unidirectional racemase activity from L-Glu/Asp to D-Glu/Asp...

## Biological Role

Catalyzes homoserine racemase (reaction.ecocyc.RXN0-7285).

## Annotation

YgeA was reported to be an amino acid racemase with broad substrate specificity, but low catalytic activity. The preferred substrate for YgeA is homoserine . Conversely, reported crystal structures and enzymatic activity for an enzyme that differs in only one amino acid residue, 178 (Cys in K-12 MG1655, Tyr in BL21(DE3)). The BL21(DE3) enzyme is reported to catalyze only unidirectional racemase activity from L-Glu/Asp to D-Glu/Asp. Changing the T83 residue within the active site (shared between the two enzymes) to C (observed in bidirectional amino acid racemases) increased the D-to-L activity of the enzyme . Crystal structures of the enzyme from E. coli O157:H7 str. SS52, whose sequence is identical to that of E. coli BL21(DE3), provide a potential explanation for the unidirectional catalytic activity of that enzyme . YgeA was predicted to be an amino acid racemase by .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7285|reaction.ecocyc.RXN0-7285]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P03813|protein.P03813]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8251`
- `QSPROTEOME:QS00199651`

## Notes

2*protein.P03813
