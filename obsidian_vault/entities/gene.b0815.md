---
entity_id: "gene.b0815"
entity_type: "gene"
name: "opgE"
source_database: "NCBI RefSeq"
source_id: "gene-b0815"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0815"
  - "opgE"
---

# opgE

`gene.b0815`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0815`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

opgE (gene.b0815) is a gene entity. It encodes opgE (protein.P75785). Encoded protein function: FUNCTION: Catalyzes the addition of a phosphoethanolamine moiety to the osmoregulated periplasmic glucan (OPG) backbone. {ECO:0000269|PubMed:24228245}. EcoCyc product frame: G6418-MONOMER. EcoCyc synonyms: ybiP. Genomic coordinates: 851014-852597. EcoCyc protein note: OpgE is required for wild-type phosphoethanolamine modification of the branched periplasmic oligosaccharides known as CPD-16398 osmoregulated periplasmic glucans (OPG), formerly called membrane-derived oligosaccharides (MDO). OpgE is suggested to catalyse the transfer of a phosphoethanolamine group from phosphatidylethanolamine in the membrane to OPG in the periplasm. OPGs extracted from opgB- opgC- opgE- cells (opgB214::Tn10 opgC::Tn5 opgE2::cml) are not substituted with phosphoglycerol, succinyl nor phosphoethanolamine moieties. OPGs extracted from opgB- opgC- cells (opgB214::Tn10 opgC::Tn5) contain phosphoethanolamine substitutions but do not contain phosphoglycerol nor succinyl modifications . OpgE is predicted to contain 4 transmembrane segments plus a periplasmic domain with sulfuric ester hydrolase and transferase activity . Mutant strains lacking substituents do not have an observable phenotype .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75785|protein.P75785]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002786,ECOCYC:G6418,GeneID:945360`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:851014-852597:-; feature_type=gene
