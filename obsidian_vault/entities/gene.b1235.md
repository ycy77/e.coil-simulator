---
entity_id: "gene.b1235"
entity_type: "gene"
name: "rssB"
source_database: "NCBI RefSeq"
source_id: "gene-b1235"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1235"
  - "rssB"
---

# rssB

`gene.b1235`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1235`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rssB (gene.b1235) is a gene entity. It encodes rssB (protein.P0AEV1). Encoded protein function: FUNCTION: Regulates the turnover of the sigma S factor (RpoS) by promoting its proteolysis in exponentially growing cells. Acts by binding and delivering RpoS to the ClpXP protease. RssB is not co-degraded with RpoS, but is released from the complex and can initiate a new cycle of RpoS recognition and degradation. In stationary phase, could also act as an anti-sigma factor and reduce the ability of RpoS to activate gene expression. Is also involved in the regulation of the mRNA polyadenylation pathway during stationary phase, probably by maintaining the association of PcnB with the degradosome. {ECO:0000255|HAMAP-Rule:MF_00958, ECO:0000269|PubMed:10672187, ECO:0000269|PubMed:11442836, ECO:0000269|PubMed:19767441, ECO:0000269|PubMed:20472786, ECO:0000269|PubMed:8635466, ECO:0000269|PubMed:8637901}. EcoCyc product frame: RSSB-P. EcoCyc synonyms: ychL, sprE, hnr. Genomic coordinates: 1290242-1291255. EcoCyc protein note: RssB is an adaptor protein that facilitates degradation of the alternative sigma factor RPOS-MONOMER σS by the protease ClpXP . RssB is specific to σS and has no effect on the stability of other ClpXP substrates . In the absence of ClpXP and upon overexpression of RssB, a direct anti-sigma factor effect of RssB on σS activity can also be observed...

## Biological Role

Repressed by glaR (protein.P37338). Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEV1|protein.P0AEV1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=rssB; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=rssB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004147,ECOCYC:EG12121,GeneID:945855`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1290242-1291255:+; feature_type=gene
