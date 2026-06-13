---
entity_id: "gene.b2734"
entity_type: "gene"
name: "pphB"
source_database: "NCBI RefSeq"
source_id: "gene-b2734"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2734"
  - "pphB"
---

# pphB

`gene.b2734`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2734`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pphB (gene.b2734) is a gene entity. It encodes pphB (protein.P55799). Encoded protein function: FUNCTION: Has been shown, in vitro, to act on Ser, Thr and Tyr-phosphorylated substrates. EcoCyc product frame: G7415-MONOMER. EcoCyc synonyms: ygbH, prpB. Genomic coordinates: 2859760-2860416. EcoCyc protein note: PphA and PphB are phosphoprotein phosphatases that act in transduction of the misfolded protein stress signal in a pathway that includes the PWY0-1485 and which activates transcription of htrA. PphB exhibits phosphatase activity toward phosphorylated serine/threonine and phosphorylated tyrosine in protein substrates. Additional phosphoproteins accumulate in a pphB mutant, suggesting that they are in vivo targets of PphB . PphA and PphB have similarity to the phosphoprotein phosphatase of bacteriophage lambda (λ-PP) and to Salmonella enterica serovar Typhimurium PrpA and PrpB proteins . A pphB null mutant has a slow growth phenotype . PrpB: "protein phosphatase B" Reviews:

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P55799|protein.P55799]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=pphB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008980,ECOCYC:G7415,GeneID:947196`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2859760-2860416:+; feature_type=gene
