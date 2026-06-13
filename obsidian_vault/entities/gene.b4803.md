---
entity_id: "gene.b4803"
entity_type: "gene"
name: "speFL"
source_database: "NCBI RefSeq"
source_id: "gene-b4803"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4803"
  - "speFL"
---

# speFL

`gene.b4803`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4803`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

speFL (gene.b4803) is a gene entity. It encodes speFL (protein.P0DTV7). Encoded protein function: FUNCTION: A small protein (arrest peptide) encoded upstream of inducible ornithine carboxylase gene (speF) that controls expression of downstream genes (speF and patE) by nascent chain-translational arrest and transcriptional attenuation. In the presence of ornithine a toeprint due to ribosomal arrest can be seen on the speFL transcript. Only L-ornithine (not other tested amino acids) has this effect (PubMed:32094585). It is thought that in the presence of ornithine, ribosomal stalling on speFL prevents binding of Rho transcription termination factor to a downstream rut site allowing transcription of the operon. In the absence of ornithine, ribosomes terminate translation and are recycled, exposing the rut site allowing Rho to bind and prematurely terminate transcription. The presence of a pair of rare Arg codons could slow down translation to prevent polysome accumulation and to expose the rut site to Rho (Probable). {ECO:0000255|HAMAP-Rule:MF_00851, ECO:0000269|PubMed:32094585, ECO:0000305|PubMed:32094585}. EcoCyc product frame: MONOMER0-4532. Genomic coordinates: 720718-720822. EcoCyc protein note: The SpeFL leader peptide enables regulation of translation of the ORNDECARBOXDEG-MONOMER (SpeF) by transcriptional attenuation...

## Biological Role

Repressed by ompR (protein.P0AA16).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DTV7|protein.P0DTV7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=speFL; function=-

## External IDs

- `Dbxref:ASAP:ABE-0285828,ECOCYC:G0-17074,GeneID:63925627`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:720718-720822:-; feature_type=gene
