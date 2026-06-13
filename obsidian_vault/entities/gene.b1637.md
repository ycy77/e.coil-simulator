---
entity_id: "gene.b1637"
entity_type: "gene"
name: "tyrS"
source_database: "NCBI RefSeq"
source_id: "gene-b1637"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1637"
  - "tyrS"
---

# tyrS

`gene.b1637`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1637`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tyrS (gene.b1637) is a gene entity. It encodes tyrS (protein.P0AGJ9). Encoded protein function: FUNCTION: Catalyzes the attachment of L-tyrosine to tRNA(Tyr) in a two-step reaction: tyrosine is first activated by ATP to form Tyr-AMP and then transferred to the acceptor end of tRNA(Tyr) (PubMed:4292198, PubMed:4579631). Can also mischarge tRNA(Tyr) with D-tyrosine, leading to the formation of D-tyrosyl-tRNA(Tyr), which can be hydrolyzed by the D-aminoacyl-tRNA deacylase (PubMed:4292198). In vitro, can also use the non-natural amino acid azatyrosine (PubMed:11006270). {ECO:0000269|PubMed:11006270, ECO:0000269|PubMed:4292198, ECO:0000269|PubMed:4579631}. EcoCyc product frame: TYRS-MONOMER. Genomic coordinates: 1715948-1717222. EcoCyc protein note: Tyrosine-tRNA ligase (TyrRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. TyrRS belongs to the Class IC aminoacyl tRNA synthetases . The enzyme is a homodimer in solution . TyrRS binds one molecule of tRNATyr per TyrRS dimer and has two binding sites for tyrosine with different dissociation constants . Other reports find two equivalent tyrosinyl-5'-AMP binding sites ; the binding data may require more complex analysis . The reaction mechanism of TyrRS has been studied...

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGJ9|protein.P0AGJ9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005477,ECOCYC:EG11043,GeneID:948855`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1715948-1717222:-; feature_type=gene
