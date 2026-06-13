---
entity_id: "gene.b4094"
entity_type: "gene"
name: "phnN"
source_database: "NCBI RefSeq"
source_id: "gene-b4094"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4094"
  - "phnN"
---

# phnN

`gene.b4094`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4094`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phnN (gene.b4094) is a gene entity. It encodes phnN (protein.P16690). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of ribose 1,5-bisphosphate to 5-phospho-D-ribosyl alpha-1-diphosphate (PRPP). Accepts ATP but not GTP as a phosphoryl donor, and uses ribose 1,5-bisphosphate but not ribose, ribose 1-phosphate, or ribose 5-phosphate as a phosphoryl acceptor. {ECO:0000269|PubMed:12700258, ECO:0000269|PubMed:19733071}. EcoCyc product frame: EG10723-MONOMER. Genomic coordinates: 4315525-4316082. EcoCyc protein note: PhnN was found to catalyze the ribose 1,5-bisphosphokinase reaction in the PWY-7805 pathway. phnN is part of a phosphate starvation-inducible operon that is required for use of phosphonate and phosphite as phosphorous sources . It was initially suggested that PhnN might be a subunit or an accessory factor of a C-P lyase. phnN insertion mutants show reduced growth on phosphite and methylphosphonate as a source of phosphorous . Derepression of phnN expression suppresses the NAD requirement of a Δprs mutant . The authors proposed a PRPP biosynthesis pathway involving phosphoribomutase (DeoB), a hypothesized ribose-1-phosphokinase, and PhnN. Overexpression of phnN increases the tolerance of E. coli to n-butanol . Reviews:

## Biological Role

Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16690|protein.P16690]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=phnN; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=phnN; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013417,ECOCYC:EG10723,GeneID:948608`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4315525-4316082:-; feature_type=gene
