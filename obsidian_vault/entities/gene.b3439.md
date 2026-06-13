---
entity_id: "gene.b3439"
entity_type: "gene"
name: "yhhW"
source_database: "NCBI RefSeq"
source_id: "gene-b3439"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3439"
  - "yhhW"
---

# yhhW

`gene.b3439`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3439`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhhW (gene.b3439) is a gene entity. It encodes yhhW (protein.P46852). Encoded protein function: FUNCTION: Has quercetin 2,3-dioxygenase activity in vitro. Its physiological role is unknown; however, may provide a mechanism that would avoid inhibition of key cellular proteins, such as DNA gyrase, by quercetin. {ECO:0000269|PubMed:15951572}. EcoCyc product frame: G7756-MONOMER. Genomic coordinates: 3578950-3579645. EcoCyc protein note: YhhW was identified as a Pirin homolog and was shown to have quercetin 2,3-dioxygenase activity, which results in the release of carbon monoxide. Quercetin is a flavonoid, a class of widely occurring compounds synthesized by plants. Possible roles of eukaryotic pirins, including modulation of transcription, DNA replication, or repair, programmed cell death, seed germination and seedling development have been proposed. The physiological role of YhhW in E. coli is unknown. A crystal structure of YhhW has been solved at 2.0 Å resolution. The structure is similar to that of quercetin 2,3-dioxygenase; modelling of potential binding pockets showed that quercetin may be a substrate . Expression of yhhW is induced by exposure to hydroquinone; this induction is abolished in a yhaJ mutant .

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0), yhaJ (protein.P67660).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46852|protein.P46852]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P67660|protein.P67660]] `RegulonDB` `S` - regulator=YhaJ; target=yhhW; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011228,ECOCYC:G7756,GeneID:947945`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3578950-3579645:-; feature_type=gene
