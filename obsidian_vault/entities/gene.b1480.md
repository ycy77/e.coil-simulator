---
entity_id: "gene.b1480"
entity_type: "gene"
name: "sra"
source_database: "NCBI RefSeq"
source_id: "gene-b1480"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1480"
  - "sra"
---

# sra

`gene.b1480`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1480`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sra (gene.b1480) is a gene entity. It encodes sra (protein.P68191). Encoded protein function: FUNCTION: Although this protein associates with the 30S subunit of the ribosome it is not considered to be a bona fide ribosomal protein. {ECO:0000269|PubMed:11292794, ECO:0000269|PubMed:17277072}. EcoCyc product frame: EG11508-MONOMER. EcoCyc synonyms: rpsV. Genomic coordinates: 1555826-1555963. EcoCyc protein note: Sra is a 30S ribosomal subunit-associated protein that is more abundant at stationary phase than during log phase growth . Transcription is induced and protein abundance increases under stationary phase conditions. σS, cAMP, ppGpp, Fis, and IHF may be involved in the transcription of sra during stationary phase . sra is also cotranscribed with the bdm gene from a promoter upstream of bdm which is activated by osmotic shock and dependent on the RcsCDB phosphorelay system . Sra protein production is increased during HipA-induced persistence . An sra deletion mutant does not have an obvious growth defect . showed that a Δsra mutant had an increased doubling time and decreased cell size. A Δsra mutant shows increased growth inhibition and lower antibiotic tolerance upon ectopic expression of HipA compared to wild type . Sra: "stationary-phase-induced ribosome-associated" Review:

## Biological Role

Activated by rcsB (protein.P0DMC7), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P68191|protein.P68191]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0DMC7|protein.P0DMC7]] `RegulonDB` `S` - regulator=RcsB; target=sra; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=sra; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004935,ECOCYC:EG11508,GeneID:946030`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1555826-1555963:-; feature_type=gene
