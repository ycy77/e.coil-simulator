---
entity_id: "gene.b1866"
entity_type: "gene"
name: "aspS"
source_database: "NCBI RefSeq"
source_id: "gene-b1866"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1866"
  - "aspS"
---

# aspS

`gene.b1866`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1866`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aspS (gene.b1866) is a gene entity. It encodes aspS (protein.P21889). Encoded protein function: FUNCTION: Catalyzes the attachment of L-aspartate to tRNA(Asp) in a two-step reaction: L-aspartate is first activated by ATP to form Asp-AMP and then transferred to the acceptor end of tRNA(Asp). Also mischarges tRNA(Asp) with D-aspartate, although it is a poor substrate (PubMed:10918062). {ECO:0000255|HAMAP-Rule:MF_00044, ECO:0000269|PubMed:10918062}. EcoCyc product frame: ASPS-MONOMER. EcoCyc synonyms: tls. Genomic coordinates: 1948750-1950522. EcoCyc protein note: Aspartate—tRNA ligase (AspRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. AspRS belongs to the Class IIb aminoacyl-tRNA synthetases . The enzyme is a dimer in solution . Crystal structures of AspRS have been determined and allow modelling of specific interactions with the tRNA and the reaction mechanism . AspRS activity appears to be the target of processed CPD0-1129, which is an aspartyl adenylate analog . The tls-1 allele of aspS consists of a P555S mutation in the highly conserved proline residue of motif 3. It has no significant effect on substrate binding, but may affect the active site...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21889|protein.P21889]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006226,ECOCYC:EG10097,GeneID:946385`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1948750-1950522:-; feature_type=gene
