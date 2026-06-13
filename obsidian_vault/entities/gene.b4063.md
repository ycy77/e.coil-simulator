---
entity_id: "gene.b4063"
entity_type: "gene"
name: "soxR"
source_database: "NCBI RefSeq"
source_id: "gene-b4063"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4063"
  - "soxR"
---

# soxR

`gene.b4063`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4063`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

soxR (gene.b4063) is a gene entity. It encodes soxR (protein.P0ACS2). Encoded protein function: FUNCTION: Activates the transcription of the soxS gene which itself controls the superoxide response regulon. SoxR contains a 2Fe-2S iron-sulfur cluster that may act as a redox sensor system that recognizes superoxide. The variable redox state of the Fe-S cluster is employed in vivo to modulate the transcriptional activity of SoxR in response to specific types of oxidative stress. Upon reduction of 2Fe-2S cluster, SoxR reversibly loses its transcriptional activity, but retains its DNA binding affinity. EcoCyc product frame: PD04132. EcoCyc synonyms: marC. Genomic coordinates: 4277469-4277933. EcoCyc protein note: The SoxR protein, for "Superoxide Response protein", is negatively autoregulated and controls the transcription of the regulon involved in defense against redox-cycling drugs and in responses to nitric oxide . SoxR also appears to be involved in resistance to ciprofloxacin , cefuroxime, gentamicin , pyocyanin and other antimicrobials . In a gene expression study during the transition from aerobic to anaerobic conditions, part of the regulatory cascade involving the protein SoxR was analyzed . SoxR belongs to the MerR family and is a homodimer in solution . This protein contains two essential [2Fe-2S] clusters for its transcriptional activity...

## Biological Role

Repressed by soxR (protein.P0ACS2), acrR (protein.P0ACS9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACS2|protein.P0ACS2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACS2|protein.P0ACS2]] `RegulonDB` `C` - regulator=SoxR; target=soxR; function=-
- `represses` <-- [[protein.P0ACS9|protein.P0ACS9]] `RegulonDB` `S` - regulator=AcrR; target=soxR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013316,ECOCYC:EG10957,GeneID:948566`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4277469-4277933:+; feature_type=gene
