---
entity_id: "gene.b0023"
entity_type: "gene"
name: "rpsT"
source_database: "NCBI RefSeq"
source_id: "gene-b0023"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0023"
  - "rpsT"
---

# rpsT

`gene.b0023`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0023`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsT (gene.b0023) is a gene entity. It encodes rpsT (protein.P0A7U7). Encoded protein function: FUNCTION: Binds directly to 16S ribosomal RNA. EcoCyc product frame: EG10919-MONOMER. EcoCyc synonyms: supS, sup(s20), supS20. Genomic coordinates: 20815-21078. EcoCyc protein note: The S20 protein is a component of the 30S subunit of the ribosome and appears to be involved in translation initiation and the association of the 30S and 50S subunits . S20 was also identified as antizyme 1, an inhibitor of the biosynthetic ornithine and arginine decarboxylases; these enzymes are involved in the biosynthesis of polyamine . S20 is identical to L26. The synthesis of S20 is regulated at the post-transcriptional level ; in an in vitro system, S20 represses its own synthesis . However, S20 doesn't show affinity for its own mRNA . The UUG initiation codon appears to be important for regulation . Processing and degradation of rpsT mRNA have been studied extensively; see for example and references therein. rpsT mRNA stability and translational efficiency are linked . S20 physically interacts with ornithine and arginine decarboxylase, and overexpression of S20 decreases the production of polyamine in vivo . Levels of S20 increase in response to polyamines; the effect is thought to be due to an increase in the level of transcription of rpsT...

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7U7|protein.P0A7U7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000082,ECOCYC:EG10919,GeneID:944759`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:20815-21078:-; feature_type=gene
