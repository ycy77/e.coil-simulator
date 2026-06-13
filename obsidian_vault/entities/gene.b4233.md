---
entity_id: "gene.b4233"
entity_type: "gene"
name: "mpl"
source_database: "NCBI RefSeq"
source_id: "gene-b4233"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4233"
  - "mpl"
---

# mpl

`gene.b4233`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4233`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mpl (gene.b4233) is a gene entity. It encodes mpl (protein.P37773). Encoded protein function: FUNCTION: Reutilizes the intact tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelate by linking it to UDP-N-acetylmuramate. The enzyme can also use the tetrapeptide L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptanedioyl-D-alanine or the pentapeptide L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptandioyl-D-alanyl-D-alanine in vivo and in vitro. {ECO:0000269|PubMed:17384195, ECO:0000269|PubMed:8808921}. EcoCyc product frame: EG12440-MONOMER. EcoCyc synonyms: tpl, yjfG. Genomic coordinates: 4455785-4457158. EcoCyc protein note: UDP-N-acetylmuramate:L-alanyl-γ-D-glutamyl-meso-diaminopimelate ligase (Mpl) acts in murein recycling by enabling ligation of the tripeptide L-Ala-D-Glu-mesoA2pm with UDP-MurNAc and reincorporation into peptidoglycan. L-Ala-D-Glu-mesoA2pm is released while remodelling the cell wall during growth . The enzyme can utilize tri-, tetra-, and pentapeptide in vitro and in vivo, but utilizes either the dipeptide L-Ala-D-Glu or L-Ala alone at a much lower rate. The substrate specificity of Mpl has been investigated . An mpl null mutant shows no obvious growth defect, but has decreased levels of UDP-MurNAc-pentapeptide and increased levels of L-Ala-D-Glu-mesoA2pm...

## Biological Role

Repressed by cra (protein.P0ACP1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37773|protein.P37773]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=mpl; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013847,ECOCYC:EG12440,GeneID:948752`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4455785-4457158:+; feature_type=gene
