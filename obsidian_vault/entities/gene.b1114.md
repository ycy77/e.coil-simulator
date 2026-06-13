---
entity_id: "gene.b1114"
entity_type: "gene"
name: "mfd"
source_database: "NCBI RefSeq"
source_id: "gene-b1114"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1114"
  - "mfd"
---

# mfd

`gene.b1114`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1114`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mfd (gene.b1114) is a gene entity. It encodes mfd (protein.P30958). Encoded protein function: FUNCTION: Couples transcription and DNA repair by recognizing RNA polymerase (RNAP) stalled at DNA lesions. Mediates ATP-dependent release of RNAP and its truncated transcript from the DNA, and recruitment of nucleotide excision repair machinery to the damaged site. Can also dissociate RNAP that is blocked by low concentration of nucleoside triphosphates or by physical obstruction, such as bound proteins. In addition, can rescue arrested complexes by promoting forward translocation. Has ATPase activity, which is required for removal of stalled RNAP, but seems to lack helicase activity. May act through a translocase activity that rewinds upstream DNA, leading either to translocation or to release of RNAP when the enzyme active site cannot continue elongation. {ECO:0000255|HAMAP-Rule:MF_00969, ECO:0000269|PubMed:12086674, ECO:0000269|PubMed:19700770, ECO:0000269|PubMed:7876261, ECO:0000269|PubMed:7876262, ECO:0000269|PubMed:8465200}. EcoCyc product frame: EG11619-MONOMER. Genomic coordinates: 1170518-1173964...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03420` Nucleotide excision repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30958|protein.P30958]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mfd; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003763,ECOCYC:EG11619,GeneID:945681`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1170518-1173964:-; feature_type=gene
