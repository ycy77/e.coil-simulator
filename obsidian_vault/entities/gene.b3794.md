---
entity_id: "gene.b3794"
entity_type: "gene"
name: "rffM"
source_database: "NCBI RefSeq"
source_id: "gene-b3794"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3794"
  - "rffM"
---

# rffM

`gene.b3794`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3794`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rffM (gene.b3794) is a gene entity. It encodes wecG (protein.P27836). Encoded protein function: FUNCTION: Catalyzes the synthesis of Und-PP-GlcNAc-ManNAcA (Lipid II), the second lipid-linked intermediate involved in enterobacterial common antigen (ECA) synthesis. {ECO:0000255|HAMAP-Rule:MF_01001, ECO:0000269|PubMed:1730666}. EcoCyc product frame: UDPMANACATRANS-MONOMER. EcoCyc synonyms: rff, wecG. Genomic coordinates: 3979956-3980696. EcoCyc protein note: UDP-N-acetyl-D-mannosaminuronic acid transferase (RffM) is involved in the biosynthesis of enterobacterial common antigen (ECA) catalyzing the transfer of Fuc4NAc (4-acetamido-4,6-dideoxy-D-galactose) from TDP-Fuc4NAc to ManNAcA-GlcNAc-pyrophosphorylundecaprenol, also known as ECA-lipid II Mutants of rffM are defective in the synthesis of ECA-lipid II . Strains lacking WecG accumulate ECA intermediates, including novel diacylglycerol pyrophosphoryl (DAG-PP)-linked species . The Keio collection rffM mutant exhibits a 'low level' of resistance to lithium exposure .

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27836|protein.P27836]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012394,ECOCYC:EG11458,GeneID:948301`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3979956-3980696:+; feature_type=gene
