---
entity_id: "protein.P0AAR0"
entity_type: "protein"
name: "tomB"
source_database: "UniProt"
source_id: "P0AAR0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tomB ybaJ b0461 JW0450"
---

# tomB

`protein.P0AAR0`

## Static

- Type: `protein`
- Source: `UniProt:P0AAR0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Attenuates Hha toxicity and regulates biofilm formation. Binds to various coding and intergenic regions of genomic DNA. {ECO:0000269|PubMed:16317765, ECO:0000269|PubMed:18545668}. The tomB-hha operon may encode an antitoxin-toxin module. Expression of TomB diminishes the toxicity of Hha expression. Both TomB and Hha were found to bind certain coding and intergenic regions of the genome . Transcription of tomB is induced upon biofilm formation . TomB: "toxin overexpression modulator in biofilms"

## Annotation

FUNCTION: Attenuates Hha toxicity and regulates biofilm formation. Binds to various coding and intergenic regions of genomic DNA. {ECO:0000269|PubMed:16317765, ECO:0000269|PubMed:18545668}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0461|gene.b0461]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAR0`
- `KEGG:ecj:JW0450;eco:b0461;ecoc:C3026_02260;`
- `GeneID:93776989;945106;`
- `GO:GO:0003677; GO:0005737; GO:0044010`

## Notes

Hha toxicity modulator TomB (Toxin overexpression modulator in biofilms)
