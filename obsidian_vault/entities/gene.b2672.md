---
entity_id: "gene.b2672"
entity_type: "gene"
name: "ygaM"
source_database: "NCBI RefSeq"
source_id: "gene-b2672"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2672"
  - "ygaM"
---

# ygaM

`gene.b2672`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2672`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygaM (gene.b2672) is a gene entity. It encodes ygaM (protein.P0ADQ7). Encoded protein function: Uncharacterized protein YgaM EcoCyc product frame: B0899-MONOMER. Genomic coordinates: 2800146-2800475. EcoCyc protein note: YgaM, G7612 YqjD, and G7173 ElaB are paralogs . YgaM, ElaB, and YqjD are ribosome-associated factors implicated in stress-associated translation modulation (see ). Overexpressed YgaM is present in the ribosome fraction . ygaM is upregulated by sodium salicylate, which is also known to cause the induction of the marRAB regulon resulting in resistance to oxidative agents and antibiotics . ygaM is induced at the transition to stationary phase, upon NaCl shock, and upon acid shock in an rpoS+ strain compared to a rpoS mutant, and is therefore believed to be controlled by the general stress response master regulator, σS . CsrA indirectly regulates the growth-phase specific expression of ygaM . ygaM clusters with osmoprotectant genes having supercoiling-dependent transcription . ygaM is among the 25 genes most susceptible to phage μ insertion at mid-log phase growth, which was shown to prefer regions of low transcription . YgaM is predicted to be a bitopic inner membrane protein . YgaM belongs to the heterogeneous group of C-tail-anchored membrane proteins .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADQ7|protein.P0ADQ7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ygaM; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008799,ECOCYC:G7400,GeneID:947157`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2800146-2800475:+; feature_type=gene
