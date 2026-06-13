---
entity_id: "gene.b3893"
entity_type: "gene"
name: "fdoH"
source_database: "NCBI RefSeq"
source_id: "gene-b3893"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3893"
  - "fdoH"
---

# fdoH

`gene.b3893`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3893`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fdoH (gene.b3893) is a gene entity. It encodes fdoH (protein.P0AAJ5). Encoded protein function: FUNCTION: Allows to use formate as major electron donor during aerobic respiration. The beta chain is an electron transfer unit containing 4 cysteine clusters involved in the formation of iron-sulfur centers. Electrons are transferred from the gamma chain to the molybdenum cofactor of the alpha subunit (By similarity). {ECO:0000250}. EcoCyc product frame: FDOH-MONOMER. Genomic coordinates: 4081857-4082759. EcoCyc protein note: fdoH encodes the β subunit of formate dehydrogenase O. It has 100% amino acid identity with FdnH, the [4Fe-4S] containing β subunit of formate dehydrogenase-N. FdoH is essentially hydrophilic in nature with one predicted α helical region at the C-terminus. The topological orientation of FdoH appears to be the reverse of FdnH, with the bulk of the protein located in the cytoplasm however the use or reporter fusions to determine toplogy of Tat-dependent proteins has been brought into question .

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

- `encodes` --> [[protein.P0AAJ5|protein.P0AAJ5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[gene.b4764|gene.b4764]] `RegulonDB` `S` - regulator=SdhX; target=fdoH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012708,ECOCYC:EG11857,GeneID:948395`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4081857-4082759:-; feature_type=gene
