---
entity_id: "gene.b2184"
entity_type: "gene"
name: "radD"
source_database: "NCBI RefSeq"
source_id: "gene-b2184"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2184"
  - "radD"
---

# radD

`gene.b2184`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2184`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

radD (gene.b2184) is a gene entity. It encodes radD (protein.P33919). Encoded protein function: FUNCTION: Genetic interactions indicate that RecG or RadD are required for DNA repair in every replication cycle; they function in different pathways, each is essential in the absence of the other (PubMed:32644157). An accessory protein to RecA, it accelerates RecA-dependent DNA-strand exchange; this requires the ATPase activity of RadD (PubMed:35150260). Disassembles RecA filaments preformed on ssDNA (PubMed:35150260). In combination with RadA is important in repair of double-strand DNA breaks (DSB) (PubMed:25425430, PubMed:25484163). Has DNA-independent ATPase activity that is stimulated by single-stranded DNA-binding protein (SSB) (PubMed:27519413, PubMed:36614183). ATPase is stimulated by a peptide with the last 10 residues of SSB (PubMed:27519413, PubMed:36614183), but not when the SSB peptide's last Phe residue is missing (PubMed:27519413). Binds ssDNA; binding is slightly better in the presence of nucleotides (PubMed:27519413). May be involved in resolution of branched DNA intermediates that result from template switching in postreplication gaps. Binds to DNA structures with 3 branches that resemble replication forks (PubMed:31665437, PubMed:36614183)...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33919|protein.P33919]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007228,ECOCYC:EG12045,GeneID:945529`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2280632-2282392:+; feature_type=gene
