---
entity_id: "protein.P77300"
entity_type: "protein"
name: "xynR"
source_database: "UniProt"
source_id: "P77300"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xynR yagI b0272 JW0265"
---

# xynR

`protein.P77300`

## Static

- Type: `protein`
- Source: `UniProt:P77300`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in regulation of xylonate catabolism. Represses the expression of both yagA and yagEF operons. Binds mainly at a single site within the spacer of the bidirectional transcription units yagA and yagEF. {ECO:0000269|PubMed:29087459}. XynR, which contains a helix-turn-helix motif to bind DNA in its N-terminal domain, appears to belong to the IclR family of transcription factors (TFs) . Based on SELEX screening of Escherichia coli K-12 W3110, XynR, formerly known as YagI, was identified as a regulator of xylonate catabolism; it is a rare single-target TF, and its regulation network is still fixed within the CR4-6 prophage without significant cross-talk with the host. It regulates the bidirectional transcripts yagA(b) and yagEF(GH) . A single peak of XynR binding was identified within the spacer of bidirectional transcription units of the yagA and yagEF operons. However, by decreasing the cutoff of detection, approximately 30 low-level peaks were detected, which are all located inside open reading frames (ORFs) . The level of XynR was detectable in the exponential growth phase, but it decreased to an undetectable level during growth in the stationary phase . Upstream of the xynR gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the xynR gene is affected by stress and glucose-lactose shift...

## Biological Role

Component of XynR-D-xylonate (complex.ecocyc.CPLX0-8257).

## Annotation

FUNCTION: Involved in regulation of xylonate catabolism. Represses the expression of both yagA and yagEF operons. Binds mainly at a single site within the spacer of the bidirectional transcription units yagA and yagEF. {ECO:0000269|PubMed:29087459}.

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8257|complex.ecocyc.CPLX0-8257]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0266|gene.b0266]] `RegulonDB` `C` - regulator=XynR; target=yagB; function=-
- `represses` --> [[gene.b0267|gene.b0267]] `RegulonDB` `C` - regulator=XynR; target=yagA; function=-
- `represses` --> [[gene.b0268|gene.b0268]] `RegulonDB` `C` - regulator=XynR; target=yagE; function=-
- `represses` --> [[gene.b0269|gene.b0269]] `RegulonDB` `C` - regulator=XynR; target=yagF; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0272|gene.b0272]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77300`
- `KEGG:ecj:JW0265;eco:b0272;ecoc:C3026_01320;`
- `GeneID:945016;`
- `GO:GO:0000976; GO:0003677; GO:0003700; GO:0044010; GO:0045892`

## Notes

HTH-type transcriptional regulator XynR (Regulator of xylonate catabolism)
