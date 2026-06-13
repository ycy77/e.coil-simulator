---
entity_id: "gene.b1453"
entity_type: "gene"
name: "ansP"
source_database: "NCBI RefSeq"
source_id: "gene-b1453"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1453"
  - "ansP"
---

# ansP

`gene.b1453`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1453`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ansP (gene.b1453) is a gene entity. It encodes ansP (protein.P77610). Encoded protein function: L-asparagine permease (L-asparagine transport protein) EcoCyc product frame: ANSP-MONOMER. EcoCyc synonyms: yncF. Genomic coordinates: 1524481-1525980. EcoCyc protein note: AnsP is a probable L-asparagine transporter. The equivalent gene to ansP in Salmonella enterica has been expressed and shown to confer L-asparagine uptake . AnsP is a member of the Amino Acid-Polyamine-Organocation (APC) superfamily of transporters and probably functions as an L-asparagine:proton symporter.

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77610|protein.P77610]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ansP; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ansP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004845,ECOCYC:G6764,GeneID:946019`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1524481-1525980:-; feature_type=gene
