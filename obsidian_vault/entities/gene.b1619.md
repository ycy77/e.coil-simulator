---
entity_id: "gene.b1619"
entity_type: "gene"
name: "hdhA"
source_database: "NCBI RefSeq"
source_id: "gene-b1619"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1619"
  - "hdhA"
---

# hdhA

`gene.b1619`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1619`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hdhA (gene.b1619) is a gene entity. It encodes hdhA (protein.P0AET8). Encoded protein function: FUNCTION: 7alpha-hydroxysteroid dehydrogenase involved in the metabolism of bile acids. Catalyzes the NAD(+)-dependent oxidation of the 7alpha-hydroxy group of 7alpha-hydroxysteroids, such as the major human bile acids cholate and chenodeoxycholate, to the corresponding 7-oxosteroids. To a lesser extent, can also act on taurochenodeoxycholate, taurocholate and glycocholate (PubMed:2007545). Can also use glycochenodeoxycholate as substrate (PubMed:8672472). Is not able to use NADP(+) instead of NAD(+) as the electron acceptor (PubMed:2007545). {ECO:0000269|PubMed:2007545, ECO:0000269|PubMed:8672472}. EcoCyc product frame: 7-ALPHA-HYDROXYSTEROID-DEH-MONOMER. EcoCyc synonyms: hsd, hsdH. Genomic coordinates: 1697273-1698040. EcoCyc protein note: 7-α-hydroxysteroid dehydrogenase catalyzes the dehydroxylation of cholic and chenodeoxycholic acids, major human bile acids, yielding 7-oxocholic and 7-oxochenodeoxycholic acids, respectively. The enzyme belongs to the short-chain nonmetalloenzyme-alcohol dehydrogenase protein family. The enzyme shows activity with several substrates having a hydroxyl group at position 7 of the steroid skeleton. NAD+ is required for enzyme activity . Crystal structures of the enzyme in binary and ternary complexes have been solved...

## Enriched Pathways

- `eco00121` Secondary bile acid biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AET8|protein.P0AET8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005419,ECOCYC:EG10425,GeneID:946151`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1697273-1698040:-; feature_type=gene
