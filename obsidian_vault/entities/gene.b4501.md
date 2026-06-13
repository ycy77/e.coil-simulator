---
entity_id: "gene.b4501"
entity_type: "gene"
name: "torI"
source_database: "NCBI RefSeq"
source_id: "gene-b4501"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4501"
  - "torI"
---

# torI

`gene.b4501`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4501`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

torI (gene.b4501) is a gene entity. It encodes torI (protein.Q2EES9). Encoded protein function: FUNCTION: Transcription inhibitory protein for the torCAD operon. Also acts as an excisionase and plays an essential role in the defective prophage CPS53 excision. {ECO:0000269|PubMed:15197250, ECO:0000269|PubMed:16079126}. EcoCyc product frame: MONOMER0-1641. Genomic coordinates: 2476310-2476510. EcoCyc protein note: TorI is the recombination directionality factor (RDF) for KplE1 (or CPS-53) prophage excision. TorI was shown to be required for prophage excision in vivo and in vitro . DnaJ interacts with and stabilizes TorI and stimulates prophage excision . A solution structure of TorI has been solved. TorI is a winged-helix protein that is structurally highly similar to the phage λ Xis protein, the Mu bacteriophage repressor MuR, and Mu transposase, and may represent the structural "missing link" between λXis and MuR. Conserved residues that are involved in DNA binding have been identified and confirmed by site-directed mutagenesis . The binding sites of TorI in the KplE1 prophage region have been mapped . The presence of their DNA target sites stabilizes TorI oligomers , and DnaJ stimulates binding of TorI to the target sites . Binding of TorI in the G7218 intS promoter region negatively regulates IntS expression...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q2EES9|protein.Q2EES9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=torI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0269710,ECOCYC:G0-9621,GeneID:1450232`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2476310-2476510:+; feature_type=gene
