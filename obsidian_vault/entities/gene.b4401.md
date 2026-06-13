---
entity_id: "gene.b4401"
entity_type: "gene"
name: "arcA"
source_database: "NCBI RefSeq"
source_id: "gene-b4401"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4401"
  - "arcA"
---

# arcA

`gene.b4401`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4401`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

arcA (gene.b4401) is a gene entity. It encodes arcA (protein.P0A9Q1). Encoded protein function: FUNCTION: Member of the two-component regulatory system ArcB/ArcA. Represses a wide variety of aerobic enzymes under anaerobic conditions. Controls the resistance of E.coli to dyes; required for expression of the alkaline phosphatase and sex factor F genes; it may also be involved in the osmoregulation of envelope proteins. When activated by ArcB, it negatively regulates the expression of genes of aerobic function. Activates the transcription of the plfB operon by binding to its promoter. EcoCyc product frame: PHOSPHO-ARCA. EcoCyc synonyms: sfrA, cpxC, dye, fexA, msp, seg. Genomic coordinates: 4639590-4640306. EcoCyc protein note: ArcA is a dual transcriptional regulator for Anoxic redox control . It acts primarily as a negative transcriptional regulator under anaerobic conditions. ArcA represses operons involved in respiratory metabolism, including those that encode products such as the tricarboxylic acid cycle enzymes, enzymes of the glyoxylate shunt, and enzymes of the pathway for fatty acid degradation . In addition, ArcA acts as a repressor for rpoS transcription . ArcA also activates a few operons encoding proteins involved in fermentative metabolism . It has been identified as global repressor of carbon oxidation pathways...

## Biological Role

Repressed by fnr (protein.P0A9E5). Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), fnr (protein.P0A9E5), arcA (protein.P0A9Q1).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9Q1|protein.P0A9Q1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=arcA; function=-+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=arcA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=arcA; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0014434,ECOCYC:EG10061,GeneID:948874`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4639590-4640306:-; feature_type=gene
