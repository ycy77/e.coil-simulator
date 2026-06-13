---
entity_id: "gene.b3892"
entity_type: "gene"
name: "fdoI"
source_database: "NCBI RefSeq"
source_id: "gene-b3892"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3892"
  - "fdoI"
---

# fdoI

`gene.b3892`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3892`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fdoI (gene.b3892) is a gene entity. It encodes fdoI (protein.P0AEL0). Encoded protein function: FUNCTION: Allows to use formate as major electron donor during aerobic respiration. Subunit gamma is probably the cytochrome b556(FDO) component of the formate dehydrogenase. EcoCyc product frame: FDOI-MONOMER. Genomic coordinates: 4081225-4081860. EcoCyc protein note: fdoI encodes the γ subunit of formate dehydrogenase O. It has 45% amino acid identity (over an alignment of 156 residues) with the heme b binding, γ subunit (FdnI) of formate dehydrogenase-N . Both the N- and C-terminus of FdoI appear to be located in the cytoplasm and it is predicted to have 4 transmembrane regions .

## Biological Role

Repressed by sdhX (gene.b4764).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEL0|protein.P0AEL0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[gene.b4764|gene.b4764]] `RegulonDB` `S` - regulator=SdhX; target=fdoI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012705,ECOCYC:EG11856,GeneID:948383`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4081225-4081860:-; feature_type=gene
