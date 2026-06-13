---
entity_id: "gene.b1814"
entity_type: "gene"
name: "sdaA"
source_database: "NCBI RefSeq"
source_id: "gene-b1814"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1814"
  - "sdaA"
---

# sdaA

`gene.b1814`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1814`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sdaA (gene.b1814) is a gene entity. It encodes sdaA (protein.P16095). Encoded protein function: FUNCTION: Also deaminates threonine, particularly when it is present in high concentration. EcoCyc product frame: LSERINEDEAM1-MONOMER. Genomic coordinates: 1896932-1898296. EcoCyc protein note: L-serine deaminase I (SdaA) is one of three enzymes carrying out the sole step in the pathway of L-serine degradation, converting serine into a basic cellular building block, pyruvate. SdaA catalyzes the conversion of L-serine into pyruvate and ammonia . SdaA contains a catalytically critical 4Fe-4S cluster that interacts directly with the L-serine substrate . This cluster is only present when the enzyme is synthesized under anaerobic conditions . Oxidatively inactivated serine deaminase can be activated in vitro with a combination of iron sulfate and dithiothreitol . Activation in vivo, presumably involving construction of the 4Fe-4S cluster, appears to require multiple additional gene products .

## Biological Role

Repressed by lrp (protein.P0ACJ0), nac (protein.Q47005). Activated by rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16095|protein.P16095]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=sdaA; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=sdaA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=sdaA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006039,ECOCYC:EG10930,GeneID:946331`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1896932-1898296:+; feature_type=gene
