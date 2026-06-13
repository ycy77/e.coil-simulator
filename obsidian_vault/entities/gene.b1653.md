---
entity_id: "gene.b1653"
entity_type: "gene"
name: "lhr"
source_database: "NCBI RefSeq"
source_id: "gene-b1653"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1653"
  - "lhr"
---

# lhr

`gene.b1653`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1653`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lhr (gene.b1653) is a gene entity. It encodes lhr (protein.P30015). Encoded protein function: FUNCTION: A 3'-5' helicase probably involved in DNA repair. Translocates in an ATP-dependent manner 3'-to-5' on single-stranded (ss)DNA, unwinding any encountered duplex nucleic acid (PubMed:33744958). An RNA:DNA hybrid with a 3'-ssDNA loading strand is a 4.5-fold better helicase substrate than 3'-tailed double-stranded (ds)DNA; substrates where the helicase loads on a 3'-ssRNA tail (DNA:RNA and RNA:RNA) are not unwound (PubMed:33744958). Unlike its M.smegmatis counterpart, the ATPase is not ssDNA-dependent (PubMed:33744958). Forms a clamp around the ssDNA loading strand (By similarity). {ECO:0000250|UniProtKB:A0QT91, ECO:0000269|PubMed:33744958}.; FUNCTION: Excises uracil residues from DNA; forked DNA with a dU residue is the best substrate followed by ssDNA (PubMed:37452011). Inactive on dsDNA with a dU residue or DNA with an 8-oxoguanine residue (PubMed:37452011). Uracil residues in DNA can arise as a result of misincorporation of dUMP residues by DNA polymerase or due to deamination of cytosine. {ECO:0000269|PubMed:37452011}. EcoCyc product frame: EG11548-MONOMER. EcoCyc synonyms: rhlF. Genomic coordinates: 1729087-1733703.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30015|protein.P30015]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=lhr; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005525,ECOCYC:EG11548,GeneID:946156`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1729087-1733703:+; feature_type=gene
