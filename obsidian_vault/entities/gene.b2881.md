---
entity_id: "gene.b2881"
entity_type: "gene"
name: "xdhD"
source_database: "NCBI RefSeq"
source_id: "gene-b2881"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2881"
  - "xdhD"
---

# xdhD

`gene.b2881`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2881`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xdhD (gene.b2881) is a gene entity. It encodes xdhD (protein.Q46814). Encoded protein function: FUNCTION: Probably has no xanthine dehydrogenase activity; however deletion results in increased adenine sensitivity, suggesting that this protein contributes to the conversion of adenine to guanine nucleotides during purine salvage. {ECO:0000269|PubMed:10986234}. EcoCyc product frame: G7500-MONOMER. EcoCyc synonyms: ygfN. Genomic coordinates: 3021316-3024186. EcoCyc protein note: XdhD has similarity to molybdenum cofactor-containing xanthine oxidases, including Drosophila melanogaster xanthine dehydrogenase and Desulfovibrio gigas aldehyde oxidoreductase and is predicted to catalyze oxidation of xanthine (with electron transfer to O2, rather than dehydrogenase activity with electron transfer to NAD or NADP) . An xdhD mutant exhibits sensitivity to adenine, which is indicative of a defect in purine salvage, but it does not exhibit a defect in an indirect assay of xanthine dehydrogenase activity . Deletion of xdhD does not confer N-hydroxylaminopurine sensitivity . An xdhD null mutant is able to reduce selenate to elemental red selenium .

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46814|protein.Q46814]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009459,ECOCYC:G7500,GeneID:949079`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3021316-3024186:+; feature_type=gene
