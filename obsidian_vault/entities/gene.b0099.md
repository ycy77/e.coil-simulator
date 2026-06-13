---
entity_id: "gene.b0099"
entity_type: "gene"
name: "mutT"
source_database: "NCBI RefSeq"
source_id: "gene-b0099"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0099"
  - "mutT"
---

# mutT

`gene.b0099`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0099`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mutT (gene.b0099) is a gene entity. It encodes mutT (protein.P08337). Encoded protein function: FUNCTION: Specifically hydrolyzes both 8-oxo-deoxyguanosine triphosphate (8-oxo-dGTP) and 8-oxo-guanosine triphosphate (8-oxo-GTP) to the related monophosphates, thereby cleaning up the nucleotide pools and preventing misincorporation of 8-oxoGua into DNA and RNA (PubMed:1309939, PubMed:15850400, PubMed:9311918). It prevents replicational errors by removing an oxidatively damaged form of guanine (8-oxo-dGTP) from DNA and the nucleotide pool (PubMed:1309939). 8-oxo-dGTP can be inserted opposite dA and dC residues of template DNA with almost equal efficiency thus leading to A.T to G.C transversions (PubMed:1309939). MutT may also ensure transcriptional fidelity, removing 8-oxo-GTP from the ribonucleotide triphosphate pool (PubMed:9311918). However, due to the lower efficiency of RNA polymerase 8-oxo-GTP incorporation, MutT is probably not a major contributor to transcriptional fidelity (PubMed:25294823). It also hydrolyzes 8-oxo-dGDP and 8-oxo-GDP to their monophosphate form (PubMed:15850400). In vitro, can also use dGTP, dGDP and other various nucleoside di- and triphosphates, with much lower efficiency (PubMed:1309939, PubMed:15850400, PubMed:1851162, PubMed:23481913)...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08337|protein.P08337]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000346,ECOCYC:EG10626,GeneID:944824`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:111044-111433:+; feature_type=gene
