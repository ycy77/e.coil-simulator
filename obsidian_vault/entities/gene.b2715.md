---
entity_id: "gene.b2715"
entity_type: "gene"
name: "ascF"
source_database: "NCBI RefSeq"
source_id: "gene-b2715"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2715"
  - "ascF"
---

# ascF

`gene.b2715`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2715`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ascF (gene.b2715) is a gene entity. It encodes ascF (protein.P24241). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in arbutin, cellobiose, and salicin transport. EcoCyc product frame: ASCF-MONOMER. EcoCyc synonyms: sac. Genomic coordinates: 2839524-2840981.

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), spf (gene.b3864), hns (protein.P0ACF8), ascG (protein.P24242). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24241|protein.P24241]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ascF; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ascF; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b3864|gene.b3864]] `RegulonDB` `S` - regulator=Spf; target=ascF; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P24242|protein.P24242]] `RegulonDB` `C` - regulator=AscG; target=ascF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008926,ECOCYC:EG10086,GeneID:947154`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2839524-2840981:+; feature_type=gene
