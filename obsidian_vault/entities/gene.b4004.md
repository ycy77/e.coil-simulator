---
entity_id: "gene.b4004"
entity_type: "gene"
name: "zraR"
source_database: "NCBI RefSeq"
source_id: "gene-b4004"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4004"
  - "zraR"
---

# zraR

`gene.b4004`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4004`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

zraR (gene.b4004) is a gene entity. It encodes zraR (protein.P14375). Encoded protein function: FUNCTION: Part of the Zra signaling pathway, an envelope stress response (ESR) system composed of the periplasmic accessory protein ZraP, the histidine kinase ZraS and the transcriptional regulator ZraR (PubMed:26438879, PubMed:30389436). The ZraPSR system contributes to antibiotic resistance and is important for membrane integrity in the presence of membrane-targeting biocides (PubMed:30389436). ZraR is a member of the two-component regulatory system ZraS/ZraR (PubMed:11243806). When activated by ZraS, acts in conjunction with sigma-54 to regulate the expression of zraP in the presence of high Zn(2+) or Pb(2+) concentrations (PubMed:11243806). Also positively autoregulates the expression of the zraSR operon (PubMed:11243806). Binds to a region within the zraP-zraSR intergenic region that is characterized by two inverted repeats separated by a 14 bp spacer (PubMed:11243806). In addition, controls a regulon of genes of diverse functions that may be critical to maintain envelope integrity and cell survival under stressful conditions (PubMed:30389436). The system has no direct role in zinc or copper resistance (PubMed:26438879). {ECO:0000269|PubMed:11243806, ECO:0000269|PubMed:26438879, ECO:0000269|PubMed:30389436}. EcoCyc product frame: PHOSPHO-HYDG. EcoCyc synonyms: hydG...

## Biological Role

Repressed by glaR (protein.P37338). Activated by zraR (protein.P14375).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P14375|protein.P14375]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB` `S` - regulator=ZraR; target=zraR; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=zraR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013093,ECOCYC:EG10482,GeneID:948505`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4203320-4204645:+; feature_type=gene
