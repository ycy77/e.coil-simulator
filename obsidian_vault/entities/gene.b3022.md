---
entity_id: "gene.b3022"
entity_type: "gene"
name: "mqsR"
source_database: "NCBI RefSeq"
source_id: "gene-b3022"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3022"
  - "mqsR"
---

# mqsR

`gene.b3022`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3022`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mqsR (gene.b3022) is a gene entity. It encodes mqsR (protein.Q46865). Encoded protein function: FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. Plays a significant role in the control of biofilm formation and induction of persister cells in the presence of antibiotics. An mRNA interferase which has been reported to be translation-independent (PubMed:19690171, PubMed:19943910, PubMed:23289863). It has also been reported to be translation-dependent (PubMed:20041169). Cleavage has been reported to occur on either side of G in the sequence GCU (PubMed:19690171). Also reported to cleave after C in GC(A/U) sequences (PubMed:19943910). There are only 14 genes in E.coli W3110 (and probably also MG1655) that do not have a GCU sequence and thus are resistant to the mRNA interferase activity; among these is the gene for toxin GhoT. Overexpression of MqsR causes cessation of cell growth and inhibits cell proliferation via inhibition of translation as well as increasing persister cell formation; these effects are overcome by concomitant or subsequent expression of antitoxin MqsA. Cross-talk can occur between different TA systems. Ectopic expression of this toxin induces transcription of the relBEF TA system operon with specific cleavage of the relBEF mRNA produced (PubMed:23432955). Regulates the expression of GhoT/GhoS, a type V TA system (PubMed:23289863)...

## Biological Role

Repressed by mqsA (protein.Q46864). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46865|protein.Q46865]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mqsR; function=+
- `represses` <-- [[protein.Q46864|protein.Q46864]] `RegulonDB` `S` - regulator=MqsA; target=mqsR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009925,ECOCYC:G7572,GeneID:947500`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3168248-3168544:-; feature_type=gene
