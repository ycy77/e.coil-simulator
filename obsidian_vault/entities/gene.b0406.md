---
entity_id: "gene.b0406"
entity_type: "gene"
name: "tgt"
source_database: "NCBI RefSeq"
source_id: "gene-b0406"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0406"
  - "tgt"
---

# tgt

`gene.b0406`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0406`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tgt (gene.b0406) is a gene entity. It encodes tgt (protein.P0A847). Encoded protein function: FUNCTION: Catalyzes the base-exchange of a guanine (G) residue with the queuine precursor 7-aminomethyl-7-deazaguanine (PreQ1) at position 34 (anticodon wobble position) in tRNAs with GU(N) anticodons (tRNA-Asp, -Asn, -His and -Tyr). Catalysis occurs through a double-displacement mechanism. The nucleophile active site attacks the C1' of nucleotide 34 to detach the guanine base from the RNA, forming a covalent enzyme-RNA intermediate. The proton acceptor active site deprotonates the incoming PreQ1, allowing a nucleophilic attack on the C1' of the ribose to form the product. After dissociation, two additional enzymatic reactions on the tRNA convert PreQ1 to queuine (Q), resulting in the hypermodified nucleoside queuosine (7-(((4,5-cis-dihydroxy-2-cyclopenten-1-yl)amino)methyl)-7-deazaguanosine). {ECO:0000255|HAMAP-Rule:MF_00168, ECO:0000269|PubMed:11714265, ECO:0000269|PubMed:12909636}. EcoCyc product frame: EG10996-MONOMER. EcoCyc synonyms: vacC(S.f.). Genomic coordinates: 426137-427264.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A847|protein.P0A847]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001413,ECOCYC:EG10996,GeneID:949130`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:426137-427264:+; feature_type=gene
