---
entity_id: "protein.P11866"
entity_type: "protein"
name: "tdcR"
source_database: "UniProt"
source_id: "P11866"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tdcR b3119 JW5525"
---

# tdcR

`protein.P11866`

## Static

- Type: `protein`
- Source: `UniProt:P11866`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probable trans-acting positive activator for the tdc operon. During anaerobiosis, TdcR participates in controlling several genes involved in transport and metabolism of threonine and serine . TdcR has a helix-turn-helix motif that shows 25% and 35% identity to the same motifs of the transcriptional regulators NtrC and Fis, respectively . It appears that due to the fact that the tdcR gene shows poor codon usage and a poor Shine-Dalgarno sequence, it is weakly expressed . tdcR is transcribed alone and is located divergently in the genome from the operon (tdcABCD), whose transcription is activated by TdcR. The first gene of the operon codes for TdcA, a transcriptional regulator that probably interacts with TdcR to activate the transcription of the operon , and these two proteins appear to function together with CRP and IHF, proteins that bend the DNA, for this activation . tdc: "threonine dehydratase" .

## Annotation

FUNCTION: Probable trans-acting positive activator for the tdc operon.

## Outgoing Edges (7)

- `activates` --> [[gene.b3113|gene.b3113]] `RegulonDB` `S` - regulator=TdcR; target=tdcF; function=+
- `activates` --> [[gene.b3114|gene.b3114]] `RegulonDB` `S` - regulator=TdcR; target=tdcE; function=+
- `activates` --> [[gene.b3115|gene.b3115]] `RegulonDB` `S` - regulator=TdcR; target=tdcD; function=+
- `activates` --> [[gene.b3116|gene.b3116]] `RegulonDB` `S` - regulator=TdcR; target=tdcC; function=+
- `activates` --> [[gene.b3117|gene.b3117]] `RegulonDB` `S` - regulator=TdcR; target=tdcB; function=+
- `activates` --> [[gene.b3118|gene.b3118]] `RegulonDB` `S` - regulator=TdcR; target=tdcA; function=+
- `activates` --> [[gene.b4471|gene.b4471]] `RegulonDB` `S` - regulator=TdcR; target=tdcG; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b3119|gene.b3119]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11866`
- `KEGG:ecj:JW5525;eco:b3119;`
- `GeneID:944907;`
- `GO:GO:0003677; GO:0045893`

## Notes

Threonine dehydratase operon activator protein
