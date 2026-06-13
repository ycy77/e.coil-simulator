---
entity_id: "protein.P37013"
entity_type: "protein"
name: "norR"
source_database: "UniProt"
source_id: "P37013"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "norR ygaA b2709 JW5843"
---

# norR

`protein.P37013`

## Static

- Type: `protein`
- Source: `UniProt:P37013`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Required for the expression of anaerobic nitric oxide (NO) reductase, acts as a transcriptional activator for at least the norVW operon. Activation also requires sigma-54. Not required for induction of the aerobic NO-detoxifying enzyme NO dioxygenase. Binds to the promoter region of norVW, to a consensus target sequence, GT-(N7)-AC, which is highly conserved among proteobacteria. {ECO:0000269|PubMed:11751865, ECO:0000269|PubMed:12586421}. NorR, "NO reduction and detoxification Regulator," is one of several regulatory proteins, such as Fur, SoxR, and OxyR, that are involved in the response to reactive nitrogen species. Under anaerobic and microaerobic conditions it activates transcription of the norVW operon, encoding a nitric oxide (NO)-reducing flavorubredoxin that detoxifies NO . It was determined by Genomic SELEX screening that NorR binds strongly only between norR and norVW, and it binds with minor strength between genes such as sad/yneJ and glpF/zapB . It has been classified as a single-target transcription factor . A norR mutant is completely defective with respect to anaerobic NO detoxification and is sensitive to reactive nitrogen intermediates generated from nitroprusside. The norR gene is transcribed divergently from norVW and autoregulated . It is activated in the absence of oxygen and by nitrite under anaerobic conditions...

## Annotation

FUNCTION: Required for the expression of anaerobic nitric oxide (NO) reductase, acts as a transcriptional activator for at least the norVW operon. Activation also requires sigma-54. Not required for induction of the aerobic NO-detoxifying enzyme NO dioxygenase. Binds to the promoter region of norVW, to a consensus target sequence, GT-(N7)-AC, which is highly conserved among proteobacteria. {ECO:0000269|PubMed:11751865, ECO:0000269|PubMed:12586421}.

## Outgoing Edges (3)

- `activates` --> [[gene.b2710|gene.b2710]] `RegulonDB` `C` - regulator=NorR; target=norV; function=+
- `activates` --> [[gene.b2711|gene.b2711]] `RegulonDB` `C` - regulator=NorR; target=norW; function=+
- `represses` --> [[gene.b2709|gene.b2709]] `RegulonDB` `C` - regulator=NorR; target=norR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2709|gene.b2709]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37013`
- `KEGG:ecj:JW5843;eco:b2709;ecoc:C3026_14910;`
- `GeneID:947186;`
- `GO:GO:0000160; GO:0000987; GO:0001216; GO:0003700; GO:0005524; GO:0008198; GO:0032993; GO:0042802; GO:0045893; GO:0070026; GO:2000144`

## Notes

Anaerobic nitric oxide reductase transcription regulator NorR
