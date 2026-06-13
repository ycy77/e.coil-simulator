---
entity_id: "gene.b0225"
entity_type: "gene"
name: "yafQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0225"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0225"
  - "yafQ"
---

# yafQ

`gene.b0225`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0225`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yafQ (gene.b0225) is a gene entity. It encodes yafQ (protein.Q47149). Encoded protein function: FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system (PubMed:17263853). A sequence-specific mRNA endoribonuclease that inhibits translation elongation and induces bacterial stasis (PubMed:19210620). Cleavage occurs between the second and third residue of the Lys codon followed by a G or A (5'AAA(G/A)3'), is reading-frame dependent and occurs within the 5' end of most mRNAs (PubMed:19210620). Ribosome-binding confers the sequence specificity and reading frame-dependence (PubMed:19210620). When overexpressed in liquid media YafQ partially inhibits protein synthesis, with a reduction in growth rate and colony growth rate. This effect is counteracted by coexpression with cognate antitoxin DinJ (PubMed:17263853). YafQ and DinJ together bind their own promoter, and repress its expression (PubMed:24898247). {ECO:0000269|PubMed:17263853, ECO:0000269|PubMed:19210620, ECO:0000269|PubMed:24898247}.; FUNCTION: Cell death governed by the MazE-MazF and DinJ-YafQ TA systems seems to play a role in biofilm formation (PubMed:19707553). {ECO:0000269|PubMed:19707553}. EcoCyc product frame: G6109-MONOMER. Genomic coordinates: 245961-246239...

## Biological Role

Repressed by nac (protein.Q47005). Activated by ygfI (protein.P52044).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47149|protein.Q47149]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=yafQ; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yafQ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000761,ECOCYC:G6109,GeneID:944911`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:245961-246239:-; feature_type=gene
