---
entity_id: "gene.b2029"
entity_type: "gene"
name: "gnd"
source_database: "NCBI RefSeq"
source_id: "gene-b2029"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2029"
  - "gnd"
---

# gnd

`gene.b2029`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2029`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gnd (gene.b2029) is a gene entity. It encodes gnd (protein.P00350). Encoded protein function: FUNCTION: Catalyzes the oxidative decarboxylation of 6-phosphogluconate to ribulose 5-phosphate and CO(2), with concomitant reduction of NADP to NADPH. {ECO:0000269|PubMed:19686854}. EcoCyc product frame: 6PGLUCONDEHYDROG-MONOMER. Genomic coordinates: 2099862-2101268. EcoCyc protein note: 6-phosphogluconate dehydrogenase (6PGDH) is an enzyme of the oxidative branch of the pentose phosphate pathway. Three crystal structures of the enzyme in complex with substrate and cosubstrate compounds have been solved. Binding of NADP+ may induce a conformational change in the enzyme. A catalytic mechanism has been proposed . gnd is a highly polymorphic gene within E. coli populations, likely due to interstrain transfer and recombination. This may be a result of its proximity to the rfb region, which determines O antigen structure . Expression of 6PGDH is growth rate-regulated . Most of the growth rate-dependent increase in 6PGDH levels is due to increased transcription, leading to higher mRNA levels . Post-transcriptional regulation involves a secondary structure element between codons 67 and 78 of the gnd mRNA . This region may function by sequestration of the translation initiation region into an mRNA secondary structure, thus reducing the efficiency of translation initiation...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00350|protein.P00350]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gnd; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006737,ECOCYC:EG10411,GeneID:946554`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2099862-2101268:-; feature_type=gene
