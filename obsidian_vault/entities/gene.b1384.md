---
entity_id: "gene.b1384"
entity_type: "gene"
name: "feaR"
source_database: "NCBI RefSeq"
source_id: "gene-b1384"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1384"
  - "feaR"
---

# feaR

`gene.b1384`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1384`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

feaR (gene.b1384) is a gene entity. It encodes feaR (protein.Q47129). Encoded protein function: FUNCTION: Positive regulator of tynA/maoA and feaB/padA, the genes for 2-phenylethylamine catabolism. EcoCyc product frame: G6706-MONOMER. EcoCyc synonyms: ydbM, maoX, maoB. Genomic coordinates: 1446378-1447283. EcoCyc protein note: "Phenylethylamine regulator," FeaR, is considered an activator of phenylacetate synthesis from 2-phenylethylamine (PEA). This regulator is regulated by catabolic repression, and highly expressed in the presence of succinate . FeaR controls expression of a pathway for the degradation of potentially toxic aromatic compounds . It is induced by tyramine, and in the absence of glucose, it activates the expression of amine oxidase and phenylacetaldehyde dehydrogenase, proteins involved in 2-phenylethylamine catabolism . Although it has not been possible to test the ligand binding to FeaR, these data and those of others suggest that it is a substrate or intermediate of the TynA/FeaB pathway, as it is more likely that an aldehyde (tyramine) is the direct inducer for the PEA catabolic pathway and a likely coeffector of FeaR . FeaR belongs to the AraC/XylS family of transcriptional regulators...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), phoB (protein.P0AFJ5), nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47129|protein.Q47129]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=feaR; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB|EcoCyc` `S` - regulator=PhoB; target=feaR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004630,ECOCYC:G6706,GeneID:945941`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1446378-1447283:-; feature_type=gene
