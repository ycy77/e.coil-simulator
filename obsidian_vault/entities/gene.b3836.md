---
entity_id: "gene.b3836"
entity_type: "gene"
name: "tatA"
source_database: "NCBI RefSeq"
source_id: "gene-b3836"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3836"
  - "tatA"
---

# tatA

`gene.b3836`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3836`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tatA (gene.b3836) is a gene entity. It encodes tatA (protein.P69428). Encoded protein function: FUNCTION: Part of the twin-arginine translocation (Tat) system that transports large folded proteins containing a characteristic twin-arginine motif in their signal peptide across membranes. TatA could form the protein-conducting channel of the Tat system. {ECO:0000255|HAMAP-Rule:MF_00236, ECO:0000269|PubMed:11922668, ECO:0000269|PubMed:9649434}. EcoCyc product frame: TATA. EcoCyc synonyms: yigT, mttA1. Genomic coordinates: 4021945-4022214. EcoCyc protein note: TatA is an inner membrane component of the twin arginine translocation (Tat) complex for the export of folded proteins. Homo-oligomeric TatA may form the translocation pore of the complex although other models have been also suggested . TatA is predicted to consist of an N-terminal transmembrane domain followed by an amphipathic helix and a cytoplasmic domain . The topology of TatA has been debated with studies variously suggesting that TatA is exposed at the cytoplasmic face of the membrane , that the N-terminus is located in the periplasm while the C-terminal region adopts a dual topology , that the N-terminus is located in the cytoplasm and the C-terminus adopts a dual topology or that it has a fixed Nout:Cin topology...

## Enriched Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69428|protein.P69428]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012541,ECOCYC:G7806,GeneID:948321`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4021945-4022214:+; feature_type=gene
