---
entity_id: "gene.b2610"
entity_type: "gene"
name: "ffh"
source_database: "NCBI RefSeq"
source_id: "gene-b2610"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2610"
  - "ffh"
---

# ffh

`gene.b2610`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2610`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ffh (gene.b2610) is a gene entity. It encodes ffh (protein.P0AGD7). Encoded protein function: FUNCTION: Involved in targeting and insertion of nascent membrane proteins into the cytoplasmic membrane. Binds to the hydrophobic signal sequence of the ribosome-nascent chain (RNC) as it emerges from the ribosomes. The SRP-RNC complex is then targeted to the cytoplasmic membrane where it interacts with the SRP receptor FtsY. Interaction with FtsY leads to the transfer of the RNC complex to the Sec translocase for insertion into the membrane, the hydrolysis of GTP by both Ffh and FtsY, and the dissociation of the SRP-FtsY complex into the individual components. {ECO:0000255|HAMAP-Rule:MF_00306, ECO:0000269|PubMed:11735405, ECO:0000269|PubMed:11741850, ECO:0000269|PubMed:1279430, ECO:0000269|PubMed:1331806, ECO:0000269|PubMed:15140892, ECO:0000269|PubMed:2171778, ECO:0000269|PubMed:9305630}. EcoCyc product frame: EG10300-MONOMER. Genomic coordinates: 2746434-2747795. EcoCyc protein note: The structure of Ffh has been analyzed alone and in a complex with the 4.5 S RNA . Ffh contains two domains: a methionine rich M domain and an NG domain containing an N-terminal 4 helix bundle plus a G region which contains the signature motifs of the GTPase family. 4...

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGD7|protein.P0AGD7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008586,ECOCYC:EG10300,GeneID:947102`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2746434-2747795:-; feature_type=gene
