---
entity_id: "gene.b3894"
entity_type: "gene"
name: "fdoG"
source_database: "NCBI RefSeq"
source_id: "gene-b3894"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3894"
  - "fdoG"
---

# fdoG

`gene.b3894`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3894`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fdoG (gene.b3894) is a gene entity. It encodes fdoG (protein.P32176). Encoded protein function: FUNCTION: Allows to use formate as major electron donor during aerobic respiration. Subunit alpha possibly forms the active site. EcoCyc product frame: FDOG-MONOMER. Genomic coordinates: 4082772-4085822. EcoCyc protein note: fdoG encodes the α subunit of formate dehydrogenase O. It has 75% amino acid identity with FDNG-MONOMER FdnG - the catalytic, molybdopterin cofactor containing α subunit of formate dehydrogenase-N. It contains an in-frame TGA (opal) codon that specifies selenocysteine . Topology analysis suggests that FdoG is located in the cytoplasm ; however, the use or reporter fusions to determine toplogy of Tat-dependent proteins has been brought into question .

## Biological Role

Repressed by sdhX (gene.b4764), nac (protein.Q47005).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32176|protein.P32176]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[gene.b4764|gene.b4764]] `RegulonDB` `S` - regulator=SdhX; target=fdoG; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=fdoG; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012710,ECOCYC:EG11858,GeneID:948394`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4082772-4085822:-; feature_type=gene
