---
entity_id: "gene.b1060"
entity_type: "gene"
name: "bssS"
source_database: "NCBI RefSeq"
source_id: "gene-b1060"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1060"
  - "bssS"
---

# bssS

`gene.b1060`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1060`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bssS (gene.b1060) is a gene entity. It encodes bssS (protein.P0AB33). Encoded protein function: FUNCTION: Represses biofilm formation in M9C glu and LB glu media but not in M9C and LB media. Seems to act as a global regulator of several genes involved in catabolite repression and stress response and regulation of the uptake and export of signaling pathways. Could be involved the regulation of indole as well as uptake and export of AI-2 through a cAMP-dependent pathway. {ECO:0000269|PubMed:16597943}. EcoCyc product frame: G6557-MONOMER. EcoCyc synonyms: yceP. Genomic coordinates: 1120701-1120955. EcoCyc protein note: There have been contradictory reports on the effect of a bssS mutation on biofilm formation. reported that a bssS mutant is impaired in biofilm formation, while reported that deletion of bssS leads to increased biofilm formation in LB+glucose and MC9C+glucose media and increased motility in LB medium. A bssS deletion mutant does not have a significant growth defect. Deletion of bssS affects the expression of more than 400 genes significantly. Among the affected pathways are indole transport and AI-2 uptake and processing. A regulatory model has been proposed . Transcription of bssS is induced upon biofilm formation compared to planktonic growth in both exponential and stationary phase...

## Biological Role

Activated by lrp (protein.P0ACJ0), glaR (protein.P37338), yhaJ (protein.P67660), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB33|protein.P0AB33]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=bssS; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P67660|protein.P67660]] `RegulonDB` `S` - regulator=YhaJ; target=bssS; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=bssS; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003594,ECOCYC:G6557,GeneID:946104`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1120701-1120955:-; feature_type=gene
