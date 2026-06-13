---
entity_id: "gene.b3601"
entity_type: "gene"
name: "mtlR"
source_database: "NCBI RefSeq"
source_id: "gene-b3601"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3601"
  - "mtlR"
---

# mtlR

`gene.b3601`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3601`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mtlR (gene.b3601) is a gene entity. It encodes mtlR (protein.P0AF10). Encoded protein function: FUNCTION: Involved in the repression of the expression of the mannitol mtlADR operon (PubMed:8300537). Does not bind the operator/promoter regulatory region of this operon (PubMed:19840941). Therefore, seems to belong to a new class of transcription factors in bacteria that may regulate gene expression indirectly, perhaps as a part of a larger transcriptional complex. {ECO:0000269|PubMed:19840941, ECO:0000269|PubMed:8300537}. EcoCyc product frame: PD00369. Genomic coordinates: 3775572-3776159. EcoCyc protein note: In 1994, MtlR, for "Mannitol Regulator," was described as a transcriptional regulator of the mtlADR operon, and potential TF-binding sites were proposed to be recognized for the regulator . However, in 2009 Tan et al. demonstrated that MtlR is unable to bind to the mtlADR operon regulatory region, and they furthermore demonstrated that MtlR does not possess a DNA-binding motif. Because a regulatory effect of MtlR has been demonstrated (mutants have an effect on mtlADR expression), it is proposed that this regulation is indirect, through the involvement of some other DNA-binding regulator, in E. coli. It is noteworthy that in other organisms, MtlR contains a DNA-binding motif; in addition, it has been shown to function as a DNA-binding regulator of transcription...

## Biological Role

Repressed by fis (protein.P0A6R3). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF10|protein.P0AF10]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=mtlR; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=mtlR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011769,ECOCYC:EG11965,GeneID:948116`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3775572-3776159:+; feature_type=gene
