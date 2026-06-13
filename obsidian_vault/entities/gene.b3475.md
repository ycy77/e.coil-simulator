---
entity_id: "gene.b3475"
entity_type: "gene"
name: "acpT"
source_database: "NCBI RefSeq"
source_id: "gene-b3475"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3475"
  - "acpT"
---

# acpT

`gene.b3475`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3475`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

acpT (gene.b3475) is a gene entity. It encodes acpT (protein.P37623). Encoded protein function: FUNCTION: May be involved in an alternative pathway for phosphopantetheinyl transfer and holo-ACP synthesis in E.coli. The native apo-protein substrate is unknown. Is able to functionally replace AcpS in vivo but only when expressed at high levels. {ECO:0000269|PubMed:10625633, ECO:0000269|PubMed:8939709}. EcoCyc product frame: EG12221-MONOMER. EcoCyc synonyms: yhhU. Genomic coordinates: 3612969-3613556. EcoCyc protein note: The carrier protein substrates of AcpT have been identified in E. coli O157:H7 strain EDL933 as Z4853 and Z4854, two proteins in O-island 138 which appears to contain genes for fatty-acid biosynthesis . O-island 138 has been deleted from a K-12 ancestor, but acpT has been retained possibly because AcpT allows slow growth in the absence of AcpS activity . Overexpression of acpT suppresses an acpS mutation . Overexpression of acpT also suppresses the lethality of yejM null mutants, as well as the temperature sensitivity of yejMG570A mutants . This suppression does not require phosphopantetheinyl transferase activity because a mutant lacking this activity was still able to suppress the temperature sensitivity of the yejMG570A mutant .

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37623|protein.P37623]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011351,ECOCYC:EG12221,GeneID:947979`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3612969-3613556:+; feature_type=gene
