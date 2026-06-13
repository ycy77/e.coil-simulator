---
entity_id: "gene.b2603"
entity_type: "gene"
name: "yfiR"
source_database: "NCBI RefSeq"
source_id: "gene-b2603"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2603"
  - "yfiR"
---

# yfiR

`gene.b2603`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2603`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfiR (gene.b2603) is a gene entity. It encodes yfiR (protein.P64548). Encoded protein function: FUNCTION: Repressor of the cell division arrest function of DgcN. Prevents DgcN relocation to the midcell. {ECO:0000269|PubMed:27507823}. EcoCyc product frame: G7354-MONOMER. Genomic coordinates: 2741875-2742393. EcoCyc protein note: An in-frame yfiR deletion mutant loses swarming motility, but only mildly affects swimming motility. A yfiR mutation partially suppresses the motility defect of a yhjH mutant. Deletion of yfiN suppresses the swarming defect of the yfiR deletion mutant . YfiR counteracts relocation of EG12880-MONOMER DgcN to the Z ring; reductive stress inactivates this YfiR function . In uropathogenic E. coli UTI89, YfiR is a periplasmic protein that represses the diguanylate cyclase YfiN. YfiR is a substrate of the DsbA/DsbB disulfide bond forming system in E. coli UTI89 . yfiR, yfiN and yfiB may form an operon in E. coli K-12. In Pseudomonas aeruginosa, this operon is involved in exopolysaccharide synthesis ; in uropathogenic E. coli, YfiR and YfiN were shown to have a role in cellulose production, but no evidence implicating YfiB in this process was obtained . E. coli K-12 does not produce cellulose due to a mutation in the bcs operon (see EG12261).

## Biological Role

Repressed by glaR (protein.P37338), nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64548|protein.P64548]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yfiR; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yfiR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yfiR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008568,ECOCYC:G7354,GeneID:947090`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2741875-2742393:+; feature_type=gene
