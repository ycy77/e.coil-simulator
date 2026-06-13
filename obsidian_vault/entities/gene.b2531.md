---
entity_id: "gene.b2531"
entity_type: "gene"
name: "iscR"
source_database: "NCBI RefSeq"
source_id: "gene-b2531"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2531"
  - "iscR"
---

# iscR

`gene.b2531`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2531`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

iscR (gene.b2531) is a gene entity. It encodes iscR (protein.P0AGK8). Encoded protein function: FUNCTION: Regulates the transcription of several operons and genes involved in the biogenesis of Fe-S clusters and Fe-S-containing proteins. Transcriptional repressor of the iscRSUA operon, which is involved in the assembly of Fe-S clusters into Fe-S proteins. In its apoform, under conditions of oxidative stress or iron deprivation, it activates the suf operon, which is a second operon involved in the assembly of Fe-S clusters. Represses its own transcription as well as that of toxin rnlA. {ECO:0000269|PubMed:11742080, ECO:0000269|PubMed:16824106, ECO:0000269|PubMed:20421606}. EcoCyc product frame: G7326-MONOMER. EcoCyc synonyms: yfhP. Genomic coordinates: 2661643-2662131. EcoCyc protein note: The transcription factor IscR, for "Iron-sulfur cluster Regulator," is negatively autoregulated, and it contains an iron-sulfur cluster that could act as a sensor of iron-sulfur cluster assembly . This protein regulates the expression of the operons that encode components of a secondary pathway of iron-sulfur cluster assembly, iron-sulfur proteins, anaerobic respiration enzymes, and biofilm formation . In addition, IscR contributes to the cellular response to stress caused by the superoxide-producing redox-cycling agent phenazine methosulfate (PMS)...

## Biological Role

Repressed by ryhB (gene.b4451), fnrS (gene.b4699), iscR (protein.P0AGK8). Activated by oxyS (gene.b4458), rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGK8|protein.P0AGK8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[gene.b4458|gene.b4458]] `RegulonDB` `S` - regulator=OxyS; target=iscR; function=+
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=iscR; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=iscR; function=-
- `represses` <-- [[gene.b4699|gene.b4699]] `RegulonDB` `S` - regulator=FnrS; target=iscR; function=-
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `C` - regulator=IscR; target=iscR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008326,ECOCYC:G7326,GeneID:945279`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2661643-2662131:-; feature_type=gene
