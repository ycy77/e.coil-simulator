---
entity_id: "gene.b2619"
entity_type: "gene"
name: "ratA"
source_database: "NCBI RefSeq"
source_id: "gene-b2619"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2619"
  - "ratA"
---

# ratA

`gene.b2619`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2619`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ratA (gene.b2619) is a gene entity. It encodes ratA (protein.P0AGL5). Encoded protein function: FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. Binds to 50S ribosomal subunits, preventing them from associating with 30S subunits to form 70S ribosomes and reducing polysomes. It does not cause ribosomes to dissociate however. The antibiotic paromomycin blocks the anti-association activity of RatA. Overexpression results in inhibition of growth in liquid cultures, and in a decrease in protein translation. The other gene of this operon, ratB, is not the cognate antitoxin in this strain; in CFT073 however it does fulfill this function.; FUNCTION: Low level expression in a deletion mutant increases resistance to acidified sodium nitrate which causes nitrosative stress. EcoCyc product frame: G7358-MONOMER. EcoCyc synonyms: yfjG. Genomic coordinates: 2754288-2754764. EcoCyc protein note: RatA is a toxic protein that inhibits initiation of translation by specifically associating with the free 50S subunit of the ribosome and inhibiting 70S ribosome formation. RatA is unable to dissociate 70S ribosomes and has no effect on cellular mRNAs . Inducing expression of RatA causes inhibition of cell growth . Deletion of the orthologous pasTI locus alone in the uropathogenic E...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGL5|protein.P0AGL5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008618,ECOCYC:G7358,GeneID:945614`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2754288-2754764:-; feature_type=gene
