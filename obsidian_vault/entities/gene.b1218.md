---
entity_id: "gene.b1218"
entity_type: "gene"
name: "chaC"
source_database: "NCBI RefSeq"
source_id: "gene-b1218"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1218"
  - "chaC"
---

# chaC

`gene.b1218`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1218`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

chaC (gene.b1218) is a gene entity. It encodes chaC (protein.P39163). Encoded protein function: FUNCTION: Catalyzes the cleavage of glutathione into 5-oxo-L-proline and a Cys-Gly dipeptide. Acts specifically on glutathione, but not on other gamma-glutamyl peptides. {ECO:0000269|PubMed:27913623}. EcoCyc product frame: EG12403-MONOMER. Genomic coordinates: 1272507-1273202. EcoCyc protein note: ChaC is a γ-glutamylcyclotransferase with relatively low catalytic efficiency . Expression of chaC enables growth on glutathione of a mutant yeast organic sulphur auxotroph that can not utilize glutathione and γ-glu amino acids . A chaC mutant shows a defect in swarming motility, but no significant defect in swimming motility .

## Biological Role

Repressed by glaR (protein.P37338).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39163|protein.P39163]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=chaC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004089,ECOCYC:EG12403,GeneID:945793`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1272507-1273202:+; feature_type=gene
