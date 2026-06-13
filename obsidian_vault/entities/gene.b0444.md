---
entity_id: "gene.b0444"
entity_type: "gene"
name: "queC"
source_database: "NCBI RefSeq"
source_id: "gene-b0444"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0444"
  - "queC"
---

# queC

`gene.b0444`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0444`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

queC (gene.b0444) is a gene entity. It encodes queC (protein.P77756). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent conversion of 7-carboxy-7-deazaguanine (CDG) to 7-cyano-7-deazaguanine (preQ(0)). {ECO:0000250, ECO:0000269|PubMed:16199558}. EcoCyc product frame: G6245-MONOMER. EcoCyc synonyms: ybaX. Genomic coordinates: 464852-465547. EcoCyc protein note: QueC appears to be the 7-cyano-7-deazaguanine synthase that catalyzes an early step of queuosine biosynthesis, leading from GTP to the formation of preQ0 . Queuosine is one of the most complex tRNA modifications, occurring at the wobble position of the GUN anticodon in the Asn, Asp, Tyr, and His tRNAs. queC rescues the queuosine deficiency phenotype of a mutant E. coli B strain . The biochemical activity of QueC was studied using the orthologous BSU13720-MONOMER from TAX-1423 .

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77756|protein.P77756]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001539,ECOCYC:G6245,GeneID:947034`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:464852-465547:-; feature_type=gene
