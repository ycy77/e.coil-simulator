---
entity_id: "gene.b3703"
entity_type: "gene"
name: "rpmH"
source_database: "NCBI RefSeq"
source_id: "gene-b3703"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3703"
  - "rpmH"
---

# rpmH

`gene.b3703`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3703`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpmH (gene.b3703) is a gene entity. It encodes rpmH (protein.P0A7P5). Encoded protein function: Large ribosomal subunit protein bL34 (50S ribosomal protein L34) EcoCyc product frame: EG10892-MONOMER. EcoCyc synonyms: rimA, ssaF. Genomic coordinates: 3884336-3884476. EcoCyc protein note: The L34 protein is a component of the 50S subunit of the ribosome. L34 can be isolated in a complex with 5S rRNA, tRNA, and other proteins of the large ribosomal subunit . Assembly of L34 into the 50S ribosomal subunit is dependent on L4, L22 and L24 . L34 can be crosslinked to L23 . L34 is one of six proteins that is completely lost from ribosomes in post-stationary cells . L34 was identified as "antizyme 2", an inhibitor of the biosynthetic ornithine and arginine decarboxylases; these enzymes are involved in the biosynthesis of polyamines . In vitro and outside the context of the ribosome, L34 and a number of additional ribosomal proteins show "antizyme" inhibition of ornithine decarboxylase . L34 physically interacts with ornithine and arginine decarboxylase, and overexpression of L34 decreases the production of polyamines in vivo . Levels of L34 increase in response to polyamines; the effect is thought to be due to an increase in the level of transcription of rpmH...

## Biological Role

Repressed by yfeC (protein.P0AD37). Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7P5|protein.P0A7P5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=rpmH; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AD37|protein.P0AD37]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012115,ECOCYC:EG10892,GeneID:948216`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3884336-3884476:+; feature_type=gene
