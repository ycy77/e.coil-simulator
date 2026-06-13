---
entity_id: "gene.b3556"
entity_type: "gene"
name: "cspA"
source_database: "NCBI RefSeq"
source_id: "gene-b3556"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3556"
  - "cspA"
---

# cspA

`gene.b3556`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3556`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cspA (gene.b3556) is a gene entity. It encodes cspA (protein.P0A9X9). Encoded protein function: FUNCTION: Binds to and stimulates the transcription of the CCAAT-containing, cold-shock-inducible promoters of the H-NS and GyrA proteins. Also binds to the inverted repeat 5'-ATTGG-3'. {ECO:0000269|PubMed:1961761}. EcoCyc product frame: PD03695. Genomic coordinates: 3720049-3720261. EcoCyc protein note: The "Cold shock protein A," CspA, is a major cold shock protein and was shown to be detected only during early-log-phase growth at 37°C and during log phase after a shift from 37°C to 10°C . However, studies have shown that although the expression of cspA is reduced during stationary phase, cspA mRNA and CspA are detectable during all growth phases . CspA acts as a positive transcription factor of at least two cold shock genes: hns and gyrA . cspA has been shown to negatively regulate its own expression as the result of attenuation of transcription . A model of how CspA might affect the transcription of hns has been proposed . CspE inhibits the expression of cspA in vitro by increasing pause recognition for RNA polymerase at the cspA "cold box" . cspA expression was increased in a uvrY mutant strain and reduced when uvrY was overexpressed . CspA belongs to the cold shock family of proteins and was shown to be homologous to eukaryotic Y-box transcription factors...

## Biological Role

Repressed by hns (protein.P0ACF8), zraR (protein.P14375). Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), rpoD (protein.P00579), ydiP (protein.P77402).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9X9|protein.P0A9X9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cspA; function=+
- `activates` <-- [[protein.P77402|protein.P77402]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=cspA; function=-
- `represses` <-- [[protein.P14375|protein.P14375]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011616,ECOCYC:EG10166,GeneID:948070`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3720049-3720261:+; feature_type=gene
