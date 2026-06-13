---
entity_id: "gene.b3822"
entity_type: "gene"
name: "recQ"
source_database: "NCBI RefSeq"
source_id: "gene-b3822"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3822"
  - "recQ"
---

# recQ

`gene.b3822`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3822`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

recQ (gene.b3822) is a gene entity. It encodes recQ (protein.P15043). Encoded protein function: FUNCTION: An ATP-dependent DNA helicase which unwinds DNA in a 3'-5' direction (PubMed:12771204, PubMed:16084389, PubMed:2164680, PubMed:9553043). ATPase activity is stimulated by single-stranded (ss)DNA but only very poorly by double-stranded (ds)DNA (PubMed:2164680). Binds to and unwinds a wide variety of substrates including 3- and 4-way junctions (including Holliday junctions, HJ), flayed duplexes, 5'- and 3'-overhangs and blunt end duplexes (PubMed:19151156, PubMed:9553043, PubMed:22722926). HJ DNA unwinding is stimulated by single-stranded binding protein (SSB) (PubMed:22722926). Unwinds G-quadruplex DNA (PubMed:11292849, PubMed:23657261). Unlike yeast SGS1 or human BLM, is equally active on dsDNA versus G-quadruplex substrates (PubMed:11292849). Can act as an initiator during homologous recombination; unwinds a linear dsDNA substrate which can be used by RecA to initiate homologous DNA pairing as well as dissociation (PubMed:9553043). The identity of a few residues in the C-terminal HRDC domain influences the type of DNA substrate bound (PubMed:16084389). Involved in the RecF recombination pathway (PubMed:2993821)...

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15043|protein.P15043]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012483,ECOCYC:EG10833,GeneID:948318`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4005864-4007693:+; feature_type=gene
