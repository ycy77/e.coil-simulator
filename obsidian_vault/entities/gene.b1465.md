---
entity_id: "gene.b1465"
entity_type: "gene"
name: "narV"
source_database: "NCBI RefSeq"
source_id: "gene-b1465"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1465"
  - "narV"
---

# narV

`gene.b1465`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1465`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

narV (gene.b1465) is a gene entity. It encodes narV (protein.P0AF32). Encoded protein function: FUNCTION: This is a second nitrate reductase enzyme which can substitute for the NRA enzyme and allows E.coli to use nitrate as an electron acceptor during anaerobic growth. The gamma chain is a membrane-embedded heme-iron unit resembling cytochrome b, which transfers electrons from quinones to the beta subunit. EcoCyc product frame: NARV-MONOMER. EcoCyc synonyms: chlZ. Genomic coordinates: 1535937-1536617. EcoCyc protein note: narV encodes the γ subunit of nitrate reductase Z - it has 68% identity with narI (encoding the γ subunit of nitrate reductase A) but 87% similarity at the protein level; it is predicted to be the heme b binding subunit which transfers electrons from the quinone pool to the β subunit .

## Biological Role

Activated by ompR (protein.P0AA16), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF32|protein.P0AF32]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=narV; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=narV; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004889,ECOCYC:EG10644,GeneID:946029`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1535937-1536617:-; feature_type=gene
