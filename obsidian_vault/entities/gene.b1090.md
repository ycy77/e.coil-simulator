---
entity_id: "gene.b1090"
entity_type: "gene"
name: "plsX"
source_database: "NCBI RefSeq"
source_id: "gene-b1090"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1090"
  - "plsX"
---

# plsX

`gene.b1090`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1090`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

plsX (gene.b1090) is a gene entity. It encodes plsX (protein.P27247). Encoded protein function: FUNCTION: Catalyzes the reversible formation of acyl-phosphate (acyl-PO(4)) from acyl-[acyl-carrier-protein] (acyl-ACP). This enzyme utilizes acyl-ACP as fatty acyl donor, but not acyl-CoA. {ECO:0000255|HAMAP-Rule:MF_00019, ECO:0000269|PubMed:17645809}. EcoCyc product frame: EG11437-MONOMER. Genomic coordinates: 1147621-1148691. EcoCyc protein note: PlsX, together with EG11674-MONOMER PlsY, can substitute for GLYCEROL-3-P-ACYLTRANSFER-MONOMER (PlsB) in synthesis of 2-Acyl-sn-glycerol-3-phosphates required for initiation of phospholipid synthesis and fine-tune the levels of other lipids involved in the structure of the cell envelope . Most Gram-negative proteobacteria have both the PlsX/PlsY and PlsB systems . The transcript levels and operon structure of plsX have been analyzed . A mutation in plsX is required for the sn-glycerol-3-phosphate auxotrophic phenotype of a plsB mutant strain . A plsX plsY double deletion is lethal . Yoshimura et al. hypothesize that PlsX and PlsY play a role in regulating the intracellular concentration of acyl-ACP . Using a suppressor screen approach, the plsX plsY double deletion synthetic lethality was confirmed, and rescue of this phenotype required increased levels of G3P that could be obtained through secondary mutations, such as in EG10400...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27247|protein.P27247]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=plsX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003692,ECOCYC:EG11437,GeneID:946165`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1147621-1148691:+; feature_type=gene
