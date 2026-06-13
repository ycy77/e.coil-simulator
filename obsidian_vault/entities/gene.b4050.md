---
entity_id: "gene.b4050"
entity_type: "gene"
name: "pspG"
source_database: "NCBI RefSeq"
source_id: "gene-b4050"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4050"
  - "pspG"
---

# pspG

`gene.b4050`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4050`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pspG (gene.b4050) is a gene entity. It encodes pspG (protein.P32696). Encoded protein function: FUNCTION: Effector of the phage shock response. {ECO:0000269|PubMed:15485810}. EcoCyc product frame: EG11933-MONOMER. EcoCyc synonyms: yjbO. Genomic coordinates: 4262840-4263082. EcoCyc protein note: The PspG protein is predicted to be an inner membrane protein. PspG is conserved in all bacteria that contain the phage shock TU00326 operon. The PspG protein appears to affect motility . Expression of the pspG gene, like that of the TU00326 operon, is upregulated by pIV secretin stress. Transcription by RPON-MONOMER σ54-containing RNA polymerase may be activated by EG12344 PspF, and EG10776-MONOMER PspA negatively regulates pspG expression, making pspG part of the PspF regulon . The EG10230-MONOMER stimulated abortive synthesis of the pspG promoter . PspG self associates and interacts with EG10778-MONOMER PspC in vivo .

## Biological Role

Activated by lrp (protein.P0ACJ0), rpoN (protein.P24255), pspF (protein.P37344).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32696|protein.P32696]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=pspG; function=+
- `activates` <-- [[protein.P37344|protein.P37344]] `RegulonDB` `S` - regulator=PspF; target=pspG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013260,ECOCYC:EG11933,GeneID:948557`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4262840-4263082:+; feature_type=gene
