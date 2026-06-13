---
entity_id: "gene.b2505"
entity_type: "gene"
name: "yfgH"
source_database: "NCBI RefSeq"
source_id: "gene-b2505"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2505"
  - "yfgH"
---

# yfgH

`gene.b2505`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2505`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfgH (gene.b2505) is a gene entity. It encodes yfgH (protein.P65290). Encoded protein function: Uncharacterized lipoprotein YfgH EcoCyc product frame: G7316-MONOMER. Genomic coordinates: 2629792-2630310. EcoCyc protein note: Strong aggravating interactions (measured by relative colony size and fitness in rich medium) were observed between lptD and yfgH . Deletion of yfgH results in impaired outer membrane integrity as evidenced by vancomycin induced morphological defects and lowered outer membrane protein (OMP) abundance . Deletion of yfgH and lptD results in cell wall failure/lysis, lowered OMP abundance and increased levels of the DegP stress response protease . YfgH contains a predicted lipoprotein signal; YfgH is an experimentally confirmed lipoprotein ( based on unpublished results).

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P65290|protein.P65290]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yfgH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008250,ECOCYC:G7316,GeneID:945709`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2629792-2630310:+; feature_type=gene
