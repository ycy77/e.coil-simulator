---
entity_id: "gene.b1742"
entity_type: "gene"
name: "ves"
source_database: "NCBI RefSeq"
source_id: "gene-b1742"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1742"
  - "ves"
---

# ves

`gene.b1742`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1742`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ves (gene.b1742) is a gene entity. It encodes ves (protein.P76214). Encoded protein function: Protein Ves (Various environmental stresses-induced protein) EcoCyc product frame: G6938-MONOMER. EcoCyc synonyms: ydjR. Genomic coordinates: 1824362-1824937. EcoCyc protein note: The C terminus of Ves has some similarity to CspA-related proteins . A ves null mutant is viable and shows no obvious growth defect. Transcription of ves is highest at 25°C . Ves: "regulated under various environmental stresses"

## Biological Role

Activated by fliA (protein.P0AEM6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76214|protein.P76214]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=ves; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005809,ECOCYC:G6938,GeneID:946245`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1824362-1824937:-; feature_type=gene
