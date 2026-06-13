---
entity_id: "gene.b2707"
entity_type: "gene"
name: "srlR"
source_database: "NCBI RefSeq"
source_id: "gene-b2707"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2707"
  - "srlR"
---

# srlR

`gene.b2707`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2707`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

srlR (gene.b2707) is a gene entity. It encodes srlR (protein.P15082). Encoded protein function: Glucitol operon repressor EcoCyc product frame: PD00283. EcoCyc synonyms: gutR. Genomic coordinates: 2829047-2829820. EcoCyc protein note: The "glucitol repressor," GutR (also called SrlR), is a DNA-binding transcription factor that represses an operon (gut) involved in transport and utilization of glucitol . This regulator is located in the unusual gut operon, which contains two glucitol-specific transcription factors, GutR and GutM, that regulate this operon negatively and positively, respectively; both regulators control transcription of glucitol PTS permease . Expression of gutR is activated in the presence of glucitol and in the absence of glucose. Although DNA binding by GutM does not depend on the presence of glucitol, this compound appears to be necessary for derepressing gutM, perhaps by interacting with GutR . In addition, Yamada et al. suggested that these regulators have contrary effects, but in the presence of glucitol, GutR interacts with this carbohydrate to dissociate from DNA, causing increments of GutM in sufficient amounts to increase transcription of the gut operon . To repress transcription, GutR recognizes DNA-binding sites, but no consensus sequence has been identified...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15082|protein.P15082]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=srlR; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=srlR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008900,ECOCYC:EG10974,GeneID:948942`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2829047-2829820:+; feature_type=gene
