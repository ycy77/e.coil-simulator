---
entity_id: "gene.b1213"
entity_type: "gene"
name: "ychQ"
source_database: "NCBI RefSeq"
source_id: "gene-b1213"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1213"
  - "ychQ"
---

# ychQ

`gene.b1213`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1213`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ychQ (gene.b1213) is a gene entity. It encodes ychQ (protein.Q46755). Encoded protein function: Protein YchQ (Protein SirB2) EcoCyc product frame: G6630-MONOMER. EcoCyc synonyms: sirB2. Genomic coordinates: 1266924-1267316. EcoCyc protein note: YchQ is an inner membrane protein with four predicted transmembrane domains. The C terminus is located in the periplasm .

## Biological Role

Activated by rpoD (protein.P00579), glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46755|protein.Q46755]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ychQ; function=+
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ychQ; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004071,ECOCYC:G6630,GeneID:945781`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1266924-1267316:+; feature_type=gene
