---
entity_id: "gene.b4016"
entity_type: "gene"
name: "aceK"
source_database: "NCBI RefSeq"
source_id: "gene-b4016"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4016"
  - "aceK"
---

# aceK

`gene.b4016`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4016`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aceK (gene.b4016) is a gene entity. It encodes aceK (protein.P11071). Encoded protein function: FUNCTION: Bifunctional enzyme which can phosphorylate or dephosphorylate isocitrate dehydrogenase (IDH) on a specific serine residue. This is a regulatory mechanism which enables bacteria to bypass the Krebs cycle via the glyoxylate shunt in response to the source of carbon. When bacteria are grown on glucose, IDH is fully active and unphosphorylated, but when grown on acetate or ethanol, the activity of IDH declines drastically concomitant with its phosphorylation. EcoCyc product frame: ICITDEHASE-KIN-PHOSPHA. Genomic coordinates: 4218596-4220332. EcoCyc protein note: Isocitrate dehydrogenase kinase/phosphatase (AceK) controls a branch point between two pathways of central metabolism, the TCA and the GLYOXYLATE-BYPASS, shown in the TCA-GLYOX-BYPASS. It controls the flux between the two cycles by controlling the activity of ISOCITHASE-CPLX (IDH), an enzyme of the TCA cycle . By phosphorylating and thus inactivating IDH , its substrate isocitrate is diverted to the glyoxylate cycle enzyme, isocitrate lyase. By dephosphorylating and thus activating IDH, this enzyme's stronger affinity for isocitrate feeds it into the TCA cycle. Models that attempt to explain the robustness of the IDH regulatory system have been published and have provided potential explanations...

## Biological Role

Repressed by iclR (protein.P16528). Activated by rpoD (protein.P00579), cra (protein.P0ACP1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11071|protein.P11071]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=aceK; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=aceK; function=+
- `represses` <-- [[protein.P16528|protein.P16528]] `RegulonDB` `S` - regulator=IclR; target=aceK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013131,ECOCYC:EG10026,GeneID:944797`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4218596-4220332:+; feature_type=gene
