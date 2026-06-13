---
entity_id: "gene.b3965"
entity_type: "gene"
name: "trmA"
source_database: "NCBI RefSeq"
source_id: "gene-b3965"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3965"
  - "trmA"
---

# trmA

`gene.b3965`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3965`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trmA (gene.b3965) is a gene entity. It encodes trmA (protein.P23003). Encoded protein function: FUNCTION: Dual-specificity methyltransferase that catalyzes the formation of 5-methyluridine at position 54 (m5U54) in all tRNAs, and that of position 341 (m5U341) in tmRNA (transfer-mRNA). {ECO:0000255|HAMAP-Rule:MF_01011, ECO:0000269|PubMed:23603891, ECO:0000269|PubMed:2999071, ECO:0000269|PubMed:6247318}. EcoCyc product frame: EG11022-MONOMER. EcoCyc synonyms: rT, rumT. Genomic coordinates: 4162170-4163270. EcoCyc protein note: TrmA is the methyltransferase that catalyzes methylation of U54 in the TΨ loop of tRNAs as well as methylation of the corresponding U341 residue within the tRNA-like domain of SSRA-RNA . In addition to its catalytic activity, TrmA also acts as a tRNA chaperone . tRNAs carry multiple modifications, often in nearby nucleotide residues. The preferred substrate for the TrmA methyltransferase activity is unmodified tRNA, while its binding activity is highest with Ψ55-modified tRNA . The catalytic mechanism involves formation of a covalent complex between the catalytic Cys324 residue of the enzyme and tRNA and occurs by single SN2 displacement . Stereochemically, the reaction proceeds by cis addition followed by trans elimination...

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23003|protein.P23003]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=trmA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012983,ECOCYC:EG11022,GeneID:947143`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4162170-4163270:-; feature_type=gene
