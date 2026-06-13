---
entity_id: "gene.b0792"
entity_type: "gene"
name: "ybhR"
source_database: "NCBI RefSeq"
source_id: "gene-b0792"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0792"
  - "ybhR"
---

# ybhR

`gene.b0792`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0792`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybhR (gene.b0792) is a gene entity. It encodes ybhR (protein.P0AFP9). Encoded protein function: FUNCTION: Part of the ABC transporter complex YbhFSR that could be involved in efflux of cefoperazone. Probably involved in the translocation of the substrate across the membrane. {ECO:0000305|PubMed:27112147}. EcoCyc product frame: YBHR-MONOMER. Genomic coordinates: 825002-826108. EcoCyc protein note: ybhR encodes one of two the integral membrane subunits of a putative ABC exporter. ybhR is part of the cecR-ybhGFSR operon which contains genes encoding a putative ABC exporter (ybhFSR), a putative membrane fusion protein (ybhG) and a transcriptional regulator (cecR) . YbhFSR is implicated in the efflux of of the third generation cephalosporin - cefoperazone , tetracycline drugs and the cationic compounds ethidium bromide and Hoechst33342 . YbhFSR may also function as a Na+ / (Li+):proton antiporter . Transcription of cecR-ybhGFSR is negatively regulated by EG12406-MONOMER CecR . In the Transporter Classification Database YbhGFSR is annotated as a 4-component system within the ATP-binding Cassette (ABC) superfamily . Overexpression of ybhR from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hypochlorous acid .

## Biological Role

Repressed by cecR (protein.P0ACU0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFP9|protein.P0AFP9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACU0|protein.P0ACU0]] `RegulonDB` `C` - regulator=CecR; target=ybhR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002701,ECOCYC:G6409,GeneID:945403`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:825002-826108:-; feature_type=gene
