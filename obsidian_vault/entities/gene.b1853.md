---
entity_id: "gene.b1853"
entity_type: "gene"
name: "yebK"
source_database: "NCBI RefSeq"
source_id: "gene-b1853"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1853"
  - "yebK"
---

# yebK

`gene.b1853`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1853`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yebK (gene.b1853) is a gene entity. It encodes hexR (protein.P46118). Encoded protein function: FUNCTION: Represses the expression of the hex regulon (zwf, eda, glp and gap). {ECO:0000250}. EcoCyc product frame: EG12860-MONOMER. EcoCyc synonyms: hexR(P.a.). Genomic coordinates: 1936652-1937521. EcoCyc protein note: YebK is a transcriptional regulator implicated in the adaptation to the transition from rich medium to cellobiose minimal medium, reducing the length of the lag phase . Expression of YebK is higher in cellobiose minimal medium than in glucose minimal medium. DNA binding of YebK is reversed by 2-keto-3-deoxygluconate-6-phosphate (KDPG) . A transposon insertion mutation in the yebK gene generates cellular susceptibility to the antibiotics trimethoprim and sulfamethoxazole . On the other hand, inhibition of yebK expression by CRISPRi reduced cellular fitness under treatment with the antibiotics carbonyl cyanide 3-chlorophenylhydrazone (CCCP), rifampicin or sulfamethizole . Genome-wide YebK binding sites were determined in vivo by chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium . A transcription factor (TF)-based biosensor, YebK-GFP, sensing the 2-keto-3-deoxy-6-phosphogluconate (KDPG) intermediate of the Entner-Doudoroff pathway (EDP), has been constructed .

## Biological Role

Repressed by hexR (protein.P46118).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46118|protein.P46118]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P46118|protein.P46118]] `RegulonDB` `S` - regulator=YebK; target=yebK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006179,ECOCYC:EG12860,GeneID:946373`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1936652-1937521:+; feature_type=gene
