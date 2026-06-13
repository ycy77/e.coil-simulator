---
entity_id: "gene.b3304"
entity_type: "gene"
name: "rplR"
source_database: "NCBI RefSeq"
source_id: "gene-b3304"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3304"
  - "rplR"
---

# rplR

`gene.b3304`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3304`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplR (gene.b3304) is a gene entity. It encodes rplR (protein.P0C018). Encoded protein function: FUNCTION: This is one of the proteins that mediates the attachment of the 5S rRNA subcomplex onto the large ribosomal subunit where it forms part of the central protuberance. Binds stably to 5S rRNA; increases binding abilities of L5 in a cooperative fashion; both proteins together confer 23S rRNA binding. The 5S rRNA and some of its associated proteins might help stabilize positioning of ribosome-bound tRNAs. {ECO:0000269|PubMed:109811, ECO:0000269|PubMed:353728, ECO:0000269|PubMed:354687, ECO:0000269|PubMed:6159586, ECO:0000269|PubMed:7038683}. EcoCyc product frame: EG10879-MONOMER. Genomic coordinates: 3445244-3445597. EcoCyc protein note: The L18 protein is a component of the 50S subunit of the ribosome and is required for incorporation of 5S rRNA into the ribosome . L18 interacts with both 23S rRNA and 5S rRNA . L18 together with L5 can associate into a quaternary complex with 5S and 23S rRNAs . The binding determinants of the 5S rRNA-L5-L18-L25 complex have been mapped . Both L5 and L18 are essential for viability . Iodination at a tyrosine residue abolishes binding of L18 to 5S rRNA . L18 is posttranslationally modified by phosphorylation, most likely at the Ser45 residue...

## Biological Role

Repressed by rpsH (protein.P0A7W7), lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C018|protein.P0C018]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A7W7|protein.P0A7W7]] `RegulonDB` `S` - regulator=RpsH; target=rplR; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010825,ECOCYC:EG10879,GeneID:947804`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3445244-3445597:-; feature_type=gene
