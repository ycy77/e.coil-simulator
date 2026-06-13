---
entity_id: "gene.b2509"
entity_type: "gene"
name: "xseA"
source_database: "NCBI RefSeq"
source_id: "gene-b2509"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2509"
  - "xseA"
---

# xseA

`gene.b2509`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2509`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xseA (gene.b2509) is a gene entity. It encodes xseA (protein.P04994). Encoded protein function: FUNCTION: Bidirectionally degrades single-stranded DNA into large acid-insoluble oligonucleotides, which are then degraded further into small acid-soluble oligonucleotides. It can degrade 3' or 5' ss regions extending from the termini of duplex DNA molecules and displaced ss regions. It can also excise thymine dimers in vitro (Probable) (PubMed:22718974, PubMed:4602029, PubMed:4602030). ssDNA-binding requires both subunits (PubMed:22718974). Required for production of the mature 5'-end of retron Ec78 or Ec83 msDNA. Overproduction of this subunit in the absence of an equivalent quantity of the small subunit is toxic, causing cell elongation and chromosome fragmentation or loss; its toxicity is mostly suppressed by RecA (PubMed:26626352). {ECO:0000269|PubMed:22718974, ECO:0000269|PubMed:26626352, ECO:0000269|PubMed:4602029, ECO:0000269|PubMed:4602030, ECO:0000305|PubMed:6284744}. EcoCyc product frame: EG11072-MONOMER. EcoCyc synonyms: xse. Genomic coordinates: 2634232-2635602. EcoCyc protein note: XseA is the large subunit of exonuclease VII (ExoVII) - a single-strand DNA exonuclease implicated in various aspects of DNA repair.

## Biological Role

Repressed by crp (protein.P0ACJ8). Activated by marA (protein.P0ACH5).

## Enriched Pathways

- `eco03430` Mismatch repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04994|protein.P04994]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=xseA; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=xseA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008263,ECOCYC:EG11072,GeneID:946988`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2634232-2635602:+; feature_type=gene
