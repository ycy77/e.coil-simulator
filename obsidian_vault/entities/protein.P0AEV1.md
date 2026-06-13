---
entity_id: "protein.P0AEV1"
entity_type: "protein"
name: "rssB"
source_database: "UniProt"
source_id: "P0AEV1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rssB hnr sprE ychL b1235 JW1223"
---

# rssB

`protein.P0AEV1`

## Static

- Type: `protein`
- Source: `UniProt:P0AEV1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Regulates the turnover of the sigma S factor (RpoS) by promoting its proteolysis in exponentially growing cells. Acts by binding and delivering RpoS to the ClpXP protease. RssB is not co-degraded with RpoS, but is released from the complex and can initiate a new cycle of RpoS recognition and degradation. In stationary phase, could also act as an anti-sigma factor and reduce the ability of RpoS to activate gene expression. Is also involved in the regulation of the mRNA polyadenylation pathway during stationary phase, probably by maintaining the association of PcnB with the degradosome. {ECO:0000255|HAMAP-Rule:MF_00958, ECO:0000269|PubMed:10672187, ECO:0000269|PubMed:11442836, ECO:0000269|PubMed:19767441, ECO:0000269|PubMed:20472786, ECO:0000269|PubMed:8635466, ECO:0000269|PubMed:8637901}. RssB is an adaptor protein that facilitates degradation of the alternative sigma factor RPOS-MONOMER σS by the protease ClpXP . RssB is specific to σS and has no effect on the stability of other ClpXP substrates . In the absence of ClpXP and upon overexpression of RssB, a direct anti-sigma factor effect of RssB on σS activity can also be observed . RssB was also found to modulate polyadenylation and thereby mRNA stability by affecting the activity and intracellular localization of EG10690-MONOMER (PAP I)...

## Annotation

FUNCTION: Regulates the turnover of the sigma S factor (RpoS) by promoting its proteolysis in exponentially growing cells. Acts by binding and delivering RpoS to the ClpXP protease. RssB is not co-degraded with RpoS, but is released from the complex and can initiate a new cycle of RpoS recognition and degradation. In stationary phase, could also act as an anti-sigma factor and reduce the ability of RpoS to activate gene expression. Is also involved in the regulation of the mRNA polyadenylation pathway during stationary phase, probably by maintaining the association of PcnB with the degradosome. {ECO:0000255|HAMAP-Rule:MF_00958, ECO:0000269|PubMed:10672187, ECO:0000269|PubMed:11442836, ECO:0000269|PubMed:19767441, ECO:0000269|PubMed:20472786, ECO:0000269|PubMed:8635466, ECO:0000269|PubMed:8637901}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1235|gene.b1235]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEV1`
- `KEGG:ecj:JW1223;eco:b1235;ecoc:C3026_07265;`
- `GeneID:93775301;945855;`
- `GO:GO:0000156; GO:0000976; GO:0005829; GO:0006355; GO:0016989; GO:0031648; GO:0032993; GO:0045862; GO:0045892; GO:1903865`

## Notes

Regulator of RpoS
