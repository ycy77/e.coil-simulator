---
entity_id: "gene.b2583"
entity_type: "gene"
name: "tapT"
source_database: "NCBI RefSeq"
source_id: "gene-b2583"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2583"
  - "tapT"
---

# tapT

`gene.b2583`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2583`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tapT (gene.b2583) is a gene entity. It encodes tapT (protein.Q47319). Encoded protein function: FUNCTION: Catalyzes the formation of 3-(3-amino-3-carboxypropyl)uridine (acp3U) at position 47 of tRNAs (PubMed:31804502, PubMed:31863583, PubMed:4597321). Acp3U47 confers thermal stability on tRNA (PubMed:31804502). {ECO:0000269|PubMed:31804502, ECO:0000269|PubMed:31863583, ECO:0000269|PubMed:4597321}. EcoCyc product frame: G7349-MONOMER. EcoCyc synonyms: yfiP, tuaA. Genomic coordinates: 2719223-2719921. EcoCyc protein note: tRNA-uridine aminocarboxypropyltransferase catalyzes the transfer of the aminocarboxypropyl group from S-adenosylmethionine to the N3 position of uridine within tRNAs . The physiological significance of the 3-(3-amino-3-carboxypropyl)uridine (acp3U) modification is so far unknown . The acp3U modification of tRNAs is widely conserved ; in E. coli, it resides in nucleotide 47 of the variable loop of eight specific tRNAs and appears to increase their thermal stability . Depending on the specific tRNA, lack of prior m7G modification at position 46 reduces acp3U modification . A structural model of TapT suggests the presence of a trefoil knot that is characteristic of the α/β knot methyltransferase superfamily . TapT binds Zn2+ in vitro; the N-terminal domain of TapT with a putative zinc-binding motif is required for catalytic activity...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47319|protein.Q47319]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008503,ECOCYC:G7349,GeneID:947057`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2719223-2719921:+; feature_type=gene
