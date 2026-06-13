---
entity_id: "gene.b4725"
entity_type: "gene"
name: "rseD"
source_database: "NCBI RefSeq"
source_id: "gene-b4725"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4725"
  - "rseD"
---

# rseD

`gene.b4725`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4725`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rseD (gene.b4725) is a gene entity. It encodes rseD (protein.P0DPC7). Encoded protein function: FUNCTION: A short protein whose stop codon overlaps with the start codon of downstream rpoE; a premature stop codon at position 12 results in decreased expression of ECF sigma factor RpoE, thus they are translationally coupled (PubMed:28924029). {ECO:0000269|PubMed:28924029}. EcoCyc product frame: MONOMER0-4396. Genomic coordinates: 2710009-2710164. EcoCyc protein note: Translation of rpoE, which encodes the extracytoplasmic stress response sigma factor σE, is coupled to the translation of the rpoE leader peptide, RseD. If translational coupling is eliminated, translation of rpoE is reduced by more than 50% .

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), glnG (protein.P0AFB8), glrR (protein.P0AFU4), rcsB (protein.P0DMC7), rpoS (protein.P13445), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DPC7|protein.P0DPC7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rseD; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rseD; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=rseD; function=+
- `activates` <-- [[protein.P0AFU4|protein.P0AFU4]] `RegulonDB` `S` - regulator=GlrR; target=rseD; function=+
- `activates` <-- [[protein.P0DMC7|protein.P0DMC7]] `RegulonDB` `C` - regulator=RcsB; target=rseD; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=rseD; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=rseD; function=+

## External IDs

- `Dbxref:ECOCYC:G0-16690,GeneID:38094969`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2710009-2710164:-; feature_type=gene
