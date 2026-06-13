---
entity_id: "gene.b0069"
entity_type: "gene"
name: "sgrR"
source_database: "NCBI RefSeq"
source_id: "gene-b0069"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0069"
  - "sgrR"
---

# sgrR

`gene.b0069`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0069`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sgrR (gene.b0069) is a gene entity. It encodes sgrR (protein.P33595). Encoded protein function: FUNCTION: Activates the small RNA gene sgrS under glucose-phosphate stress conditions as well as yfdZ. Represses its own transcription under both stress and non-stress conditions; this repression likely provides one measure of control over sgrR at the level of synthesis. Might act as a sensor of the intracellular accumulation of phosphoglucose by binding these molecules in its C-terminal solute-binding domain. {ECO:0000269|PubMed:15522088, ECO:0000269|PubMed:17209026}. EcoCyc product frame: EG12094-MONOMER. EcoCyc synonyms: yabN. Genomic coordinates: 75644-77299. EcoCyc protein note: "SugaR transport-related Regulator" SgrR is negatively autoregulated and coordinately activates transcription of the divergent operon. This regulator coordinates the response to glucose-phosphate stress . As the intracellular accumulation of glucose-6-phosphate correlates with SgrR induction, it has been proposed as its inducer . Autoregulation of SgrR is not affected by phosphosugar stress . In addition, the induction of sgrS expression by the nonmetabolizable glucose PTS substrate (+/-)-methyl glucoside is abolished in a sgrR mutant...

## Biological Role

Repressed by sgrR (protein.P33595).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33595|protein.P33595]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P33595|protein.P33595]] `RegulonDB` `C` - regulator=SgrR; target=sgrR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000251,ECOCYC:EG12094,GeneID:944788`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:75644-77299:-; feature_type=gene
