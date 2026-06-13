---
entity_id: "gene.b0001"
entity_type: "gene"
name: "thrL"
source_database: "NCBI RefSeq"
source_id: "gene-b0001"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0001"
  - "thrL"
---

# thrL

`gene.b0001`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0001`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thrL (gene.b0001) is a gene entity. It encodes thrL (protein.P0AD86). Encoded protein function: FUNCTION: This protein is involved in control of the biosynthesis of threonine. EcoCyc product frame: EG11277-MONOMER. Genomic coordinates: 190-255. EcoCyc protein note: The ThrL leader peptide controls by attenuation the expression of the thrLABC operon, which encodes four out of the five enzymes of threonine biosynthesis pathway, in response to the threonine and isoleucine levels . ThrL is a 21 amino acid long peptide, with eight threonine and four isoleucine residues as regulatory points during attenuation .

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD86|protein.P0AD86]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=thrL; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=thrL; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000006,ECOCYC:EG11277,GeneID:944742`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:190-255:+; feature_type=gene
