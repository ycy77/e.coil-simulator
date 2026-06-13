---
entity_id: "protein.P0A7B8"
entity_type: "protein"
name: "hslV"
source_database: "UniProt"
source_id: "P0A7B8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hslV htpO yiiC b3932 JW3903"
---

# hslV

`protein.P0A7B8`

## Static

- Type: `protein`
- Source: `UniProt:P0A7B8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Protease subunit of a proteasome-like degradation complex believed to be a general protein degrading machinery. The complex has been shown to be involved in the specific degradation of heat shock induced transcription factors such as RpoH and SulA. In addition, small hydrophobic peptides are also hydrolyzed by HslV. HslV has weak protease activity even in the absence of HslU, but this activity is induced more than 100-fold in the presence of HslU. HslU recognizes protein substrates and unfolds these before guiding them to HslV for hydrolysis. HslV is not believed to degrade folded proteins. {ECO:0000255|HAMAP-Rule:MF_00248, ECO:0000269|PubMed:10419524, ECO:0000269|PubMed:10452560, ECO:0000269|PubMed:15696175, ECO:0000269|PubMed:8650174, ECO:0000269|PubMed:8662828, ECO:0000269|PubMed:9288941, ECO:0000269|PubMed:9393683}.

## Biological Role

Component of HslV hexamer (complex.ecocyc.CPLX0-1162), HslVU protease (complex.ecocyc.CPLX0-1163).

## Annotation

FUNCTION: Protease subunit of a proteasome-like degradation complex believed to be a general protein degrading machinery. The complex has been shown to be involved in the specific degradation of heat shock induced transcription factors such as RpoH and SulA. In addition, small hydrophobic peptides are also hydrolyzed by HslV. HslV has weak protease activity even in the absence of HslU, but this activity is induced more than 100-fold in the presence of HslU. HslU recognizes protein substrates and unfolds these before guiding them to HslV for hydrolysis. HslV is not believed to degrade folded proteins. {ECO:0000255|HAMAP-Rule:MF_00248, ECO:0000269|PubMed:10419524, ECO:0000269|PubMed:10452560, ECO:0000269|PubMed:15696175, ECO:0000269|PubMed:8650174, ECO:0000269|PubMed:8662828, ECO:0000269|PubMed:9288941, ECO:0000269|PubMed:9393683}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1162|complex.ecocyc.CPLX0-1162]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `is_component_of` --> [[complex.ecocyc.CPLX0-1163|complex.ecocyc.CPLX0-1163]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12

## Incoming Edges (1)

- `encodes` <-- [[gene.b3932|gene.b3932]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7B8`
- `KEGG:ecj:JW3903;eco:b3932;ecoc:C3026_21250;`
- `GeneID:86861674;93777966;948429;`
- `GO:GO:0000287; GO:0004298; GO:0005524; GO:0005737; GO:0005829; GO:0005839; GO:0006508; GO:0009376; GO:0009408; GO:0019904; GO:0030164; GO:0034605; GO:0042802; GO:0051603`
- `EC:3.4.25.2`

## Notes

ATP-dependent protease subunit HslV (EC 3.4.25.2) (Heat shock protein HslV)
