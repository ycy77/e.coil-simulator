---
entity_id: "gene.b4559"
entity_type: "gene"
name: "ghoT"
source_database: "NCBI RefSeq"
source_id: "gene-b4559"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4559"
  - "ghoT"
---

# ghoT

`gene.b4559`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4559`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ghoT (gene.b4559) is a gene entity. It encodes ghoT (protein.P64646). Encoded protein function: FUNCTION: Toxic component of a type V toxin-antitoxin (TA) system. Causes membrane damage when induced by MqsR, slowing cell growth and increasing the formation of dormant persister cells; involved with GhoS, its antitoxin, in reducing cell growth during antibacterial stress (PubMed:24373067). Overexpression causes cell lysis, forming ghost cells; both effects are neutralized by expression of GhoS. Overexpression in the presence of ampicillin increases persister cell formation (persister cells exhibit antibiotic tolerance without genetic change) (PubMed:22941047). Overexpression causes about 90-fold reduction in cellular ATP levels and dissipates the membrane potential (PubMed:24373067). {ECO:0000269|PubMed:22941047, ECO:0000269|PubMed:24373067}. EcoCyc product frame: MONOMER0-2694. EcoCyc synonyms: yjdO. Genomic coordinates: 4352908-4353081. EcoCyc protein note: GhoT is the toxin of a novel type V toxin-antitoxin system. GhoT is a peptide that damages the membrane, reduces cellular ATP levels and disrupts membrane potential, causing ghost cell formation and increasing persistence . The GhoS antitoxin acts by specifically cleaving ghoT mRNA...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64646|protein.P64646]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0285080,ECOCYC:G0-10472,GeneID:1450308`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4352908-4353081:+; feature_type=gene
