---
entity_id: "gene.b2330"
entity_type: "gene"
name: "prmB"
source_database: "NCBI RefSeq"
source_id: "gene-b2330"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2330"
  - "prmB"
---

# prmB

`gene.b2330`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2330`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

prmB (gene.b2330) is a gene entity. It encodes prmB (protein.P39199). Encoded protein function: FUNCTION: Specifically methylates ribosomal protein uL3 on 'Gln-150' (PubMed:11847124, PubMed:372746). Does not methylate the translation termination release factors RF1 or RF2 (PubMed:11847124). {ECO:0000269|PubMed:11847124, ECO:0000269|PubMed:372746}. EcoCyc product frame: EG12449-MONOMER. EcoCyc synonyms: yfcB. Genomic coordinates: 2447508-2448440. EcoCyc protein note: PrmB is an N5-glutamine methyltransferase that specifically methylates EG10866-MONOMER ribosomal protein L3 . PrmB and PrmC have sequence similarity to each other; PrmB is active toward ribosomal protein L3, whereas PrmC is active toward polypeptide chain release factors RF1 and RF2 . A prmB mutant lacks methylation of L3, has a cold-sensitive growth phenotype and accumulates abnormal ribosomal particles, indicating a defect in ribosome assembly . PrmB: "protein methylation B"

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39199|protein.P39199]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=prmB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007695,ECOCYC:EG12449,GeneID:946805`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2447508-2448440:-; feature_type=gene
