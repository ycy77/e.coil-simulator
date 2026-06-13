---
entity_id: "gene.b0167"
entity_type: "gene"
name: "glnD"
source_database: "NCBI RefSeq"
source_id: "gene-b0167"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0167"
  - "glnD"
---

# glnD

`gene.b0167`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0167`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glnD (gene.b0167) is a gene entity. It encodes glnD (protein.P27249). Encoded protein function: FUNCTION: Modifies, by uridylylation and deuridylylation, the PII regulatory proteins GlnB and GlnK, in response to the nitrogen status of the cell that GlnD senses through the glutamine level. Under low glutamine levels, catalyzes the conversion of the PII proteins and UTP to PII-UMP and PPi, while under higher glutamine levels, GlnD hydrolyzes PII-UMP to PII and UMP (deuridylylation). Thus, controls uridylylation state and activity of the PII proteins, and plays an important role in the regulation of nitrogen assimilation and metabolism. {ECO:0000269|PubMed:10231487, ECO:0000269|PubMed:20363937, ECO:0000269|PubMed:6130097, ECO:0000269|PubMed:8843440, ECO:0000269|PubMed:9737855}. EcoCyc product frame: GLND-MONOMER. EcoCyc synonyms: glnD5. Genomic coordinates: 185978-188650. EcoCyc protein note: Uridylyltransferase (UTase) encoded by glnD is a bifunctional protein that catalyzes the uridylylation as well as the de-uridylylation of PROTEIN-PII. Uridylylation and deuridylylation are distinct reactions; uridylylation involves the transfer of a UMP group (derived from UTP) to PII-1 to form PII-1-UMP and pyrophosphate; deuridylylation of PII-1-UMP is a hydrolytic reaction that results in the release of UMP and PII-1...

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27249|protein.P27249]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=glnD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000568,ECOCYC:EG11411,GeneID:944863`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:185978-188650:-; feature_type=gene
