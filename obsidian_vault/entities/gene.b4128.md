---
entity_id: "gene.b4128"
entity_type: "gene"
name: "ghoS"
source_database: "NCBI RefSeq"
source_id: "gene-b4128"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4128"
  - "ghoS"
---

# ghoS

`gene.b4128`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4128`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ghoS (gene.b4128) is a gene entity. It encodes ghoS (protein.P0AF61). Encoded protein function: FUNCTION: Antitoxin component of a type V toxin-antitoxin (TA) system. Neutralizes the toxic effects of toxin GhoT by digesting ghoT transcripts in a sequence-specific manner (PubMed:22941047). In concert with GhoT is involved in reducing cell growth during antibacterial stress (PubMed:24373067). Overexpression leads to transcript level reduction of 20 other mRNAs involved in purine or pyrimidine synthesis and transport. Not seen to bind its own promoter DNA (PubMed:22941047). {ECO:0000269|PubMed:22941047, ECO:0000269|PubMed:24373067}. EcoCyc product frame: G7830-MONOMER. EcoCyc synonyms: yjdK. Genomic coordinates: 4352584-4352880. EcoCyc protein note: GhoS is the antitoxin of a novel type V toxin-antitoxin system. GhoS is a sequence-specific endoribonuclease that specifically cleaves sites within the ghoT coding region of the ghoST transcript, thereby limiting translation of the GhoT toxin . ghoT is one of a small set of coding regions that do not contain cleavage sites for the G7572-MONOMER MqsR toxin, whereas the ghoS coding region contains three consensus MqsR cleavage sites. Thus, in the presence of MqsR, the ghoS-encoding 5' region of the ghoST transcript is degraded, thereby enriching for the ghoT-encoding 3' region...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF61|protein.P0AF61]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013518,ECOCYC:G7830,GeneID:948646`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4352584-4352880:+; feature_type=gene
