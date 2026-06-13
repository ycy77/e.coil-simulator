---
entity_id: "protein.P30958"
entity_type: "protein"
name: "mfd"
source_database: "UniProt"
source_id: "P30958"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00969}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mfd b1114 JW1100"
---

# mfd

`protein.P30958`

## Static

- Type: `protein`
- Source: `UniProt:P30958`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00969}.

## Enriched Summary

FUNCTION: Couples transcription and DNA repair by recognizing RNA polymerase (RNAP) stalled at DNA lesions. Mediates ATP-dependent release of RNAP and its truncated transcript from the DNA, and recruitment of nucleotide excision repair machinery to the damaged site. Can also dissociate RNAP that is blocked by low concentration of nucleoside triphosphates or by physical obstruction, such as bound proteins. In addition, can rescue arrested complexes by promoting forward translocation. Has ATPase activity, which is required for removal of stalled RNAP, but seems to lack helicase activity. May act through a translocase activity that rewinds upstream DNA, leading either to translocation or to release of RNAP when the enzyme active site cannot continue elongation. {ECO:0000255|HAMAP-Rule:MF_00969, ECO:0000269|PubMed:12086674, ECO:0000269|PubMed:19700770, ECO:0000269|PubMed:7876261, ECO:0000269|PubMed:7876262, ECO:0000269|PubMed:8465200}. The Mfd protein, also known as transcription-repair coupling factor (TRCF) , is responsible for ATP-dependent displacement of stalled RNA polymerase (RNAP) from DNA lesions with concomitant recruitment of UVRABC-CPLX "nucleotide excision repair" machinery to the site of damage . Mfd facilitates the repair of template strand lesions...

## Enriched Pathways

- `eco03420` Nucleotide excision repair (KEGG)

## Annotation

FUNCTION: Couples transcription and DNA repair by recognizing RNA polymerase (RNAP) stalled at DNA lesions. Mediates ATP-dependent release of RNAP and its truncated transcript from the DNA, and recruitment of nucleotide excision repair machinery to the damaged site. Can also dissociate RNAP that is blocked by low concentration of nucleoside triphosphates or by physical obstruction, such as bound proteins. In addition, can rescue arrested complexes by promoting forward translocation. Has ATPase activity, which is required for removal of stalled RNAP, but seems to lack helicase activity. May act through a translocase activity that rewinds upstream DNA, leading either to translocation or to release of RNAP when the enzyme active site cannot continue elongation. {ECO:0000255|HAMAP-Rule:MF_00969, ECO:0000269|PubMed:12086674, ECO:0000269|PubMed:19700770, ECO:0000269|PubMed:7876261, ECO:0000269|PubMed:7876262, ECO:0000269|PubMed:8465200}.

## Pathways

- `eco03420` Nucleotide excision repair (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1114|gene.b1114]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30958`
- `KEGG:ecj:JW1100;eco:b1114;ecoc:C3026_06715;`
- `GeneID:75203700;945681;`
- `GO:GO:0000716; GO:0003677; GO:0003684; GO:0005524; GO:0005829; GO:0006281; GO:0006283; GO:0006294; GO:0006355; GO:0006974; GO:0015616; GO:0016787; GO:0043175; GO:1990391`
- `EC:3.6.4.-`

## Notes

Transcription-repair-coupling factor (TRCF) (EC 3.6.4.-)
