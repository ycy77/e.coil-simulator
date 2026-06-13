---
entity_id: "gene.b4057"
entity_type: "gene"
name: "yjbR"
source_database: "NCBI RefSeq"
source_id: "gene-b4057"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4057"
  - "yjbR"
---

# yjbR

`gene.b4057`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4057`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjbR (gene.b4057) is a gene entity. It encodes yjbR (protein.P0AF50). Encoded protein function: Uncharacterized protein YjbR EcoCyc product frame: EG11936-MONOMER. Genomic coordinates: 4270658-4271014. EcoCyc protein note: A solution structure of YjbR has been determined, and structural similarity to the "double wing" DNA binding motif was found . Expression of yjbR is upregulated in a strain containing the ompR234 allele (an ompR up-mutation) .

## Biological Role

Activated by lrp (protein.P0ACJ0), gadE (protein.P63204).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF50|protein.P0AF50]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `S` - regulator=GadE; target=yjbR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013288,ECOCYC:EG11936,GeneID:948560`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4270658-4271014:+; feature_type=gene
