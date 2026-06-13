---
entity_id: "gene.b3709"
entity_type: "gene"
name: "tnaB"
source_database: "NCBI RefSeq"
source_id: "gene-b3709"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3709"
  - "tnaB"
---

# tnaB

`gene.b3709`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3709`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tnaB (gene.b3709) is a gene entity. It encodes tnaB (protein.P23173). Encoded protein function: FUNCTION: Involved in tryptophan transport across the cytoplasmic membrane. Plays a role in transporting tryptophan which is to be used catabolically. EcoCyc product frame: TNAB-MONOMER. EcoCyc synonyms: tnaP, trpP. Genomic coordinates: 3890236-3891483. EcoCyc protein note: TnaB is one of three known transporters for tryptophan in E. coli, the others being MTR-MONOMER Mtr and EG10084 AroP. The tnaB gene is located in an operon with the EG11005 gene, encoding tryptophanase . Transcription of the tnaAB operon is regulated by tryptophan-induced transcriptional antitermination and is subject to catabolite repression . Whole cell transport experiments have indicated that TnaB is a low affinity tryptophan transporter (Km of about 70 μM) . TnaB is a member of the ArAAAP family of amino acid transporters and is homologous to the MTR-MONOMER Mtr and EG11041 TyrP transporters . Examination of EG10617, EG10084 and EG11006 mutants under various growth conditions has shown that TnaB is essential for growth on tryptophan as the sole carbon source and its primary role is probably uptake of tryptophan for catabolic purposes. Imported tryptophan can be utilized as a carbon and nitrogen source following its degradation to indole, pyruvate and ammonia by TRYPTOPHAN-MONOMER.

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), torR (protein.P38684).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23173|protein.P23173]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=tnaB; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=tnaB; function=+
- `activates` <-- [[protein.P38684|protein.P38684]] `RegulonDB` `S` - regulator=TorR; target=tnaB; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=tnaB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012135,ECOCYC:EG11006,GeneID:948220`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3890236-3891483:+; feature_type=gene
