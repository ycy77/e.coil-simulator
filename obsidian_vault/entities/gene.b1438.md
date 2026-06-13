---
entity_id: "gene.b1438"
entity_type: "gene"
name: "hicB"
source_database: "NCBI RefSeq"
source_id: "gene-b1438"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1438"
  - "hicB"
---

# hicB

`gene.b1438`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1438`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hicB (gene.b1438) is a gene entity. It encodes hicB (protein.P67697). Encoded protein function: FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Functions as an mRNA interferase antitoxin; overexpression prevents HicA-mediated cessation of cell growth and inhibition of cell proliferation. {ECO:0000269|PubMed:19060138}. EcoCyc product frame: G6749-MONOMER. EcoCyc synonyms: ydcQ. Genomic coordinates: 1509508-1509924. EcoCyc protein note: HicB acts as the antitoxin of the HicA-HicB toxin-antitoxin system, and it also regulates the transcription of the operon that encodes the toxin-antitoxin system. HicB recognizes and binds an inverted repeat DNA sequence to regulate transcription, suggesting that HicB binds to DNA as a dimer . An HTH motif has been identified in the C terminus of HicB . Overexpression of HicA induces mRNA cleavage and growth inhibition, but not cell death. Expression of HicB neutralizes the effect of HicA . The loss of HicB downregulates the extracytoplasmic stress response mediated by σE and the production of outer membrane vesicles. It reduces the cellular levels of DegP and Spy and downregulates the Cpx response independently of CpxR . hicB insertion mutants suppress the essential nature of RPOE-MONOMER σE...

## Biological Role

Repressed by hicB (protein.P67697). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P67697|protein.P67697]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hicB; function=+
- `represses` <-- [[protein.P67697|protein.P67697]] `RegulonDB` `C` - regulator=HicB; target=hicB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004796,ECOCYC:G6749,GeneID:946001`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1509508-1509924:+; feature_type=gene
