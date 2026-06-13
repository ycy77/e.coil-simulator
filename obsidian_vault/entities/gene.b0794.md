---
entity_id: "gene.b0794"
entity_type: "gene"
name: "ybhF"
source_database: "NCBI RefSeq"
source_id: "gene-b0794"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0794"
  - "ybhF"
---

# ybhF

`gene.b0794`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0794`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybhF (gene.b0794) is a gene entity. It encodes ybhF (protein.P0A9U1). Encoded protein function: FUNCTION: Part of the ABC transporter complex YbhFSR that could be involved in efflux of cefoperazone. Probably responsible for energy coupling to the transport system. {ECO:0000305|PubMed:27112147}. EcoCyc product frame: YBHF-MONOMER. Genomic coordinates: 827245-828981. EcoCyc protein note: ybhF encodes the ATP binding subunit of a putative ABC exporter. ybhF is part of the cecR-ybhGFSR operon which cntains genes encoding a putative ABC exporter (ybhFSR), a putative membrane fusion protein (ybhG) and a transcriptional regulator (cecR) . YbhFSR is implicated in the efflux of of the third generation cephalosporin - cefoperazone , tetracycline drugs and the cationic compounds ethidium bromide and Hoechst33342 . YbhFSR may also function as a Na+ / (Li+):proton antiporter . Transcription of cecR-ybhGFSR is negatively regulated by EG12406-MONOMER "CecR" . In the Transporter Classification Database YbhGFSR is annotated as a 4-component system within the ATP-binding Cassette (ABC) superfamily . ΔybhF mutants show reduced growth in the presence of cephalosporin . Recombinant, purified YbhF has ATPase activity .

## Biological Role

Repressed by cecR (protein.P0ACU0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9U1|protein.P0A9U1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACU0|protein.P0ACU0]] `RegulonDB` `C` - regulator=CecR; target=ybhF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002707,ECOCYC:G6411,GeneID:945413`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:827245-828981:-; feature_type=gene
