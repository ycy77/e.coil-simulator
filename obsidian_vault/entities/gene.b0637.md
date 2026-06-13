---
entity_id: "gene.b0637"
entity_type: "gene"
name: "rsfS"
source_database: "NCBI RefSeq"
source_id: "gene-b0637"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0637"
  - "rsfS"
---

# rsfS

`gene.b0637`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0637`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rsfS (gene.b0637) is a gene entity. It encodes rsfS (protein.P0AAT6). Encoded protein function: FUNCTION: Functions as a ribosomal silencing factor (PubMed:22829778). Interacts with ribosomal protein uL14 (rplN), blocking formation of intersubunit bridge B8. Prevents association of the 30S and 50S ribosomal subunits and the formation of functional ribosomes, thus repressing translation (PubMed:22829778). {ECO:0000255|HAMAP-Rule:MF_01477, ECO:0000269|PubMed:22829778}.; FUNCTION: Member of a network of 50S ribosomal subunit biogenesis factors (ObgE, RluD, RsfS and DarP(YjgA)) which assembles along the 30S-50S interface, preventing incorrect 23S rRNA structures from forming (PubMed:33639093). Binds to late stage, pre-50S ribosomal subunits where it contacts ObgE and enhances the latter's GTPase activity (PubMed:33639093). Addition to isolated ribosomal subunits partially inhibits their association, preventing translation (PubMed:22829778). {ECO:0000269|PubMed:22829778, ECO:0000269|PubMed:33639093}. EcoCyc product frame: EG11255-MONOMER. EcoCyc synonyms: ybeB, rsfA. Genomic coordinates: 668719-669036. EcoCyc protein note: RsfS is a ribosomal silencing factor that inhibits assembly of the functional 70S ribosome. It interacts directly with the EG10875-MONOMER . RsfS may act as an anti-association factor in both ribosome assembly and silencing...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAT6|protein.P0AAT6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002183,ECOCYC:EG11255,GeneID:945237`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:668719-669036:-; feature_type=gene
