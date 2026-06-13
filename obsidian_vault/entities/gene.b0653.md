---
entity_id: "gene.b0653"
entity_type: "gene"
name: "gltK"
source_database: "NCBI RefSeq"
source_id: "gene-b0653"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0653"
  - "gltK"
---

# gltK

`gene.b0653`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0653`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gltK (gene.b0653) is a gene entity. It encodes gltK (protein.P0AER5). Encoded protein function: FUNCTION: Part of the ABC transporter complex GltIJKL involved in glutamate and aspartate uptake. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000305|PubMed:9593292}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from P.luminescens strain TTO1 across the inner membrane to the cytoplasm, where CdiA has a toxic effect. Toxin transport is strain-specific, mutations in this gene do not confer resistance to several other tested CdiA toxins. {ECO:0000269|PubMed:26305955}. EcoCyc product frame: GLTK-MONOMER. Genomic coordinates: 685255-685929. EcoCyc protein note: GltK is the predicted integral membrane subunit of a glutamate/aspartate ABC transporter complex (see . GltK has been implicated in the import of specific toxins of contact-dependent growth inhibition (CDI) systems in gram-negative bacteria; gltK transposon insertion mutants and gltK in-frame deletion mutants are resistant to the CdiA-CTTT01 toxin; inner membrane proteins such as GltK are thought to act as receptors which bring the nuclease domain of CDI toxins into close proximity with the inner membrane of target cells .

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AER5|protein.P0AER5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002234,ECOCYC:EG12662,GeneID:947354`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:685255-685929:-; feature_type=gene
