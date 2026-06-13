---
entity_id: "gene.b3766"
entity_type: "gene"
name: "ilvL"
source_database: "NCBI RefSeq"
source_id: "gene-b3766"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3766"
  - "ilvL"
---

# ilvL

`gene.b3766`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3766`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ilvL (gene.b3766) is a gene entity. It encodes ilvL (protein.P62522). Encoded protein function: ilv operon leader peptide (ilvGMEDA operon attenuator peptide) EcoCyc product frame: EG11270-MONOMER. Genomic coordinates: 3950322-3950420. EcoCyc protein note: The IlvL leader peptide controls by attenuation the transcription of the ilvLXGMEDA operon, which codes for four of the five enzymes necessary for the isoleucine and valine biosynthesis . It is a 32 amino acid long peptide with multiple isoleucine, valine and leucine residues that serve as its regulatory points during attenuation .

## Biological Role

Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P62522|protein.P62522]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ilvL; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ilvL; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012307,ECOCYC:EG11270,GeneID:948283`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3950322-3950420:+; feature_type=gene
