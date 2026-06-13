---
entity_id: "gene.b1838"
entity_type: "gene"
name: "pphA"
source_database: "NCBI RefSeq"
source_id: "gene-b1838"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1838"
  - "pphA"
---

# pphA

`gene.b1838`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1838`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pphA (gene.b1838) is a gene entity. It encodes pphA (protein.P55798). Encoded protein function: FUNCTION: Plays a key role in signaling protein misfolding via the CpxR/CPXA transducing system. It also modulates the phosphorylated status of many phosphoproteins in E.coli, some of which acting as major chaperones. Has been shown, in vitro, to act on Ser, Thr and Tyr-phosphorylated substrates. EcoCyc product frame: G7011-MONOMER. EcoCyc synonyms: yebX, prpA. Genomic coordinates: 1922313-1922969. EcoCyc protein note: PphA and PphB are phosphoprotein phosphatases that act in transduction of the misfolded protein stress signal in a pathway that includes the PWY0-1485 and which activates transcription of htrA. PphA is involved in induction of the heat shock response. PphA exhibits phosphatase activity toward phosphorylated serine/threonine and phosphorylated tyrosine in protein substrates and PHOSPHO-CPXR phosphorylated CpxR. Additional phosphoproteins accumulate in a pphA mutant, suggesting that they are in vivo targets of PphA . PphA and PphB have similarity to the phosphoprotein phosphatase of bacteriophage lambda (λ-PP) and to Salmonella enterica serovar Typhimurium PrpA and PrpB proteins . A pphA null mutant has a slow growth phenotype. Overexpression of pphA induces the heat shock response...

## Biological Role

Activated by rpoH (protein.P0AGB3), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P55798|protein.P55798]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=pphA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=pphA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006114,ECOCYC:G7011,GeneID:946356`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1922313-1922969:-; feature_type=gene
