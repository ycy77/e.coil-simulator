---
entity_id: "gene.b2151"
entity_type: "gene"
name: "galS"
source_database: "NCBI RefSeq"
source_id: "gene-b2151"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2151"
  - "galS"
---

# galS

`gene.b2151`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2151`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

galS (gene.b2151) is a gene entity. It encodes galS (protein.P25748). Encoded protein function: FUNCTION: Repressor of the mgl operon. Binds galactose and D-fucose as inducers. GalS binds to an operator DNA sequence within its own coding sequence (corresponding to residues 15 to 20). EcoCyc product frame: PD00261. EcoCyc synonyms: mglD. Genomic coordinates: 2240628-2241668. EcoCyc protein note: The "Galactose isorepressor," GalS, is a DNA-binding transcription factor that represses transcription of the operons involved in transport and catabolism of D-galactose . Synthesis of these operons is induced when E. coli is grown in the presence of the inducer (D-galactose) and the absence glucose . GalS is negatively autoregulated, and its expression is increased in the presence of inducer and glucose . On the other hand, GalS is highly homologous in its amino acid sequence to GalR (55% identical and 88% similar); apparently both act together and are capable of cross-talking to regulate expression of the gal regulon . For this reason these regulators bind the same operators, in the cis regulatory regions, with different affinities. Also, it has been suggested that the DNA-binding consensus sequences that recognize GalR and GalS are not the same . In the presence of an inductor, GalS undergoes a conformational change that reduces its affinity for the operator. Golding et al...

## Biological Role

Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25748|protein.P25748]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=galS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007110,ECOCYC:EG10365,GeneID:949043`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2240628-2241668:-; feature_type=gene
