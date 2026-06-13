---
entity_id: "gene.b1105"
entity_type: "gene"
name: "lpoB"
source_database: "NCBI RefSeq"
source_id: "gene-b1105"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1105"
  - "lpoB"
---

# lpoB

`gene.b1105`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1105`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lpoB (gene.b1105) is a gene entity. It encodes lpoB (protein.P0AB38). Encoded protein function: FUNCTION: Regulator of peptidoglycan synthesis that is essential for the function of penicillin-binding protein 1B (PBP1b). Stimulates transpeptidase and transglycosylase activities of PBP1b in vitro. May also contribute to outer membrane constriction during cell division, in complex with PBP1b. {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}. EcoCyc product frame: G6565-MONOMER. EcoCyc synonyms: ycfM. Genomic coordinates: 1162638-1163279. EcoCyc protein note: LpoB is an outer membrane lipoprotein that forms a complex with CPLX0-3951 "penicillin binding protein 1B (PBP1B)" and is essential for its peptidoglycan glycosyl transferase activity and/or transpeptidase activity . Purified LpoB interacts with PBPIB and stimulates both its glycosyltransferase and transpeptidase activitities in vitro . LpoB binds and allosterically activates both the transpeptidase and transglycosylase activities of PBP1B (see further ). An lpoB- mutant is synthetically lethal in a PBP1A defective strain and this phenotype can be corrected by the expression of lpoB from a plasmid . Depletion of LpoB in the absence of PBP1A results in the same terminal phenotype as PBP1A- PBP1B- cells and lpoB- mutants show a similar βlactam hypersensitivity phenotype to PBP1B- mutants...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB38|protein.P0AB38]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003733,ECOCYC:G6565,GeneID:948536`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1162638-1163279:+; feature_type=gene
